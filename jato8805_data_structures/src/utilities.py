"""
-------------------------------------------------------
Utilities
-------------------------------------------------------
Author:  Joseph Jatou
ID:      169088805
Email:   jato8805@mylaurier.ca
Section: CP164 B
__updated__ = "2025-01-26"
-------------------------------------------------------
"""
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue

# Stack Utilities
def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        stack.push(source.pop())
    return

def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not stack.is_empty():
        target.insert(0, stack.pop())
    return

def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    stack = Stack()
    
    # Test empty stack
    print("Testing empty stack:")
    print(f"is_empty(): {stack.is_empty()}")
    
    try:
        stack.peek()
    except AssertionError as e:
        print(f"peek() error: {str(e)}")
        
    try:
        stack.pop()
    except AssertionError as e:
        print(f"pop() error: {str(e)}")
    
    # Test with data
    print("\nPushing data...")
    for value in source:
        print(f"push: {value}")
        stack.push(value)
    
    print(f"\nis_empty(): {stack.is_empty()}")
    
    if not stack.is_empty():
        print(f"peek: {stack.peek()}")
        
    print("\nPopping data:")
    while not stack.is_empty():
        print(f"pop: {stack.pop()}")
        
    print(f"\nis_empty(): {stack.is_empty()}")
    return

# Queue Utilities
def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        queue.insert(source.pop(0))
    return

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        target.append(queue.remove())
    return

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()
    
    # Test empty queue
    print("Testing empty queue:")
    print(f"is_empty(): {q.is_empty()}")
    print(f"len: {len(q)}")
    
    try:
        q.peek()
    except AssertionError as e:
        print(f"peek() error: {str(e)}")
        
    try:
        q.remove()
    except AssertionError as e:
        print(f"remove() error: {str(e)}")
    
    # Test with data
    print("\nInserting data...")
    for value in a:
        print(f"insert: {value}")
        q.insert(value)
    
    print(f"\nis_empty(): {q.is_empty()}")
    print(f"len: {len(q)}")
    
    if not q.is_empty():
        print(f"peek: {q.peek()}")
        
    print("\nRemoving data:")
    while not q.is_empty():
        print(f"remove: {q.remove()}")
        
    print(f"\nis_empty(): {q.is_empty()}")
    print(f"len: {len(q)}")
    return

# Priority Queue Utilities
def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        pq.insert(source.pop(0))
    return

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        target.append(pq.remove())
    return

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    
    # Test empty priority queue
    print("Testing empty priority queue:")
    print(f"is_empty(): {pq.is_empty()}")
    
    try:
        pq.peek()
    except AssertionError as e:
        print(f"peek() error: {str(e)}")
        
    try:
        pq.remove()
    except AssertionError as e:
        print(f"remove() error: {str(e)}")
    
    # Test with data
    print("\nInserting data...")
    for value in a:
        print(f"insert: {value}")
        pq.insert(value)
    
    print(f"\nis_empty(): {pq.is_empty()}")
    
    if not pq.is_empty():
        print(f"peek: {pq.peek()}")
        
    print("\nRemoving data:")
    while not pq.is_empty():
        print(f"remove: {pq.remove()}")
        
    print(f"\nis_empty(): {pq.is_empty()}")
    return 