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

from functions import is_palindrome

def test_is_palindrome():
    print(is_palindrome("Able was I ere I saw Elba!"))  # Expected: True
    print(is_palindrome("Palindrome"))  # Expected: False

test_is_palindrome()