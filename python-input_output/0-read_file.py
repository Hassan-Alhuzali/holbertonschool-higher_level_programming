#!/usr/bin/python3
"""
Reads a file and prints its content to stdout.
"""


def read_file(filename=""):
    """Reads a file and prints its content to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        """Reads the content of the file."""
        content = f.read()
        print(content, end="")
