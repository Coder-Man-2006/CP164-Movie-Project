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

from Movie_utilities import get_by_rating
from Movie import Movie

# Sample movies for testing
movies = [
    Movie("Movie A", 2021, "Director A", 8.0, [1, 2]),
    Movie("Movie B", 2020, "Director B", 7.5, [3]),
    Movie("Movie C", 2021, "Director C", 9.0, [1, 4]),
]

# Test for rating >= 8.0
min_rating = 8.0
result = get_by_rating(movies, min_rating)

print(f"Movies with rating >= {min_rating}:")
for movie in result:
    print(movie)
