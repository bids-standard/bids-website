from __future__ import annotations

import pytest
from scripts.count_citation import load_dataframe_from_file, query_api


@pytest.fixture
def test_file(tmp_path):
    # Create a temporary file and write test data to it
    test_file = tmp_path / "test.tsv"
    test_file.write_text("col1\tcol2\n1\ta\n2\tb\n")
    yield test_file
    # Delete the temporary file
    test_file.unlink()


def test_load_dataframe_from_file(test_file):
    # Call the function with the test file path
    df = load_dataframe_from_file(test_file)

    # Assert that the returned DataFrame is as expected
    assert df.to_dict() == {"col1": {0: 1, 1: 2}, "col2": {0: "a", 1: "b"}}


def test_query_api(requests_mock):
    # Setup mock response for API query
    papers = {"bids-app": "1234", "not-a-paper": "5678"}
    requests_mock.get(
        "https://opencitations.net/index/coci/api/v1/references/1234",
        json=[
            {"citing": {"DOI": "10.1234/foo"}},
            {"citing": {"DOI": "10.5678/bar"}},
        ],
    )
    requests_mock.get(
        "https://opencitations.net/index/coci/api/v1/references/5678",
        status_code=404,
    )

    # Call the function with test papers
    result = query_api(papers)

    # Assert that the returned dict is as expected
    assert result == {"papers": ["bids-app"], "nb_citations": [2]}
