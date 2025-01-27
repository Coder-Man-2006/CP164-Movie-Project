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

from Movie import Movie

print(Movie.genres_menu())
m1 = Movie("T1", 2000, "D1", 5, [0])
print(m1.genres_list_string())

