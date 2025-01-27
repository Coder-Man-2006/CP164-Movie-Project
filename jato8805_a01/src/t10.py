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

from functions import matrix_rotate_right

def test_matrix_rotate_right():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    rotated = matrix_rotate_right(matrix)
    print(f"Rotated matrix: {rotated}")  
    # Expected: [[10, 7, 4, 1], [11, 8, 5, 2], [12, 9, 6, 3]]

test_matrix_rotate_right()