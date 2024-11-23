

def min_groups(w, n, prices):
    """
    Determines the minimum number of groups needed to distribute souvenirs with a constraint on the group's total price.
    
    The souvenirs are grouped in pairs such that the total price of each group does not exceed the limit `w`. 
    The function aims to minimize the number of groups created under this constraint.
    
    Args:
    w (int): The maximum allowed sum of prices for any group of souvenirs.
    n (int): The total number of souvenirs.
    prices (list): A list of integers representing the price of each souvenir.
    
    Returns:
    int: The minimum number of groups required to distribute all souvenirs.

    Examples:
    
    Case 1:
    A limit of 100 and 9 souvenirs with prices [90, 20, 20, 30, 50, 60, 70, 80, 90].
    The minimum number of groups is 6.
    >>> min_groups(100, 9, [90, 20, 20, 30, 50, 60, 70, 80, 90])
    6
    
    Case 2:
    A limit of 200 and 5 souvenirs with prices [80, 120, 60, 40, 100].
    The minimum number of groups is 3.
    >>> min_groups(200, 5, [80, 120, 60, 40, 100])
    3
    
    Case 3:
    A limit of 80 and 4 souvenirs with prices [30, 30, 20, 10].
    Since each pair's total price does not exceed the limit, the minimum number of groups is 2.
    >>> min_groups(80, 4, [30, 30, 20, 10])
    2
    """
    prices.sort()  # Sort the prices in ascending order
    groups = 0
    left = 0  # Pointer to the least expensive souvenir
    right = n - 1  # Pointer to the most expensive souvenir

    while left <= right:
        if prices[left] + prices[right] <= w:
            # If the cheapest and the most expensive can be paired, do so
            left += 1
            right -= 1
        # Whether paired or not, the most expensive souvenir forms a group
        groups += 1
        right -= 1

    return groups
def test_min_groups():
    # Test case 1
    w1 = 100
    n1 = 9
    prices1 = [90, 20, 20, 30, 50, 60, 70, 80, 90]
    expected_output1 = 6
    assert min_groups(w1, n1, prices1) == expected_output1, "Test case 1 failed"

    # Test case 2
    w2 = 200
    n2 = 5
    prices2 = [80, 120, 60, 40, 100]
    expected_output2 = 3
    assert min_groups(w2, n2, prices2) == expected_output2, "Test case 2 failed"

    # Test case 3
    w3 = 80
    n3 = 4
    prices3 = [30, 30, 20, 10]
    expected_output3 = 2
    assert min_groups(w3, n3, prices3) == expected_output3, "Test case 3 failed"

    print("All test cases passed!")

# Run the test function
test_min_groups()