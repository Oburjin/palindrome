from __future__ import annotations
""" palindrome.py
    
Defines a function to check if a string is a palindrome

Unless otherwise stated and not an abstract method, best case and worst case complexity is O(1)
If only one complexity is stated, than worst and best case time complexity are the same.
"""
from data_structures.stack_adt import ArrayStack


def check_palindrome(input_str: str) -> bool:
    """ Checks if input string is a palindrome
    
    :Input:
        input_str (str): The string to check
    
    :Returns:
        bool: True if the input string is a palindrome, False otherwise
    
    :Complexity: O(n) where n is the length of the input string
    """

    # array = ArrayStack(len(input_str)//2+1)
    # for i in range(len(input_str)//2+1):
    #     array.push(input_str[i])
    # for i in range(len(array.length)):
    #     if array.pop == array.

    # array = ArrayStack(len(input_str))
    # for i in range(len(input_str)):
    #     array.length += 1
    #     array.push(input_str[i])
    # for i in range(len(array.length)):
    #     temp = array.pop()
    #     array.length -= 1
    #     if temp == array.peek():
    #         for i in range(len(array.length)):
    
    # array = ArrayStack()
    # for i in range(len(input_str)):
    #     array.length += 1
    #     array.push(input_str[i])
    # back_array = ArrayStack()
    # for i in range(len(array.length)):
    #     back_array.length += 1
    #     back_array.push(array.pop)
    #     array.length -= 1
    #     if back_array.peek() != array.pop():
    #         return False
    # return True

    # LESS OPTIMISED
    # array = ArrayStack()
    # for i in range(len(input_str)):
    #     array.length += 1
    #     array.push(input_str[i])
    #     if array.peek() != input_str[i]:
    #         return False
    # return True

    # # MORE OPTIMISED
    # array = ArrayStack(len(input_str))
    # for i in range(len(input_str)):
    #     array.length += 1
    #     array.push(input_str[i])
    # for i in range(len(input_str//2)):
    #     if array.peek() != input_str[i]:
    #         return False
    # return True

    # MORE OPTIMISED
    array = ArrayStack(len(input_str))
    for i in range(len(input_str)):
        array.push(input_str[i])
    for i in range(len(input_str)//2):
        if array.peek() != input_str[i]:
            return False
    return True