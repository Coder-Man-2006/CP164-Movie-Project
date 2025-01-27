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

from Movie_utilities import read_movies

with open("movies.txt", "r") as fv:
    movies = read_movies(fv)
for movie in movies:
    print(movie)
