"""
-------------------------------------------------------
Stack Functions.
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
Section: CP164 B
__updated__ = "2025-01-26"
-------------------------------------------------------
"""
from Stack_array import Stack

# Constants
OPERATORS = "+-*/"

def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    alternate = True

    while not source.is_empty():
        if alternate:
            target1.push(source.pop())
        else:
            target2.push(source.pop())
        alternate = not alternate

    return target1, target2

def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    temp_stack = Stack()
    temp_stack2 = Stack()
    
    # Move all elements to first temporary stack (reverses order)
    while not source.is_empty():
        temp_stack.push(source.pop())
        
    # Move all elements to second temporary stack (reverses order again)
    while not temp_stack.is_empty():
        temp_stack2.push(temp_stack.pop())
        
    # Move all elements back to source (reverses order final time)
    while not temp_stack2.is_empty():
        source.push(temp_stack2.pop())
    return

def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    stack = Stack()
    # Clean the string - keep only letters and convert to lowercase
    cleaned = ''.join(c.lower() for c in string if c.isalpha())
    
    # Push first half of characters onto stack
    mid = len(cleaned) // 2
    for i in range(mid):
        stack.push(cleaned[i])
        
    # Skip middle character if string length is odd
    start = mid + 1 if len(cleaned) % 2 == 1 else mid
    
    # Compare second half with stack
    for i in range(start, len(cleaned)):
        if stack.is_empty() or stack.pop() != cleaned[i]:
            return False
            
    return stack.is_empty()  # Should be empty if palindrome

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()
    tokens = string.split()
    
    for token in tokens:
        if token in OPERATORS:
            # Pop operands in reverse order
            b = float(stack.pop())
            a = float(stack.pop())
            
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)
        else:
            # Token is a number
            stack.push(float(token))
            
    return stack.pop()

def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    stack = Stack()
    values_out = []
    values_in_pos = 0
    
    try:
        for op in opstring:
            if op == 'S':
                if values_in_pos >= len(values_in):
                    return None  # Invalid: trying to push when input is empty
                stack.push(values_in[values_in_pos])
                values_in_pos += 1
            elif op == 'X':
                if stack.is_empty():
                    return None  # Invalid: trying to pop from empty stack
                values_out.append(stack.pop())
                
        # Check if all input values were used and stack is empty
        if values_in_pos != len(values_in) or not stack.is_empty():
            return None
            
        return values_out
        
    except:
        return None

