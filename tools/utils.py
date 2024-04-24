from __future__ import annotations

from pathlib import Path


def root_dir():
    return Path(__file__).parent.parent.absolute()


def bids_spec_dir():
    return root_dir() / "bids-specification"


def data_dir():
    return root_dir() / "data"


def figures_dir():
    return root_dir() / "images"
