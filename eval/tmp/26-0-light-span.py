

from math import gcd
def count_coprime_pairs(x0: int, y0: int) -> int:
    """
    Counts the number of pairs of positive integers (P, Q) such that P and Q have x0 as their greatest common divisor (GCD)
    and y0 as their least common multiple (LCM).

    Args:
    x0 (int): The GCD that each pair (P, Q) must have.
    y0 (int): The LCM that each pair (P, Q) must have.

    Returns:
    int: The count of all possible pairs (P, Q) that meet the specified criteria.

    The function iterates through all possible factors 'a' of the quotient 'y0 / x0'. For each factor 'a',
    it calculates the corresponding factor 'b' such that 'a * b = y0 / x0'. It then checks if 'a' and 'b'
    are co-prime (their GCD is 1) because P and Q can only be multiples of 'x0' by co-prime factors to maintain
    the GCD as 'x0'. If 'a' and 'b' are co-prime, the count is incremented by 1 if 'a' is the same as 'b',
    else by 2 to account for both (P, Q) and (Q, P) pairs.

    Example Cases:

    Case 1: count_coprime_pairs(3, 60)
    Explanation: The function would return 4, since the valid pairs are (3, 60), (15, 12), (12, 15), and (60, 3).

    Case 2: count_coprime_pairs(2, 50)
    Explanation: The function would return 0, as 50 is not a multiple of 2, so there are no valid pairs (P, Q).

    Case 3: count_coprime_pairs(6, 180)
    Explanation: The function would return 8, the valid pairs are (6, 180), (30, 36), (18, 60), (42, 30),
    (60, 18), (36, 30), (180, 6), and the counts for other arrangements of these numbers.

    Note:
    For the function to work correctly, the input y0 must be a multiple of x0. If not, the function returns 0, 
    indicating no valid pairs exist under the given constraints.
    """
    if y0 % x0 != 0:
        return 0  # If y0 is not a multiple of x0, there are no valid pairs.

    product = y0 // x0
    count = 0
    
    # Iterate through all factors of product.
    for a in range(1, int(product**0.5) + 1):
        if product % a == 0:
            b = product // a
            if gcd(a, b) == 1:  # Check if a and b are co-prime
                count += 1 if a == b else 2  # If a and b are different, we have two pairs (P, Q) and (Q, P).
    
    return count

# Helper function to calculate gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def test_count_coprime_pairs():
    test_cases = [
        (3, 60, 4),   # The example from the problem statement
        (2, 50, 2), 
        (6, 180, 8),  # 180/6 = 30, factors are (1, 30), (2, 15), (3, 10), (5, 6), (6, 5), (10, 3), (15, 2), (30, 1)
    ]

    for i, (x0, y0, expected) in enumerate(test_cases):
        result = count_coprime_pairs(x0, y0)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed: x0 = {x0}, y0 = {y0}, expected = {expected}, got = {result}")

# Call the test function
test_count_coprime_pairs()