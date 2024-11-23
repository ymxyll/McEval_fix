

def vigenere_decrypt(key: str, ciphertext: str) -> str:
    """
    Decrypts a ciphertext encrypted with the Vigenère cipher using the provided key.
    
    The Vigenère cipher is a method of encrypting alphabetic text by using a series of
    Caesar ciphers based on the letters of a keyword. This function reverses the process
    to recover the original plaintext from the ciphertext.

    Args:
        key (str): The encryption key used to encrypt the original plaintext.
                   This key should consist only of alphabetic characters.
        ciphertext (str): The encrypted text that needs to be decrypted.
                          The ciphertext should consist only of alphabetic characters.

    Returns:
        str: The decrypted plaintext corresponding to the input ciphertext.

    Examples:
        >>> vigenere_decrypt("CompleteVictory", "Yvqgpxaimmklongnzfwpvxmniytm")
        'Wherethereisawillthereisaway'

        >>> vigenere_decrypt("ABC", "DEF")
        'DCB'

        >>> vigenere_decrypt("xyz", "abc")
        'xyz'
        
        >>> vigenere_decrypt("MiXeD", "JpOeR")
        'Hello'
        
        >>> vigenere_decrypt("short", "PqrsPqrsPq")
        'LongLongLo'
    """
    # Function implementation as provided
    # Convert the key to uppercase for simplicity
    key = key.upper()
    key_length = len(key)
    
    # Define the alphabet
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Initialize the plaintext result
    plaintext = []
    
    # Decryption process
    for i, char in enumerate(ciphertext):
        # Get the corresponding key character
        key_char = key[i % key_length]
        
        # Get the position of the key character and the ciphertext character in the alphabet
        key_pos = alphabet.index(key_char)
        char_pos = alphabet.index(char)
        
        # Calculate the position of the plaintext character
        plaintext_pos = (char_pos - key_pos) % 26
        
        # Append the plaintext character to the result
        plaintext.append(alphabet[plaintext_pos])
    
    # Join the plaintext characters into a string and return
    return ''.join(plaintext)
def test_vigenere_decrypt():
    # Test case 1: Example provided in the problem statement
    key1 = "CompleteVictory"
    ciphertext1 = "Yvqgpxaimmklongnzfwpvxmniytm"
    expected_plaintext1 = "Wherethereisawillthereisaway"
    assert vigenere_decrypt(key1, ciphertext1) == expected_plaintext1, "Test case 1 failed"

    # Test case 2: All uppercase characters
    key2 = "ABC"
    ciphertext2 = "DEF"
    expected_plaintext2 = "DDD"
    assert vigenere_decrypt(key2, ciphertext2) == expected_plaintext2, "Test case 2 failed"

    # Test case 3: All lowercase characters
    key3 = "xyz"
    ciphertext3 = "abc"
    expected_plaintext3 = "ddd"
    assert vigenere_decrypt(key3, ciphertext3) == expected_plaintext3, "Test case 3 failed"

    # Test case 4: Mixed case characters
    key4 = "MiXeD"
    ciphertext4 = "JpOeR"
    expected_plaintext4 = "XhRaO"
    assert vigenere_decrypt(key4, ciphertext4) == expected_plaintext4, "Test case 4 failed"

    # Test case 5: Key shorter than ciphertext
    key5 = "short"
    ciphertext5 = "PqrsPqrsPq"
    expected_plaintext5 = "XjdbWykeYx"
    assert vigenere_decrypt(key5, ciphertext5) == expected_plaintext5, "Test case 5 failed"

    print("All test cases passed!")

# Run the test function
test_vigenere_decrypt()