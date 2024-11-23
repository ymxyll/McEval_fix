

def count_partitions(n: int, k: int, x: int) -> int:
    """
    Count the number of ways to partition an integer n into k parts,
    where each part is at least x and order of parts does not matter.

    Parameters:
    n (int): The integer to be partitioned.
    k (int): The number of parts to divide n into.
    x (int): The minimum value for each part.

    Returns:
    int: The number of distinct partitioning ways.

    Examples:
    - count_partitions(7, 3, 1) will return 4, because there are four ways to partition 
      the number 7 into 3 parts with each part being at least 1: [1,1,5], [1,2,4], 
      [1,3,3], [2,2,3].
    - count_partitions(6, 2, 1) will return 3, because there are three ways to partition 
      the number 6 into 2 parts with each part being at least 1: [1,5], [2,4], [3,3].
    """
    # Initialize the dp array
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    # There is only one way to partition 0 into any number of parts
    for i in range(n+1):
        dp[i][0] = 1

    # There are no ways to partition a positive number into 0 parts
    for i in range(1, n+1):
        dp[i][1] = 1

    # Fill the dp array
    for i in range(x, n+1):
        for j in range(2, k+1):
            # If the current part is at least x, we can use it or not use it
            dp[i][j] = dp[i-1][j] + dp[i-x][j-1]

    return dp[n][k]
def test_count_partitions():
    # Test case 1: Simple case
    result = count_partitions(7, 3, 1)
    assert result == 4, f"Expected 4, got {result}"

    # Test case 2: Another simple case
    result = count_partitions(6, 2, 1)
    assert result == 3, f"Expected 3, got {result}"

    # Test case 3: Partitioning into a larger number of parts
    result = count_partitions(8, 4, 1)
    assert result == 5, f"Expected 5, got {result}"

    print("All test cases passed successfully!")


# Call the test function to run the test cases
test_count_partitions()