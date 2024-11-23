

def catalan_number(n: int) -> int:
    """
    Calculate the nth Catalan number.

    The function computes the nth Catalan number using dynamic programming. Catalan numbers are a sequence of natural 
    numbers that have many applications in combinatorial mathematics, including the counting of certain types of lattice paths, 
    the number of expressions containing n pairs of parentheses which are correctly matched, the number of different ways n+1 
    factors can be completely parenthesized, and more.

    Args:
    - n (int): The position in the Catalan number sequence to compute (must be non-negative).

    Returns:
    - int: The nth Catalan number.

    Cases:
    - For n=0, the function should return 1, since C(0) = 1.
      catalan_number(0) -> 1

    - For n=3, the function should return 5, since C(3) = 5.
      catalan_number(3) -> 5

    - For n=5, the function should return 42, since C(5) = 42.
      catalan_number(5) -> 42

    Note:
    The computation is based on the recursive formula:
    C(n) = C(0)C(n-1) + C(1)C(n-2) + ... + C(n-1)C(0)
    where C(0) is 1.
    """
    # Initialize an array to store the intermediate catalan numbers
    catalan = [0 for _ in range(n+1)]

    # Base case
    if n == 0:
        return 1

    # Initialize the first two values
    catalan[0] = 1
    catalan[1] = 1

    # Compute the rest of the values
    for i in range(2, n+1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1]

    # Return the nth catalan number
    return catalan[n]
def test_catalan_number():
    # Test case 1: The first Catalan number (base case)
    n1 = 0
    expected_output1 = 1
    assert catalan_number(n1) == expected_output1, f"Test case 1 failed: expected {expected_output1}, got {catalan_number(n1)}"

    # Test case 2: The third Catalan number
    n2 = 3
    expected_output2 = 5
    assert catalan_number(n2) == expected_output2, f"Test case 2 failed: expected {expected_output2}, got {catalan_number(n2)}"

    # Test case 3: The fifth Catalan number
    n3 = 5
    expected_output3 = 42
    assert catalan_number(n3) == expected_output3, f"Test case 3 failed: expected {expected_output3}, got {catalan_number(n3)}"

    print("All test cases passed!")

# Run the test function
test_catalan_number()