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

from functions import matrix_flatten

def test_matrix_flatten():
    matrix = [['a', 'b'], ['x', 'z'], ['e', 'f']]
    flattened = matrix_flatten(matrix)
    print(f"Flattened: {flattened}")  # Expected: ['a', 'b', 'x', 'z', 'e', 'f']

test_matrix_flatten()