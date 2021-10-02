from entry import Entry
import re

entry_pattern = "([\w ]+),([^\d]+),([^\d]+),(\d+),(\d+)"


def parse_entry(str):
    searchObj = re.search(entry_pattern, str, re.M | re.I)

    if "Lincoln" in str:
        print("here")

    if searchObj:
        publications = int(searchObj.group(4))
        citations = int(searchObj.group(5))
        return Entry(
            searchObj.group(1),
            searchObj.group(2),
            searchObj.group(3),
            publications,
            citations
        )
    else:
        raise Exception("Invalid entry! " + str)