#!/usr/bin/python3
"""
Saves a Python object to a JSON file
"""


def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a JSON file
    """
    import json
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
