

def find_min_n_greater_than_k(k: int) -> int:
    """
    Calculate the smallest positive integer n such that the sum of the harmonic series
    up to 1/n is greater than a given positive integer k.

    The harmonic series is defined as S_n = 1 + 1/2 + 1/3 + ... + 1/n.

    Args:
    - k (int): A positive integer representing the threshold value the harmonic series sum must exceed.

    Returns:
    - int: The smallest integer n for which the harmonic series sum S_n exceeds the threshold k.

    Examples:
    >>> find_min_n_greater_than_k(1)
    2
    The sum S_2 = 1 + 1/2 = 1.5, which is greater than 1.

    >>> find_min_n_greater_than_k(3)
    11
    The sum S_10 = 1 + 1/2 + 1/3 + ... + 1/10 is less than or equal to 3, but the sum S_11 exceeds 3.
    """
    # Initialize variables
    n = 1
    harmonic_sum = 0

    # Calculate the harmonic sum
    while harmonic_sum <= k:
        harmonic_sum += 1 / n
        n += 1

    # Return the smallest integer n for which the harmonic series sum exceeds the threshold k
    return n - 1
def test_find_min_n_greater_than_k():
    # Test case 1: k = 1, expected result is 2

    assert find_min_n_greater_than_k(1) == 2, "Test case 1 failed."

    # Test case 2: k = 3, expected result is 11
    assert find_min_n_greater_than_k(3) == 11, "Test case 2 failed."
    # Test case 3: k = 5, expected result is 83
    assert find_min_n_greater_than_k(5) == 83, "Test case 3 failed."

    print("All test cases passed.")


# Run the test function
test_find_min_n_greater_than_k()