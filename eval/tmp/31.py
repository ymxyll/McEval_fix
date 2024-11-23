

from collections import deque
def generate_numbers(n, rules) -> int:
    """
    Generate all unique numbers from the given number by applying transformation rules.

    Each rule allows a single digit to be transformed into another. A breadth-first search
    (BFS) is used to explore all possible transformations. The function returns the count
    of unique numbers that can be generated from the original number, including the number itself.

    Args:
    - n (int): The original integer number to transform.
    - rules (list of tuples): A list of transformation rules, where each rule is represented
                              as a tuple (x, y) indicating that digit x can be transformed into y.

    Returns:
    - int: The total count of unique numbers that can be generated.

    Cases:
    >>> generate_numbers(234, [(2, 5), (3, 6)])
    4
    >>> generate_numbers(100, [(1, 9)])
    2
    """
    # Convert the number to a list of digits
    digits = list(str(n))
    # Create a set to store the unique numbers
    unique_numbers = set()
    # Create a queue for BFS
    queue = deque([digits])
    # Perform BFS
    while queue:
        current_digits = queue.popleft()
        # Convert the current digits back to a number
        current_number = int(''.join(current_digits))
        # Add the current number to the set of unique numbers
        unique_numbers.add(current_number)
        # Generate all possible next numbers by applying the transformation rules
        for i in range(len(current_digits)):
            for rule in rules:
                if current_digits[i] == str(rule[0]):
                    # Create a copy of the current digits
                    next_digits = current_digits[:]
                    # Apply the transformation rule
                    next_digits[i] = str(rule[1])
                    # Add the next digits to the queue
                    queue.append(next_digits)
    # Return the count of unique numbers
    return len(unique_numbers)
def test_generate_numbers():
    # Test case 1
    n1, k1 = 234, 2
    rules1 = [(2, 5), (3, 6)]
    assert generate_numbers(n1, rules1) == 4, "Test case 1 failed"

    # Test case 2
    n2, k2 = 123, 3
    rules2 = [(1, 9), (2, 8), (3, 7)]
    assert generate_numbers(n2, rules2) == 8, "Test case 2 failed"

    # Test case 3
    n3, k3 = 999, 1
    rules3 = [(9, 1)]
    assert generate_numbers(n3, rules3) == 8, "Test case 3 failed"

    print("All test cases passed!")

# Call the test function
test_generate_numbers()