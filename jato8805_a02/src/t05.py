"""
-------------------------------------------------------
Movie class definition.
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
Section: CP164 B
__updated__ = "2025-01-18"
-------------------------------------------------------
"""

from Movie_utilities import genre_counts
from Movie import Movie

# Sample movies for testing
movies = [
    Movie("Movie A", 2021, "Director A", 8.0, [1, 2]),
    Movie("Movie B", 2020, "Director B", 7.5, [3]),
    Movie("Movie C", 2021, "Director C", 9.0, [1, 4]),
]

# Count genres
result = genre_counts(movies)

print("Genre counts:")
for index, count in enumerate(result):
    print(f"Genre {index}: {count} movie(s)")
