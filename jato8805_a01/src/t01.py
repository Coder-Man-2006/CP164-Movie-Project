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
from functions import clean_list

def test_clean_list():
    values = [1, 2, 0, 1, 4, 1, 1, 2, 2, 5, 4, 3, 1, 3, 3, 4, 2, 4, 3, 1, 3, 0, 3, 0, 0]
    clean_list(values)
    print(f"After cleaning: {values}")  # Expected: [1, 2, 0, 4, 5, 3]

test_clean_list()