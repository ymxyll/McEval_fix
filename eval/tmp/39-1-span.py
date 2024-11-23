

def calculate_arrangements(n, m, a) -> int:
    """
    Compute the number of ways to arrange m pots of flowers using up to n types,
    where the ith type can have at most a[i] pots, and the arrangement must be in
    increasing order of flower types.

    Args:
    - n (int): The number of flower types available.
    - m (int): The total number of flower pots to arrange.
    - a (list of int): A list where a[i] is the maximum number of pots for the ith type of flower.

    Returns:
    - int: The number of distinct arrangements modulo (10^6 + 7).

    Examples:
    - calculate_arrangements(2, 4, [3, 2]) returns 2.
      There are two possible arrangements for 4 pots using two types of flowers with
      at most 3 of the first type and 2 of the second type: [1, 1, 2, 2] and [1, 2, 2, 2].

    - calculate_arrangements(3, 3, [1, 2, 3]) returns 6.
      There are six ways to arrange 3 pots using three types of flowers when the
      maximum pots are 1, 2, and 3 for the first, second, and third types respectively.
    """
    MOD = 10 ** 6 + 7

    # Initialize the dp array
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case

    # Fill the dp array
    for i in range(1, n + 1):
        for j in range(m + 1):
            # Calculate the number of ways for each state
            for k in range(min(j, a[i - 1]) + 1):
                dp[i][j] += dp[i - 1][j - k]

    # Return the result
    return dp[n][m] % MOD
def test_calculate_arrangements():
    # Helper function to compare expected and actual results
    def assert_equal(actual, expected, message):
        assert actual == expected, message

    # Test Case 1
    n, m, a = 2, 4, [3, 2]
    expected = 2
    assert_equal(calculate_arrangements(n, m, a), expected, f"Test Case 1 failed: expected {expected}, got {calculate_arrangements(n, m, a)}")

    # Test Case 2
    n, m, a = 3, 3, [1, 2, 3]
    expected = 6
    assert_equal(calculate_arrangements(n, m, a), expected, f"Test Case 2 failed: expected {expected}, got {calculate_arrangements(n, m, a)}")

    # Test Case 3
    n, m, a = 1, 5, [5]
    expected = 1
    assert_equal(calculate_arrangements(n, m, a), expected, f"Test Case 3 failed: expected {expected}, got {calculate_arrangements(n, m, a)}")

    print("All tests passed!")

if __name__ == "__main__":
    test_calculate_arrangements()