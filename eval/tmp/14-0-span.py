

def verify_isbn(isbn: str) -> str:
    """
    Verify the correctness of a given ISBN number and correct it if necessary.

    The function checks the provided ISBN number against the ISBN standard checksum calculation.
    If the checksum is correct, the function returns "Right". If the checksum is incorrect,
    the function returns the corrected ISBN number.

    Args:
    isbn: A string representing the ISBN number to be verified. The format should be 'x-xxx-xxxxx-x',
          where 'x' is a digit, and the last 'x' could also be 'X' representing the checksum digit.

    Returns:
    A string that is either "Right" if the ISBN checksum is correct, or the corrected ISBN number
    in the same format as the input if the checksum is incorrect.

    Examples:
    >>> verify_isbn("0-670-82162-4")
    'Right'
    
    >>> verify_isbn("0-670-82162-0")
    '0-670-82162-4'

    The second example shows the correction of the ISBN number where the checksum digit is calculated
    to be '4' instead of the provided '0', thus the corrected ISBN is returned.
    """
    # Function implementation goes here.
    # Remove the hyphens '-' and keep only the digits and possibly 'X'
    isbn_digits = isbn.replace('-', '')

    # Calculate the sum of products
    total_sum = sum((10 - i) * int(digit) for i, digit in enumerate(isbn_digits[:-1]))

    # Calculate the check digit
    check_digit = (11 - (total_sum % 11)) % 11

    # Convert the check digit to a character
    if check_digit == 10:
        check_digit_char = 'X'
    else:
        check_digit_char = str(check_digit)

    # Compare with the last digit of the input ISBN
    if check_digit_char == isbn_digits[-1].upper():
        return "Right"
    else:
        # Return the corrected ISBN
        return isbn[:-1] + check_digit_char
def test_verify_isbn():
    # Test case 1: Correct ISBN number
    assert verify_isbn("0-670-82162-4") == "Right", "Test case 1 failed"

    # Test case 2: Incorrect ISBN number with wrong checksum digit
    assert verify_isbn("0-670-82162-0") == "0-670-82162-4", "Test case 2 failed"

    print("All test cases passed!")

# Run the test cases
test_verify_isbn()