// Fill the "Activity" table under "Proposed" BEPs from the
// bids-schema BEPs/dashboard.json feed. All collection happens in
// bids-schema; this file only formats the feed's raw values.
// See templates/beps_activity_table_md.jinja.
(function () {
  "use strict";

  var DAY_MS = 86400000;
  var DASH = "—";
  var NONE = { text: DASH, sort: "" };

  function daysSince(iso, now) {
    return Math.floor((now - new Date(iso).getTime()) / DAY_MS);
  }

  function link(href, text) {
    var a = document.createElement("a");
    a.href = href;
    a.textContent = text;
    return a;
  }

  function orDash(n) {
    return n === null || n === undefined ? DASH : String(n);
  }

  // Each formatter returns {node|text, sort} for one cell. A cell without
  // `sort` leaves the <td>'s sort value alone.

  // Most recent of Google Doc edit, PR commit, and PR comment: a
  // traffic-light dot, the day count, and the source, linked to the doc or
  // PR. The tooltip lists all three dates. Merging these keeps a BEP whose
  // Google Doc has been superseded by its PR from looking stalled.
  function activityCell(e, thresholds, now) {
    var pr = e.pr || {};
    var doc = e.doc_activity || {};
    var sources = [
      { at: doc.last_modified, label: "Doc edit", href: e.google_doc },
      { at: pr.commits && pr.commits.last_at, label: "PR commit", href: e.pr_url },
      { at: pr.comments && pr.comments.last_at, label: "PR comment", href: e.pr_url },
    ];
    var known = sources.filter(function (s) { return s.at; });
    if (!known.length) return NONE;
    known.sort(function (a, b) { return new Date(b.at) - new Date(a.at); });
    var last = known[0];
    var days = daysSince(last.at, now);
    var icon = days <= thresholds.fresh ? "\uD83D\uDFE2"
      : days <= thresholds.active ? "\uD83D\uDFE1" : "\uD83D\uDD34";
    var span = document.createElement("span");
    span.appendChild(document.createTextNode(icon + " " + days + " \u00B7 "));
    // Non-breaking spaces keep "PR commit" etc. on one line in narrow cells.
    var label = last.label.replace(/ /g, "\u00A0");
    span.appendChild(last.href ? link(last.href, label) : document.createTextNode(label));
    span.title = sources.map(function (s) {
      return s.label + ": " + (s.at ? s.at.slice(0, 10) : DASH);
    }).join("\n");
    return { node: span, sort: String(days) };
  }

  function buildIcon(pr) {
    if (pr.build_status === "success") return "✅";
    if (pr.build_status === "failed") return "❌";
    return DASH;
  }

  // Marker for BEPs whose PR has no data in the feed (no schema build),
  // pointing at the note under the table.
  function notReadyMarker() {
    var sup = document.createElement("sup");
    var a = link("#bep-not-schema-ready", "*");
    a.title = "Not yet schema-ready: status uncertain";
    sup.appendChild(a);
    return sup;
  }

  // Follows the static "doc/PR" links: "/authors/commenters/build". The cell
  // sorts by PR number (see apply).
  function prRestCell(pr) {
    if (!pr) return { node: notReadyMarker(), sort: "pr" };
    return {
      text: "/" + orDash(pr.authors) + "/" + orDash(pr.commenters) + "/" + buildIcon(pr),
      sort: "pr",
    };
  }

  // e.g. "2 ✅/29 💬", with a non-breaking space between each count and icon.
  function reviewsCell(r) {
    if (!r) return NONE;
    var parts = [];
    if (r.approved) parts.push(r.approved + "\u00A0✅");
    if (r.changes_requested) parts.push(r.changes_requested + "\u00A0❌");
    if (r.commented) parts.push(r.commented + "\u00A0💬");
    var total = (r.approved || 0) + (r.changes_requested || 0) + (r.commented || 0);
    return { text: parts.length ? parts.join("/") : "0", sort: String(total) };
  }

  // "days since last comment / # comments / # unresolved" (unresolved bolded
  // when > 0). Sorts by days.
  function commentsCell(pr, now) {
    if (!pr) return NONE;
    var c = pr.comments || {};
    var days = c.last_at ? daysSince(c.last_at, now) : null;
    var frag = document.createDocumentFragment();
    frag.appendChild(document.createTextNode(orDash(days) + "/" + orDash(c.total) + "/"));
    var n = pr.unresolved_threads;
    if (n) {
      var b = document.createElement("strong");
      b.textContent = String(n);
      frag.appendChild(b);
    } else {
      frag.appendChild(document.createTextNode(orDash(n)));
    }
    return { node: frag, sort: days === null ? "" : String(days) };
  }

  function cellsFor(e, thresholds, now) {
    if (!e) {
      return { activity: NONE, pr_rest: prRestCell(null), reviews: NONE, comments: NONE };
    }
    return {
      activity: activityCell(e, thresholds, now),
      pr_rest: prRestCell(e.pr),
      reviews: reviewsCell(e.pr && e.pr.reviews),
      comments: commentsCell(e.pr, now),
    };
  }

  function apply(span, cell) {
    span.textContent = "";
    if (cell.node) span.appendChild(cell.node);
    else span.textContent = cell.text;
    var td = span.closest("td");
    if (!td || cell.sort === undefined) return;
    var sort = cell.sort;
    if (sort === "pr") {
      // Combined Doc/PR cell: sort by the PR number in its static link
      // (the 📄 Google Doc link comes first, so match the PR URL).
      var a = td.querySelector('a[href*="/pull/"]');
      sort = a ? a.textContent.trim() : "";
    }
    td.setAttribute("data-sort", sort);
  }

  function fill(status, data) {
    var thresholds = data.thresholds_days || { fresh: 30, active: 180 };
    var now = Date.now();
    var cache = {};
    var notReady = false;
    document.querySelectorAll("span[data-bep][data-field]").forEach(function (span) {
      var bep = span.getAttribute("data-bep");
      if (!cache[bep]) cache[bep] = cellsFor(data.beps[bep], thresholds, now);
      var field = span.getAttribute("data-field");
      if (field === "pr_rest" && !(data.beps[bep] && data.beps[bep].pr)) notReady = true;
      apply(span, cache[bep][field] || NONE);
    });
    var note = document.getElementById("bep-not-schema-ready");
    if (note) note.hidden = !notReady;
    status.textContent = "Activity data from ";
    status.appendChild(link("https://github.com/bids-standard/bids-schema/tree/main/BEPs", "bids-schema"));
    status.appendChild(document.createTextNode(
      data.data_as_of ? ", collected " + data.data_as_of.slice(0, 10) + "." : "."));
  }

  function fail(status) {
    document.querySelectorAll("span[data-bep][data-field]").forEach(function (span) {
      // Without the feed nothing is known to be not schema-ready: no marker.
      apply(span, span.getAttribute("data-field") === "pr_rest"
        ? { text: "", sort: "pr" } : NONE);
    });
    status.textContent = "Activity data is temporarily unavailable.";
  }

  function init() {
    var status = document.querySelector(".bep-dashboard-status[data-src]");
    if (!status) return;
    status.textContent = "Loading activity data…";
    fetch(status.getAttribute("data-src"), { cache: "no-cache" })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (data) { fill(status, data); })
      .catch(function (err) {
        console.warn("BEP dashboard:", err);
        fail(status);
      });
  }

  // Material's instant navigation re-renders pages without a full reload.
  if (typeof document$ !== "undefined") document$.subscribe(init);
  else document.addEventListener("DOMContentLoaded", init);
})();
