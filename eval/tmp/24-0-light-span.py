

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
    if k == 1:
        return 1 if n >= x else 0
    count = 0
    for i in range(x, n // k + 1):
        count += count_partitions(n - i, k - 1, i)
    return count
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