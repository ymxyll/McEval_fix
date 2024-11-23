

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
    - Case 1: n = 234, rules = [(2, 5), (3, 6)]
              This case should return 4 because the following unique numbers can be generated:
              234 (original), 534 (2 -> 5), 264 (3 -> 6), and 564 (2 -> 5, 3 -> 6).

    - Case 2: n = 100, rules = [(1, 9)]
              This case should return 2 because the following unique numbers can be generated:
              100 (original) and 900 (1 -> 9).

    - Case 3: n = 8, rules = [(8, 3), (8, 5)]
              This case should return 3 because the following unique numbers can be generated:
              8 (original), 3 (8 -> 3), and 5 (8 -> 5).
    """
    # Convert the input number n to a string for easier manipulation
    str_n = str(n)
    # Create a set to store all unique numbers generated
    unique_numbers = {str_n}
    # Use a queue to perform BFS on all possible transformations
    queue = deque([str_n])
    
    while queue:
        current = queue.popleft()
        # Loop through each digit in the current number
        for i in range(len(current)):
            # Apply each rule to the digit if applicable
            for x, y in rules:
                if current[i] == str(x):
                    new_number = current[:i] + str(y) + current[i+1:]
                    if new_number not in unique_numbers:
                        unique_numbers.add(new_number)
                        queue.append(new_number)
    
    # Return the count of unique numbers generated
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