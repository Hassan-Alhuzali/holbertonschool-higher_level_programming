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
