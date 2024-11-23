

def count_passing_ways(n: int, m: int) -> int:
    """
    Counts the number of different ways to pass a ball among 'n' students arranged in a circle 
    such that after 'm' passes, the ball returns to the starting student.

    The function uses dynamic programming to determine the number of passing sequences. Each student
    can pass the ball either to the left neighbor or to the right neighbor.

    Args:
    n: The number of students standing in a circle.
    m: The number of times the ball is passed.

    Returns:
    An integer representing the number of distinct passing ways that result in the ball
    returning to the starting student after 'm' passes.

    Cases:
    Case 1:
    For n = 3 students and m = 3 passes, the function should return 2.
    There are two sequences: 1 -> 2 -> 3 -> 1 and 1 -> 3 -> 2 -> 1.

    Case 2:
    For n = 4 students and m = 2 passes, the function should return 2.
    There are two sequences: 1 -> 2 -> 1 and 1 -> 4 -> 1.

    Case 3:
    For n = 5 students and m = 4 passes, the function should return 6.
    The sequences include: 1 -> 2 -> 3 -> 4 -> 1, 1 -> 2 -> 1 -> 2 -> 1, 
    1 -> 4 -> 3 -> 2 -> 1, 1 -> 4 -> 5 -> 4 -> 1, 1 -> 2 -> 3 -> 2 -> 1,
    and 1 -> 4 -> 5 -> 2 -> 1.
    """
    # The code implementation would go here.
    # Initialize the DP table
    dp = [[0] * n for _ in range(m + 1)]

    # Base case
    dp[0][0] = 1

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(n):
            # Calculate the number of ways to pass the ball to j-th student
            dp[i][j] = dp[i - 1][(j - 1) % n] + dp[i - 1][(j + 1) % n]

    # Return the result
    return dp[m][0]
def test_count_passing_ways():
    test_cases = [
        # Test case 1: simple case
        {
            'n': 3,
            'm': 1,
            'expected': 0
        },
        # Test case 2: another simple case
        {
            'n': 4,
            'm': 2,
            'expected': 2
        },
        # Test case 3: larger number of students and passes
        {
            'n': 5,
            'm': 3,
            'expected': 0
        },
    ]

    for i, test in enumerate(test_cases, 1):
        result = count_passing_ways(test['n'], test['m'])
        assert result == test['expected'], f"Test case {i} failed: result {result} does not match expected {test['expected']}"
        print(f"Test case {i} passed with result {result}.")

# Run the test function
test_count_passing_ways()