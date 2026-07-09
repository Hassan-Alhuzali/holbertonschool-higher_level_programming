#!/usr/bin/python3
"""
Loads a Python object from a JSON file
"""


def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file
    """
    import json
    with open(filename, 'r') as f:
        return json.load(f)


def add_item(filename, item):
    """
    Adds an item to a JSON file
    """
    import json
    with open(filename, 'w') as f:
        json.dump(item, f)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: {} <filename> <item>".format(sys.argv[0]))
        sys.exit(1)
    filename = sys.argv[1]
    item = sys.argv[2]
    add_item(filename, item)
    print("Item added to {}".format(filename))
