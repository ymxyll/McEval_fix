

from typing import List, Tuple

def max_value_on_paths(N: int, grid_values: List[Tuple[int, int, int]]) -> int:
    """
    Calculate the maximum sum of values collected on two paths in an N x N grid.

    This function utilizes dynamic programming to find two paths from the top-left corner to
    the bottom-right corner of the grid which maximize the sum of the values collected. Each
    value can be collected at most once, even if both paths pass through it.

    Args:
    - N (int): The size of the grid (N x N).
    - grid_values (List[Tuple[int, int, int]]): A list of tuples where each tuple contains
      the x-coordinate, y-coordinate, and value to be placed on the grid at that position.
      The list is terminated by a tuple with all zeros.

    Returns:
    - int: The maximum sum of values collected on the two paths.

    Examples:
    >>> max_value_on_paths(2, [(1, 2, 1), (2, 1, 2), (0, 0, 0)])
    3
    >>> max_value_on_paths(8, [
    ...     (2, 3, 13), (2, 6, 6), (3, 5, 7), (4, 4, 14),
    ...     (5, 2, 21), (5, 6, 4), (6, 3, 15), (7, 2, 14),
    ...     (0, 0, 0)])
    67
    """
    # Initialize a 4-dimensional DP array
    # dp[x1][y1][x2][y2] will store the max sum until reaching points (x1, y1) and (x2, y2) on both paths
    dp = [[[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
    
    # Fill in the grid with input values
    grid = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for x, y, val in grid_values:
        if x == 0 and y == 0:
            break
        grid[x][y] = val
    
    # Dynamic programming to calculate maximum values
    # Both persons start at (1,1) and end at (N,N)
    for x1 in range(1, N+1):
        for y1 in range(1, N+1):
            for x2 in range(1, N+1):
                for y2 in range(1, N+1):
                    # The maximum value for the current cell is the maximum of the values from
                    # the previous step plus the value in the current cell(s)
                    dp[x1][y1][x2][y2] = max(
                        dp[x1-1][y1][x2-1][y2],
                        dp[x1-1][y1][x2][y2-1],
                        dp[x1][y1-1][x2-1][y2],
                        dp[x1][y1-1][x2][y2-1]
                    ) + grid[x1][y1] + (grid[x2][y2] if (x1, y1) != (x2, y2) else 0)
    
    # The answer is in the cell dp[N][N][N][N]
    return dp[N][N][N][N]
def test_max_value_on_paths():
    # Test case 1: Small grid with clear path
    assert max_value_on_paths(2, [(1, 2, 1), (2, 1, 2), (0, 0, 0)]) == 3
    
    # Test case 2: Example provided in the problem statement
    assert max_value_on_paths(8, [
        (2, 3, 13), (2, 6, 6), (3, 5, 7), (4, 4, 14),
        (5, 2, 21), (5, 6, 4), (6, 3, 15), (7, 2, 14),
        (0, 0, 0)]) == 67

    print("All test cases passed!")

# Run the test cases
test_max_value_on_paths()