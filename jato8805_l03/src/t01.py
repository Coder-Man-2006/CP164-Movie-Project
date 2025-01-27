"""
-------------------------------------------------------
Lab 3, Testing
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
Section: CP164 B
__updated__ = "2025-01-26"
-------------------------------------------------------
"""
from Movie import Movie
from utilities import queue_test, priority_queue_test

# Test Queue with integers
source = [5, 8, 12, 3]
print("Testing Queue with integers:")
print("-" * 40)
queue_test(source)

# Test Queue with Movie objects
movies = [
    Movie("Dellamorte Dellamore", 1994, "Michele Soavi", 7.2, [3, 4, 5, 8]),
    Movie("Dark City", 1998, "Alex Proyas", 7.8, [0, 1, 4]),
    Movie("Zulu", 1964, "Cy Endfield", 7.8, [7])
]

print("\nTesting Queue with Movie objects:")
print("-" * 40)
queue_test(movies)

print("\nTesting Priority Queue with integers:")
print("-" * 40)
priority_queue_test(source)

print("\nTesting Priority Queue with Movie objects:")
print("-" * 40)
priority_queue_test(movies) 