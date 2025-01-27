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

from Movie_utilities import read_movie

line = "Dellamorte Dellamore|1994|Michele Soavi|7.2|3,4,5,8"
movie = read_movie(line)
print(movie)