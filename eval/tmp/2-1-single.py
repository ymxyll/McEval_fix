

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
        # If it's an opening parenthesis, push to stack and add to current group
        if char == "(":
            stack.append(char)
            current_group += char
        # If it's a closing parenthesis, pop from stack and add to current group
        elif char == ")" and stack:
            stack.pop()
            current_group += char
            # If stack is empty, it means we have a complete group
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