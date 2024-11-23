

from collections import deque
from typing import Union

def string_transformation(A: str, B: str, rules: list) -> Union[int, str]:
    """
    Perform string transformation from A to B using a set of transformation rules.

    This function takes an initial string A and a target string B, along with a list
    of transformation rules, and attempts to transform A into B using the rules.
    A Breadth-First Search (BFS) algorithm is used to explore the possible transformations
    up to a maximum of 10 steps. If A can be transformed into B within 10 steps, the function
    returns the minimum number of steps required. If it's not possible, the function returns
    "NO ANSWER!".

    Parameters:
    A (str): The initial string to be transformed.
    B (str): The target string to be achieved.
    rules (list of tuples): A list of transformation rules, where each rule is a tuple
                            containing the source substring (to be replaced) and the
                            target substring (to replace with).

    Returns:
    Union[int, str]: The minimum number of transformation steps if possible, otherwise "NO ANSWER!".

    Examples:
    Case 1:
    A = "abcd", B = "xyz", rules = [("abc", "xu"), ("ud", "y"), ("y", "yz")]
    string_transformation(A, B, rules) should return 3.

    Case 2:
    A = "aaa", B = "bbbb", rules = [("a", "b"), ("aa", "bb"), ("aaa", "bbb")]
    string_transformation(A, B, rules) should return "NO ANSWER!" because transformation
    is not possible within 10 steps.

    Case 3:
    A = "abc", B = "xyz", rules = [("a", "x"), ("b", "y"), ("c", "z")]
    string_transformation(A, B, rules) should return 3, as each character is replaced
    individually.
    """

    queue = deque([(A, 0)])  # Each element in the queue is a tuple (current_string, steps_taken)
    visited = set([A])  # Keep track of visited strings to avoid loops

    # Perform BFS
    while queue:
        current, steps = queue.popleft()
        if current == B:
            return steps  # Found the target string
        if steps == 10:
            continue  # Stop if already taken 10 steps
        for source, target in rules:
            index = current.find(source)
            while index != -1:
                next_string = current[:index] + target + current[index + len(source):]
                if next_string not in visited:
                    queue.append((next_string, steps + 1))
                    visited.add(next_string)
                index = current.find(source, index + 1)
    return "NO ANSWER!"
def test_string_transformation():
    # Test case 1
    A1 = "abcd"
    B1 = "xyz"
    rules1 = [("abc", "xu"), ("ud", "y"), ("y", "yz")]
    expected_result1 = 3
    assert string_transformation(A1, B1, rules1) == expected_result1, "Test case 1 failed"

    # Test case 2
    A2 = "aaa"
    B2 = "bbbb"
    rules2 = [("a", "b"), ("aa", "bb"), ("aaa", "bbb")]
    expected_result2 = "NO ANSWER!"
    assert string_transformation(A2, B2, rules2) == expected_result2, "Test case 2 failed"

    # Test case 3
    A3 = "hello"
    B3 = "world"
    rules3 = [("h", "w"), ("e", "o"), ("l", "r"), ("lol", "ldr")]
    expected_result3 = "NO ANSWER!"
    assert string_transformation(A3, B3, rules3) == expected_result3, "Test case 3 failed"

    print("All test cases passed!")

# Run the test function
test_string_transformation()