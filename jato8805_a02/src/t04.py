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

from Movie_utilities import get_by_genres
from Movie import Movie

# Sample movies for testing
movies = [
    Movie("Movie A", 2021, "Director A", 8.0, [1, 2]),
    Movie("Movie B", 2020, "Director B", 7.5, [3]),
    Movie("Movie C", 2021, "Director C", 9.0, [1, 4]),
]

# Test for genre codes [1, 4]
test_genres = [1, 4]
result = get_by_genres(movies, test_genres)

print(f"Movies with genres {test_genres}:")
for movie in result:
    print(movie)
