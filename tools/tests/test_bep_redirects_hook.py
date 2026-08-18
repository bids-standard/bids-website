"""Tests for the mkdocs on_config hook that auto-populates BEP redirects."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType, SimpleNamespace

import pytest
import ruamel.yaml

HOOK_PATH = (
    Path(__file__).resolve().parents[1] / "build" / "bep_redirects_hook.py"
)


def _load_hook() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "bep_redirects_hook", HOOK_PATH
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["bep_redirects_hook"] = module
    spec.loader.exec_module(module)
    return module


def _make_config(redirect_maps: dict[str, str] | None) -> dict:
    if redirect_maps is None:
        return {"plugins": {}}
    redirects_plugin = SimpleNamespace(
        config={"redirect_maps": dict(redirect_maps)}
    )
    return {"plugins": {"redirects": redirects_plugin}}


def test_hook_injects_from_real_beps_yml() -> None:
    """Every BEP in data/beps/beps.yml gets bep{NNN}.md + bep{NNN}/index.md."""
    hook = _load_hook()
    config = _make_config({"foo.md": "bar.md"})

    hook.on_config(config)

    redirect_maps = config["plugins"]["redirects"].config["redirect_maps"]
    yaml = ruamel.yaml.YAML(typ="safe")
    beps = yaml.load(hook._BEPS_YML)
    for bep in beps:
        n = bep["number"]
        expected = f"extensions/beps/bep_{n}.md"
        assert redirect_maps[f"bep{n}.md"] == expected
        assert redirect_maps[f"bep{n}/index.md"] == expected


def test_hook_preserves_pre_existing_entries() -> None:
    """Manual entries in mkdocs.yml redirect_maps must not be overwritten."""
    hook = _load_hook()
    manual_target = "https://example.org/kept.html"
    # '045' is present in beps.yml — hook must not clobber a manual entry.
    config = _make_config({"bep045.md": manual_target})

    hook.on_config(config)

    redirect_maps = config["plugins"]["redirects"].config["redirect_maps"]
    assert redirect_maps["bep045.md"] == manual_target


def test_hook_mirrors_manual_entries_with_index_md() -> None:
    """Manual bepNNN.md entries also get a bepNNN/index.md mirror."""
    hook = _load_hook()
    external = "https://bids-specification.readthedocs.io/en/stable/x.html"
    config = _make_config({"bep001.md": external})

    hook.on_config(config)

    redirect_maps = config["plugins"]["redirects"].config["redirect_maps"]
    assert redirect_maps["bep001.md"] == external
    assert redirect_maps["bep001/index.md"] == external


def test_hook_leaves_non_bep_entries_alone() -> None:
    """Non-BEP redirect keys are ignored — only bepNNN.md gets mirrored."""
    hook = _load_hook()
    config = _make_config(
        {"news.md": "blog/index.md", "beyond-bep.md": "somewhere.md"}
    )
    hook.on_config(config)
    redirect_maps = config["plugins"]["redirects"].config["redirect_maps"]
    assert "news/index.md" not in redirect_maps
    assert "beyond-bep/index.md" not in redirect_maps


def test_hook_is_noop_without_redirects_plugin() -> None:
    """No redirects plugin -> hook returns without raising."""
    hook = _load_hook()
    config = _make_config(None)
    hook.on_config(config)
    assert config == {"plugins": {}}


def test_hook_uses_isolated_fixture(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """With a controlled beps.yml fixture only its numbers get injected."""
    hook = _load_hook()
    fixture = tmp_path / "beps.yml"
    fixture.write_text(
        "- number: '100'\n"
        "  google_doc: https://example.org/\n"
        "- number: '200'\n"
        "  pull_request: https://example.org/pr\n"
    )
    monkeypatch.setattr(hook, "_BEPS_YML", fixture)

    config = _make_config({})
    hook.on_config(config)

    redirect_maps = config["plugins"]["redirects"].config["redirect_maps"]
    assert redirect_maps == {
        "bep100.md": "extensions/beps/bep_100.md",
        "bep100/index.md": "extensions/beps/bep_100.md",
        "bep200.md": "extensions/beps/bep_200.md",
        "bep200/index.md": "extensions/beps/bep_200.md",
    }
