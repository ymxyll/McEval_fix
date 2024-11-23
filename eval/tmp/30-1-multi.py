

def is_prime(num: int) -> bool:
    """
    Determine whether a given integer is a prime number.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function checks for primality by eliminating non-prime numbers using several tests. First, it handles edge cases for numbers less than or equal to 1, which are not prime, and small numbers (2 and 3) which are prime. It then checks for divisibility by 2 and 3. For larger numbers, it uses a 6k +/- 1 optimization to test for factors up to the square root of the number.

    Args:
    num (int): The integer to check for primality.

    Returns:
    bool: True if `num` is a prime number, False otherwise.

    Cases:
    - For num = 2 or num = 3, the function should return True, since both are prime numbers.
    - For num = 1 or num = 0, the function should return False, as neither is considered prime.
    - For num = 15, which is divisible by 3 and 5, the function should return False.
    - For num = 29, which has no divisors other than 1 and itself, the function should return True.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
    """Check if a number is a prime."""
    if num <= 1:
        return False
    if num <= 3:
        return num > 1
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
def test_is_prime():
    # Test case 1: Test a prime number
    prime_number = 29
    assert is_prime(prime_number) == True, f"Test case 1 failed: {prime_number} is a prime number."

    # Test case 2: Test a non-prime number
    non_prime_number = 21  # 21 = 3 * 7, so it's not prime
    assert is_prime(non_prime_number) == False, f"Test case 2 failed: {non_prime_number} is not a prime number."

    # Test case 3: Test a number less than 2 (should not be prime)
    less_than_two = 1
    assert is_prime(less_than_two) == False, f"Test case 3 failed: {less_than_two} is not a prime number."

    # Test case 4: Test another prime number
    another_prime_number = 97
    assert is_prime(another_prime_number) == True, f"Test case 4 failed: {another_prime_number} is a prime number."

    # Test case 5: Test zero (should not be prime)
    zero = 0
    assert is_prime(zero) == False, f"Test case 5 failed: {zero} is not a prime number."

    print("All test cases passed.")

# Run the test function
test_is_prime()