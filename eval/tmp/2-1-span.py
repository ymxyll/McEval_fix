

from typing import List
 
 
def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize variables to store current group and stack to track parentheses
    current_group = ""
    stack = []
    result = []
    
    # Iterate over each character in the input string
    for char in paren_string:
        if char == '(':
            # If it's an open parenthesis, push it to the stack
            stack.append(char)
            current_group += char
        elif char == ')':
            # If it's a close parenthesis, pop from the stack
            if stack:
                stack.pop()
            current_group += char
            # If the stack is empty, it means we've found a complete group
            if not stack:
                result.append(current_group)
                current_group = ""  # Reset current group for the next one

    return result
def check(separate_paren_groups):
    assert separate_paren_groups('(()()) ((())) () ((())()())') == [
    '(()())', '((()))', '()', '((())()())'
    ]
    assert separate_paren_groups('() (()) ((())) (((())))') == [
    '()', '(())', '((()))', '(((())))'
    ]
    assert separate_paren_groups('(()(())((())))') == [
    '(()(())((())))'
    ]
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
 
check(separate_paren_groups)