

def decode(encoded: str, original: str, message: str) -> str:
    """
    Decodes an encrypted message using a cipher derived from a known encoded-original pair.
    
    The function builds a mapping from encoded letters to their original letters and uses this
    mapping to decode a given encrypted message. If a contradiction is found during mapping
    construction, or not all letters are represented in the mapping, the function returns "Failed".
    
    Args:
    encoded (str): A string representing the encoded information.
    original (str): A string representing the original information corresponding to the encoded string.
    message (str): A string representing the encrypted message to be decoded.
    
    Returns:
    str: The decoded message if successful, or "Failed" if the decoding is not possible.
    
    Examples:
    >>> decode("AA", "AB", "EOWIE")
    'Failed'
    
    >>> decode("QWERTYUIOPLKJHGFDSAZXCVBN", "ABCDEFGHIJKLMNOPQRSTUVWXY", "DSLIEWO")
    'Failed'
    
    >>> decode("MSRTZCJKPFLQYVAWBINXUEDGHOOILSMIJFRCOPPQCEUNYDUMPP", "YIZSDWAHLNOVFUCERKJXQMGTBPPKOIYKANZWPLLVWMQJFGQYLL", "FLSO")
    'NOIP'
    """
    # Initialize a mapping dictionary to store the relationship between letters and their corresponding code letters
    mapping = {}
    reverse_mapping = {}
    
    # Build the mapping based on the encoded information and the original information
    for e, o in zip(encoded, original):
        if e in mapping and mapping[e] != o:
            # A contradiction is found, output "Failed"
            return "Failed"
        mapping[e] = o
        reverse_mapping[o] = e
    
    # Check if all letters are represented in the mapping
    if len(mapping) != 26:
        return "Failed"
    
    # Decode the message using the mapping
    decoded_message = ''
    for char in message:
        if char in reverse_mapping:
            decoded_message += reverse_mapping[char]
        else:
            # If a character in the message is not in the mapping, output "Failed"
            return "Failed"
    
    return decoded_message
def test_decode():
    # Test case 1: Contradiction in mapping
    assert decode("AA", "AB", "EOWIE") == "Failed", "Test case 1 failed"

    # Test case 2: Not all letters are represented
    assert decode("QWERTYUIOPLKJHGFDSAZXCVBN", "ABCDEFGHIJKLMNOPQRSTUVWXY", "DSLIEWO") == "Failed", "Test case 2 failed"

    # Test case 3: Successful decoding
    assert decode("MSRTZCJKPFLQYVAWBINXUEDGHOOILSMIJFRCOPPQCEUNYDUMPP", "YIZSDWAHLNOVFUCERKJXQMGTBPPKOIYKANZWPLLVWMQJFGQYLL", "FLSO") == "NOIP", "Test case 3 failed"
    
    # Test case 4: Character in message not in mapping
    assert decode("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ", "UVWXYZ") == "Failed", "Test case 4 failed"

    # Test case 5: Empty strings
    assert decode("", "", "") == "Failed", "Test case 5 failed"

    print("All test cases passed!")

# Call the test function to run the test cases
test_decode()