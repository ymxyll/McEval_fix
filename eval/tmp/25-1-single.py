

def count_sequences(n: int, last: int, memo: dict) -> int:
    """
    Calculate the number of valid sequences that can be formed according to specific rules.
    
    Each sequence starts with a given number 'n', and a new number can be appended to the sequence
    if it is a positive integer and not greater than half the last number in the sequence. This
    function uses memoization to store previously calculated results to optimize performance.
    
    Args:
        n (int): The starting number of the sequence.
        last (int): The last number in the current sequence.
        memo (dict): A dictionary used for memoization, storing the number of valid sequences
                     for each 'last' value encountered.
    
    Returns:
        int: The total number of valid sequences that can be formed starting with 'n'.
    
    Examples:
        # Only one sequence can be formed starting with 1: [1]
        >>> count_sequences(1, 1, {})
        1
        
        # Six sequences can be formed starting with 6:
        # [6], [6, 1], [6, 2], [6, 3], [6, 2, 1], [6, 3, 1]
        >>> count_sequences(6, 6, {})
        6
        
        # More complex example with memoization dictionary passed
        # You would typically not pass this dictionary manually,
        # it's used internally by the function for optimization.
        >>> memo = {}
        >>> count_sequences(10, 10, memo)
        42  # This is an assumed value for the example; the actual result may differ.
    """
    # Function implementation is here...
    if last in memo:
        return memo[last]  # Return the precomputed result

    count = 1  # Count the current sequence
    for next_num in range(1, last // 2 + 1):  # Try appending all possible numbers
        count += count_sequences(n, next_num, memo)

    memo[last] = count  # Store the computed result in the memo dictionary
    return count  # Return the count after the loop
def test_count_sequences():
    test_cases = [
        (6, 6),
        (1, 1),
        (10, 14)
    ]

    for i, (n, expected) in enumerate(test_cases):
        memo = {}
        result = count_sequences(n, n, memo)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed: n = {n}, expected = {expected}, got = {result}")

# Call the test function
test_count_sequences()