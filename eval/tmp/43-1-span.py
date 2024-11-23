

from itertools import permutations
def next_permutation(perm: list) -> bool:
    """
    Transforms the input permutation to the next permutation in lexicographic order.
    
    The function finds the first number from the end that is smaller than the number following it 
    and swaps it with the smallest number that is larger and comes after it. Then it reverses the 
    order of numbers after the original first smaller number. If the input is the last permutation 
    (in descending order), the function returns False, indicating no next permutation is possible.
    
    Args:
    perm (list): A list of integers representing the current permutation.
    
    Returns:
    bool: True if the permutation was successfully transformed, False if it was the last permutation.
    
    Examples:
    >>> next_permutation([1, 2, 3])
    True
    >>> [1, 2, 3]
    [1, 3, 2]
    
    >>> next_permutation([3, 2, 1])
    False
    >>> [3, 2, 1]
    [3, 2, 1]
    
    >>> next_permutation([1, 3, 2])
    True
    >>> [1, 3, 2]
    [2, 1, 3]
    """
    # Find the first (smaller) number from the end which is smaller than the number after it
    i = len(perm) - 2
    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1
    
    # If no such number exists, this is the last permutation
    if i == -1:
        return False
    
    # Find the first (larger) number from the end which is larger than the (smaller) number found above
    j = len(perm) - 1
    while perm[j] <= perm[i]:
        j -= 1
    
    # Swap the found numbers
    perm[i], perm[j] = perm[j], perm[i]
    
    # Reverse the rest of the list
    perm[i + 1:] = perm[i + 1:][::-1]
    
    return True
def test_next_permutation():
    # Test case 1: ordinary case
    perm1 = [1, 2, 3]
    assert next_permutation(perm1) == True, "Test case 1 failed: next_permutation([1, 2, 3]) should return True"
    assert perm1 == [1, 3, 2], "Test case 1 failed: perm1 should be [1, 3, 2]"
    
    # Test case 2: last permutation, should return False
    perm2 = [3, 2, 1]
    assert next_permutation(perm2) == False, "Test case 2 failed: next_permutation([3, 2, 1]) should return False"
    assert perm2 == [3, 2, 1], "Test case 2 failed: perm2 should be [3, 2, 1] (unchanged)"
    
    # Test case 3: permutation with repeated elements
    perm3 = [1, 5, 1]
    assert next_permutation(perm3) == True, "Test case 3 failed: next_permutation([1, 5, 1]) should return True"
    assert perm3 == [5, 1, 1], "Test case 3 failed: perm3 should be [5, 1, 1]"

    # Test case 4: permutation with all elements equal
    perm4 = [1, 1, 1]
    assert next_permutation(perm4) == False, "Test case 4 failed: next_permutation([1, 1, 1]) should return False"
    assert perm4 == [1, 1, 1], "Test case 4 failed: perm4 should be [1, 1, 1] (unchanged)"
    
    # Test case 5: permutation with only one element
    perm5 = [42]
    assert next_permutation(perm5) == False, "Test case 5 failed: next_permutation([42]) should return False"
    assert perm5 == [42], "Test case 5 failed: perm5 should be [42] (unchanged)"
    
    print("All test cases passed.")

# Run the test function
test_next_permutation()