

def mod_inverse(a, b):
    """
    Calculate the modular multiplicative inverse of `a` modulo `b`.
    
    This function finds an integer `x` such that (a * x) % b == 1, provided that
    `a` and `b` are coprime (i.e., gcd(a, b) == 1). It uses the Extended Euclidean
    Algorithm to compute the inverse. If `a` and `b` are not coprime, the modular
    inverse does not exist, and the function returns `None`.
    
    Args:
      a (int): The integer whose modular inverse is to be found.
      b (int): The modulus with respect to which the inverse is sought.
    
    Returns:
      int: The modular inverse of `a` modulo `b` if it exists, otherwise `None`.
    
    Examples:
      >>> mod_inverse(3, 10)
      7
      # Explanation: (3 * 7) % 10 == 1

      >>> mod_inverse(17, 3120)
      2753
      # Explanation: (17 * 2753) % 3120 == 1

      >>> mod_inverse(42, 2017)
      None
      # Explanation: gcd(42, 2017) != 1, so no inverse exists
    """
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    gcd, x, _ = extended_gcd(a, b)
    if gcd != 1:
        # Modular inverse does not exist since a and b are not coprime
        return None
    else:
        # Make sure the result is positive
        return x % b
def test_mod_inverse():
    test_cases = [
        (3, 10),  # Test case 1: gcd(3, 10) = 1, inverse should be 7
        (17, 3120),  # Test case 2: gcd(17, 3120) = 1, inverse should be 2753
        (42, 2017),  # Test case 3: gcd(42, 2017) = 1, inverse should be 1969
    ]
    expected_results = [
        7,  # Expected result for test case 1
        2753,  # Expected result for test case 2
        1969,  # Expected result for test case 3
    ]

    for i, (a, b) in enumerate(test_cases):
        actual_result = mod_inverse(a, b)
        expected_result = expected_results[i]
        assert actual_result == expected_result, f"Test case {i+1} failed: expected {expected_result}, got {actual_result}"
        print(f"Test case {i+1} passed: a={a}, b={b}, x0={actual_result}")

# Run the test function
test_mod_inverse()