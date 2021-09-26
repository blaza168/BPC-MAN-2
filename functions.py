from entry import Entry
import re

def parse_entry(str):
    # First , is name.
    comma_index = str.find(",")
    name = str[0:comma_index]

    str = str[comma_index:]
    print("name")
    print(name)