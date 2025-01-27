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

from functions import matrixes_multiply

def test_matrixes_multiply():
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[7, 8], [9, 10], [11, 12]]
    result = matrixes_multiply(a, b)
    print(f"Matrix product: {result}")  # Expected: [[58, 64], [139, 154]]

test_matrixes_multiply()