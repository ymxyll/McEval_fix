

from itertools import permutations

def find_number_combinations():
    """
    Generate all unique combinations of three numbers, each formed from the digits 1 to 9 without repetition,
    such that the second number is twice the first and the third is three times the first.

    Returns:
        list of tuples: A sorted list of tuples, where each tuple contains three integers representing the
                        valid number combinations in ascending order based on the first number.

    Example:
        >>> find_number_combinations()
        [(123, 246, 369), (124, 248, 372), ...]
    """
    # Store the valid combinations
    valid_combinations = []

    # Generate all permutations of the numbers 1 through 9
    for perm in permutations(range(1, 10)):
        # Split the permutation into three numbers
        num1 = perm[0] * 100 + perm[1] * 10 + perm[2]
        num2 = perm[3] * 100 + perm[4] * 10 + perm[5]
        num3 = perm[6] * 100 + perm[7] * 10 + perm[8]

        # Check if the numbers form a 1:2:3 ratio
        if num2 == 2 * num1 and num3 == 3 * num1:
            valid_combinations.append((num1, num2, num3))

    # Sort the valid combinations in ascending order based on the first number
    valid_combinations.sort()

    return valid_combinations
def test_find_number_combinations():
    # Call the function to get the combinations
    combinations = find_number_combinations()

    # Check that we have at least one valid combination
    assert len(combinations) > 0, "There should be at least one valid combination."

    # Iterate over each combination to perform further checks
    for combo in combinations:
        # Each combination should have exactly three numbers
        assert len(combo) == 3, "Each combination should have three numbers."

        # Check if numbers are 3-digit numbers
        for num in combo:
            assert 100 <= num <= 999, f"Each number should be a 3-digit number, got {num}."

        # Check the 1:2:3 ratio
        assert combo[1] == 2 * combo[0] and combo[2] == 3 * combo[0], "The numbers should be in a 1:2:3 ratio."

    print("All test cases passed!")