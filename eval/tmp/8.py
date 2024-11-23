

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
    # Create a 2D grid with the given values
    grid = [[0]*N for _ in range(N)]
    for x, y, value in grid_values:
        if x == 0 and y == 0:
            grid[0][0] = value
        else:
            grid[x-1][y-1] = value

    # Initialize a 2D array to store the maximum sum of values that can be collected
    # from the top-left corner to the current cell
    dp = [[-1]*N for _ in range(N)]

    # Function to calculate the maximum sum of values that can be collected
    # from the top-left corner to the current cell
    def max_sum(x: int, y: int) -> int:
        if x == 0 and y == 0:
            return grid[0][0]
        if dp[x][y] != -1:
            return dp[x][y]
        if x > 0:
            dp[x][y] = max(dp[x][y], max_sum(x-1, y) + grid[x][y])
        if y > 0:
            dp[x][y] = max(dp[x][y], max_sum(x, y-1) + grid[x][y])
        return dp[x][y]

    # Calculate the maximum sum of values that can be collected from the top-left
    # corner to the bottom-right corner of the grid
    return max_sum(N-1, N-1)
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