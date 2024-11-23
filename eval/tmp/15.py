

def optimize_seating(M: int, N: int, K: int, L: int, D: int, chatting_pairs: list) -> (str, str):
    """
    Optimize the placement of aisles in a classroom to minimize the amount of chatting between students.

    Args:
    M (int): The number of rows in the classroom.
    N (int): The number of columns in the classroom.
    K (int): The number of horizontal aisles to add.
    L (int): The number of vertical aisles to add.
    D (int): The number of chatting pairs in the classroom.
    chatting_pairs (list of tuples): A list of tuples, each containing the positions (Xi, Yi) and (Pi, Qi) of a chatting pair.

    Returns:
    (str, str): Two space-separated strings representing the optimal row and column indices for the aisles.

    The function works by counting the number of chatting pairs that can be separated by adding an aisle in each possible position.
    It then selects the most effective positions for aisles, aiming to separate as many chatting pairs as possible.

    Examples:
    - optimize_seating(4, 5, 1, 2, 3, [(4, 2, 4, 3), (2, 3, 3, 3), (2, 5, 2, 4)])
    Returns: ('2', '2 4')

    - optimize_seating(3, 3, 1, 1, 2, [(1, 2, 1, 3), (2, 1, 3, 1)])
    Returns: ('2', '2')
    """
    # Create a 2D array to represent the classroom
    classroom = [[0 for _ in range(N)] for _ in range(M)]

    # Mark the positions of chatting pairs in the classroom
    for pair in chatting_pairs:
        (x1, y1), (x2, y2) = pair
        classroom[x1-1][y1-1] += 1
        classroom[x2-1][y2-1] += 1

    # Count the number of chatting pairs in each row and column
    row_counts = [sum(row) for row in classroom]
    col_counts = [sum(col) for col in zip(*classroom)]

    # Find the row and column with the maximum number of chatting pairs
    max_row_count = max(row_counts)
    max_col_count = max(col_counts)
    max_row_index = row_counts.index(max_row_count)
    max_col_index = col_counts.index(max_col_count)

    # Add aisles to separate the row and column with the most chatting pairs
    for i in range(M):
        if i != max_row_index:
            K -= 1
            if K == 0:
                return str(max_row_index + 1), ' '.join(str(j + 1) for j in range(N) if j != max_col_index)

    for j in range(N):
        if j != max_col_index:
            L -= 1
            if L == 0:
                return str(max_row_index + 1), str(max_col_index + 1)

    return str(max_row_index + 1), ' '.join(str(j + 1) for j in range(N) if j != max_col_index)
def test_optimize_seating():
    test_cases = [
        # Test case 1 from the provided example
        {
            'M': 4, 'N': 5, 'K': 1, 'L': 2, 'D': 3,
            'chatting_pairs': [(4, 2, 4, 3), (2, 3, 3, 3), (2, 5, 2, 4)],
            'expected': ('2', '2 4')
        },
        # Corrected Test case 2
        {
            'M': 5, 'N': 6, 'K': 2, 'L': 3, 'D': 4,
            'chatting_pairs': [(1, 1, 1, 2), (2, 2, 3, 2), (4, 5, 4, 6), (5, 1, 5, 2)],
            'expected': ('1 2', '1 2 5')  # Corrected expected output
        },
        # Test case 3
        {
            'M': 3, 'N': 3, 'K': 1, 'L': 1, 'D': 2,
            'chatting_pairs': [(1, 2, 1, 3), (2, 1, 3, 1)],
            'expected': ('2', '2')
        },
    ]

    for i, test in enumerate(test_cases, 1):
        row_output, col_output = optimize_seating(
            test['M'], test['N'], test['K'], test['L'], test['D'], test['chatting_pairs']
        )
        assert row_output == test['expected'][0], f"Test case {i} failed: row_output {row_output} does not match expected {test['expected'][0]}"
        assert col_output == test['expected'][1], f"Test case {i} failed: col_output {col_output} does not match expected {test['expected'][1]}"
        print(f"Test case {i} passed.")

# Run the test function
test_optimize_seating()