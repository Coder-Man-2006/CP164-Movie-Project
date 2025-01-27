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

from functions import matrix_transpose

def test_matrix_transpose():
    matrix = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
    transposed = matrix_transpose(matrix)
    print(f"Transposed: {transposed}")  # Expected: [[0, 2, 4, 6, 8], [1, 3, 5, 7, 9]]

test_matrix_transpose()