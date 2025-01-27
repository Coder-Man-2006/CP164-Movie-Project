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

from functions import median_scores

def test_median_scores():
    with open("numbers.txt", "r") as fv:
        median = median_scores(fv)
        print(f"Median: {median}")  # Expected: Value depends on numbers in "numbers.txt"

test_median_scores()