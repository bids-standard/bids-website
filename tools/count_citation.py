from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import requests
from bids_website.utils import data_dir
from pyzotero import zotero
from rich import print
import os

DEBUG = False
VERBOSE = True
MINIMUM_YEAR = 2016

TOKEN_FILE = "/home/remi/Documents/tokens/open_citations_access_token.txt"

OUTPUT_FILE = data_dir() / "count_citation.tsv"

# requires token from https://opencitations.net/index/coci/api/v1/token
# saved in token.txt


def main():
    # List dois for BIDS papers from zotero group
    zot = zotero.Zotero(library_id="5111637", library_type="group")
    items = zot.everything(zot.top())
    with open(data_dir() / "papers.json", "w") as f:
        json.dump(items, f, indent=" ")

    papers = {}
    for item in items:
        if VERBOSE:
            print(item)
        title = (
            item["data"].get("shortTitle")
            or item["data"].get("title").split(",")[0]
        )

        DOI = item["data"].get("DOI")
        if not DOI:
            if extra := item["data"].get("extra"):
                DOI = extra.replace("DOI: ", "")

        if DOI:
            papers[title] = DOI

    print(papers)

    query_api(papers)


def return_citation_count_per_year(citations_doi: str) -> dict[str, int]:
    if not citations_doi:
        return {}
    citation_count_per_year = {}
    citations_doi = citations_doi.replace("; ", "__")
    print(f"Trying querying all citing papers at once: {citations_doi}")
    if metadata := query_for_metadata(citations_doi):
        for citation in metadata:
            year = citation["year"]
            if "-" in year:
                year = year.split("-")[0]
            if int(year) < MINIMUM_YEAR:
                continue
            if year in citation_count_per_year:
                citation_count_per_year[year] += 1
            else:
                citation_count_per_year[year] = 1
    else:
        citations_doi = citations_doi.split("__")
        print(f" querying papers one by one: {citations_doi}")
        for citation in citations_doi:
            if VERBOSE:
                print(f"  querying: {citation}")
            if metadata := query_for_metadata(citation):
                year = metadata[0]["year"].split("-")[0]
                print(year)
                try:
                    if int(year) < MINIMUM_YEAR:
                        continue
                except:  # noqa
                    print("skipping")
                    continue
                if year in citation_count_per_year:
                    citation_count_per_year[year] += 1
                else:
                    citation_count_per_year[year] = 1
    return citation_count_per_year


def query_for_metadata(doi: str) -> dict[str, str]:
    with open(TOKEN_FILE) as f:
        token = f.read().strip()
    headers = {"authorization": token}
    api_call = f"https://opencitations.net/index/coci/api/v1/metadata/{doi}"
    r = requests.get(api_call, headers=headers)
    if r.status_code == 200:
        return r.json()
    print(f"[red]Error: {r.status_code}[/red]")
    return {}


def query_api(papers: dict[str, str]) -> dict[str, list[str] | list[int]]:
    """
    Use requests to query papers that cited each paper listed in dict.
    """
    df = {"papers": [], "years": [], "nb_citations": []}

    for i, paper_ in enumerate(papers):
        if i > 4 and DEBUG:
            break
        print(f" {paper_}")
        if metadata := query_for_metadata(papers[paper_]):
            print(metadata)
            if citations := metadata[0]["citation"]:
                citation_count_per_year = return_citation_count_per_year(
                    citations
                )
                print(f" citation per year: {citation_count_per_year}")
                for year in citation_count_per_year:
                    df["papers"].append(paper_)
                    df["years"].append(int(year))
                    df["nb_citations"].append(citation_count_per_year[year])
        pd.DataFrame(df).to_csv(OUTPUT_FILE, sep="\t", index=False)

    return pd.DataFrame(df)


def save_dataframe_to_file(df: pd.DataFrame, file_path: Path):
    """Save DataFrame to TSV"""
    if not df.empty:
        df.to_csv(file_path, sep="\t", index=False)


if __name__ == "__main__":
    main()
