"""
-------------------------------------------------------
Movie class definition.
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
Section: CP164 B
__updated__ = "2025-01-11"
-------------------------------------------------------
"""

from functions import file_analyze

def test_file_analyze():
    with open("sample.txt", "r") as fv:
        upp, low, dig, whi, rem = file_analyze(fv)
        print(f"Uppercase: {upp}, Lowercase: {low}, Digits: {dig}, Whitespace: {whi}, Remaining: {rem}")

test_file_analyze()