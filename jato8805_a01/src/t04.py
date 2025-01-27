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

from functions import find_subs

def test_find_subs():
    print(find_subs("It was a really, really, big assignment.", "real"))  # Expected: [9, 17]
    print(find_subs("aaaa", "aa"))  # Expected: [0, 2]

test_find_subs()