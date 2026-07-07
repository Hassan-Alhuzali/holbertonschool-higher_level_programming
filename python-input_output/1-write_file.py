#!/usr/bin/python3
"""
Writes a string to a text file (UTF-8) and returns
the number of characters written.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8) and returns
    the number of characters written."""

    with open("test.py", "w", encoding="UTF-8") as data_is_written:
        return data_is_written.write(text)
