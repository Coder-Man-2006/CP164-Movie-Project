"""
-------------------------------------------------------
Lab 2, Testing
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
Section: CP164 B
__updated__ = "2025-01-26"
-------------------------------------------------------
"""
from Movie import Movie
from utilities import stack_test

# Test with integers
source = [5, 8, 12, 3]
print("Testing with integers:")
print("-" * 40)
stack_test(source)

# Test with Movie objects
movies = [
    Movie("Dellamorte Dellamore", 1994, "Michele Soavi", 7.2, [3, 4, 5, 8]),
    Movie("Dark City", 1998, "Alex Proyas", 7.8, [0, 1, 4]),
    Movie("Zulu", 1964, "Cy Endfield", 7.8, [7])
]

print("\nTesting with Movie objects:")
print("-" * 40)
stack_test(movies) 