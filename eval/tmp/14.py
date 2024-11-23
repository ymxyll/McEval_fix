

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
    """
    # Split the ISBN into its parts
    parts = isbn.split('-')
    
    # Calculate the checksum
    checksum = 0
    for i, part in enumerate(parts[:-1]):
        checksum += (10 - i) * int(part)
    
    # Calculate the expected checksum digit
    expected_checksum = (11 - (checksum % 11)) % 11
    
    # If the expected checksum is 10, replace it with 'X'
    if expected_checksum == 10:
        expected_checksum = 'X'
    
    # If the expected checksum is 11, replace it with 0
    if expected_checksum == 11:
        expected_checksum = 0
    
    # If the expected checksum is equal to the last character of the ISBN, return 'Right'
    if str(expected_checksum) == parts[-1].upper():
        return 'Right'
    
    # Otherwise, return the corrected ISBN
    else:
        return isbn[:-1] + str(expected_checksum)
def test_verify_isbn():
    # Test case 1: Correct ISBN number
    assert verify_isbn("0-670-82162-4") == "Right", "Test case 1 failed"

    # Test case 2: Incorrect ISBN number with wrong checksum digit
    assert verify_isbn("0-670-82162-0") == "0-670-82162-4", "Test case 2 failed"

    print("All test cases passed!")

# Run the test cases
test_verify_isbn()