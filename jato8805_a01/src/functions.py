"""
-------------------------------------------------------
Movie class definition.
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
Section: CP164 B
__updated__ = "2025-01-10"
-------------------------------------------------------
"""

# Author: Your Name
# ID: Your Student ID
# Email: Your Laurier Email Address

def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    seen = set()
    i = 0
    while i < len(values):
        if values[i] in seen:
            values.pop(i)
        else:
            seen.add(values[i])
            i += 1

def list_subtraction(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    Use: list_subtraction(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    minuend[:] = [value for value in minuend if value not in subtrahend]

def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    Use: upp, low, dig, whi, rem = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        upp - the number of uppercase letters in the file (int)
        low - the number of lowercase letters in the file (int)
        dig - the number of digits in the file (int)
        whi - the number of whitespace characters in the file (int)
        rem - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    upp, low, dig, whi, rem = 0, 0, 0, 0, 0
    for line in fv:
        for char in line:
            if char.isupper():
                upp += 1
            elif char.islower():
                low += 1
            elif char.isdigit():
                dig += 1
            elif char.isspace():
                whi += 1
            else:
                rem += 1
    return upp, low, dig, whi, rem

def find_subs(string, sub):
    """
    -------------------------------------------------------
    Finds the indices of the locations of sub within string.
    Use: locations = find_subs(string, sub)
    -------------------------------------------------------
    Parameters:
        string - a string to evaluate (str)
        sub - a substring to locate in string (str)
    Returns:
        locations - an ordered list of the indices of the locations
            of sub within string (list of int)
    -------------------------------------------------------
    """
    locations = []
    index = 0
    while index < len(string):
        match = string.find(sub, index)
        if match == -1:
            break
        locations.append(match)
        index = match + len(sub)  # Move past the current match
    return locations

def is_palindrome(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome.
    Use: palindrome = is_palindrome(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    import string as s
    filtered = ''.join(filter(lambda c: c.isalnum(), string)).lower()
    return filtered == filtered[::-1]

def median_scores(fv):
    """
    -------------------------------------------------------
    Determines the median of a series of integers in a file.
    Use: median = median_scores(fv)
    -------------------------------------------------------
    Parameters:
        fv - a file variable for an already open file of integers (file)
    Returns:
        median - the median of the values in the file (float)
    -------------------------------------------------------
    """
    numbers = sorted([int(line.strip()) for line in fv])
    mid = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    return numbers[mid]

def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    return [list(row) for row in zip(*a)]

def matrix_flatten(a):
    """
    -------------------------------------------------------
    Flatten the contents of 2D list a.
    Use: b = matrix_flatten(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of ?)
    Returns:
        b - the flattened version of a (list of ?)
    -------------------------------------------------------
    """
    return [item for sublist in a for item in sublist]

def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrices a and b.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]

def matrix_rotate_right(a):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    Use: b = matrix_rotate_right(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of values (2D list of int/float)
    Returns:
        b - the rotated 2D list of values (2D list of int/float)
    -------------------------------------------------------
    """
    return [list(row) for row in zip(*a[::-1])]
