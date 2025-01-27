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

from functions import list_subtraction

def test_list_subtraction():
    minuend = [5, 5, 4, 5]
    subtrahend = [5]
    list_subtraction(minuend, subtrahend)
    print(f"After subtraction: {minuend}")  # Expected: [4]

test_list_subtraction()