

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
    >>> count_passing_ways(3, 3)
    2
    >>> count_passing_ways(5, 4)
    6
    """
    # Initialize a 2D list to store the number of ways to pass the ball
    # from each student to each position.
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Initialize the base case: if there is only one student, there is only one way to pass the ball.
    for i in range(n):
        dp[i][i] = 1

    # Fill in the dp table.
    for k in range(2, m+1):  # k is the number of passes
        for i in range(n):
            # Calculate the number of ways to pass the ball from each student.
            # The ball can be passed to the left or right neighbor.
            dp[i][(i-1+n)%n] += dp[(i-1+n)%n][(i-k+1+n)%n]
            dp[i][(i+1)%n] += dp[i][(i-k+n)%n]

    # The number of ways to pass the ball from the first student after 'm' passes is the answer.
    return dp[0][(0+m-1)%n]
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