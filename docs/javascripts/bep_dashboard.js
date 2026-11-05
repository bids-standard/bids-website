// Fill the activity columns of the "Active BEPs" table from the
// bids-schema BEPs/dashboard.json feed. All collection happens in
// bids-schema; this file only formats the feed's raw values.
// See templates/beps_active_table_md.jinja.
(function () {
  "use strict";

  var DAY_MS = 86400000;
  var DASH = "—";

  function daysSince(iso, now) {
    return Math.floor((now - new Date(iso).getTime()) / DAY_MS);
  }

  function plural(n, word) {
    return n + " " + word + (n === 1 ? "" : "s");
  }

  function link(href, text) {
    var a = document.createElement("a");
    a.href = href;
    a.textContent = text;
    return a;
  }

  // Each formatter returns {node|text, sort} for one cell.
  function docCell(e, thresholds, now) {
    if (!e.google_doc) return { text: DASH, sort: "" };
    var act = e.doc_activity;
    if (!act || !act.last_modified) {
      return { node: link(e.google_doc, "⚪ Unknown"), sort: "99999" };
    }
    var days = daysSince(act.last_modified, now);
    var icon = days <= thresholds.fresh ? "🟢"
      : days <= thresholds.active ? "🟡" : "🔴";
    var label = icon + " Edited " + plural(days, "day") + " ago";
    if (act.edits_since_last_check) {
      label += " (+" + plural(act.edits_since_last_check, "edit") + ")";
    }
    return { node: link(e.google_doc, label), sort: String(days) };
  }

  function count(n) {
    return n === null || n === undefined
      ? { text: DASH, sort: "" }
      : { text: String(n), sort: String(n) };
  }

  function reviewsCell(r) {
    if (!r) return { text: DASH, sort: "" };
    var parts = [];
    if (r.approved) parts.push(r.approved + "✅");
    if (r.changes_requested) parts.push(r.changes_requested + "❌");
    if (r.commented) parts.push(r.commented + "💬");
    var total = (r.approved || 0) + (r.changes_requested || 0) + (r.commented || 0);
    return { text: parts.length ? parts.join("/") : "0", sort: String(total) };
  }

  function unresolvedCell(n) {
    if (n === null || n === undefined) return { text: DASH, sort: "" };
    if (n === 0) return { text: "0", sort: "0" };
    var b = document.createElement("strong");
    b.textContent = String(n);
    return { node: b, sort: String(n) };
  }

  function buildCell(pr) {
    var status = pr && pr.build_status;
    if (status === "success") return { text: "✅", sort: "1" };
    if (status === "failed") return { text: "❌", sort: "0" };
    return { text: DASH, sort: "" };
  }

  function cellsFor(e, thresholds, now) {
    var pr = e && e.pr;
    var comments = pr && pr.comments;
    return {
      doc: e ? docCell(e, thresholds, now) : { text: DASH, sort: "" },
      authors: count(pr && pr.authors),
      commenters: count(pr && pr.commenters),
      build: buildCell(pr),
      reviews: reviewsCell(pr && pr.reviews),
      unresolved: unresolvedCell(pr && pr.unresolved_threads),
      comments: count(comments && comments.total),
      last_comment: comments && comments.last_at
        ? { text: comments.last_at.slice(0, 10), sort: comments.last_at }
        : { text: DASH, sort: "" },
      schema: e && e.schema_url
        ? { node: link(e.schema_url, "JSON"), sort: "1" }
        : { text: DASH, sort: "" },
    };
  }

  function apply(span, cell) {
    span.textContent = "";
    if (cell.node) span.appendChild(cell.node);
    else span.textContent = cell.text;
    var td = span.closest("td");
    if (td) td.setAttribute("data-sort", cell.sort);
  }

  function fill(status, data) {
    var thresholds = data.thresholds_days || { fresh: 30, active: 180 };
    var now = Date.now();
    var cache = {};
    document.querySelectorAll("span[data-bep][data-field]").forEach(function (span) {
      var bep = span.getAttribute("data-bep");
      if (!cache[bep]) cache[bep] = cellsFor(data.beps[bep], thresholds, now);
      apply(span, cache[bep][span.getAttribute("data-field")] || { text: DASH, sort: "" });
    });
    status.textContent = "Activity data from ";
    status.appendChild(link("https://github.com/bids-standard/bids-schema/tree/main/BEPs", "bids-schema"));
    status.appendChild(document.createTextNode(
      data.data_as_of ? ", collected " + data.data_as_of.slice(0, 10) + "." : "."));
  }

  function fail(status) {
    document.querySelectorAll("span[data-bep][data-field]").forEach(function (span) {
      apply(span, { text: DASH, sort: "" });
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
