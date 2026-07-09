#!/usr/bin/python3
"""
Appends a string to a text file
"""
def append_write(filename="", text=""):
    """
    Appends a string to a text file
    """
    with open(filename, 'a') as f:
        f.write(text)
    return len(text)
