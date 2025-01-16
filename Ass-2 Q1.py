def encrypt(text, n, m):
    encrypted_text = ""

    for char in text:
        if char.islower():  # For lowercase letters
            if 'a' <= char <= 'm':  # First half of the alphabet (a-m)
                encrypted_text += chr((ord(char) - ord('a') + n * m) % 26 + ord('a'))
            elif 'n' <= char <= 'z':  # Second half of the alphabet (n-z)
                encrypted_text += chr((ord(char) - ord('a') - (n + m)) % 26 + ord('a'))
        elif char.isupper():  # For uppercase letters
            if 'A' <= char <= 'M':  # First half of the alphabet (A-M)
                encrypted_text += chr((ord(char) - ord('A') - n) % 26 + ord('A'))
            elif 'N' <= char <= 'Z':  # Second half of the alphabet (N-Z)
                encrypted_text += chr((ord(char) - ord('A') + m**2) % 26 + ord('A'))
        else:  # Special characters, spaces, and numbers remain unchanged
            encrypted_text += char
    
    return encrypted_text


def decrypt(text, n, m):
    decrypted_text = ""

    for char in text:
        if char.islower():  # For lowercase letters
            if 'a' <= char <= 'm':  # First half of the alphabet (a-m)
                decrypted_text += chr((ord(char) - ord('a') - n * m) % 26 + ord('a'))
            elif 'n' <= char <= 'z':  # Second half of the alphabet (n-z)
                decrypted_text += chr((ord(char) - ord('a') + (n + m)) % 26 + ord('a'))
        elif char.isupper():  # For uppercase letters
            if 'A' <= char <= 'M':  # First half of the alphabet (A-M)
                decrypted_text += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            elif 'N' <= char <= 'Z':  # Second half of the alphabet (N-Z)
                decrypted_text += chr((ord(char) - ord('A') - m**2) % 26 + ord('A'))
        else:  # Special characters, spaces, and numbers remain unchanged
            decrypted_text += char
    
    return decrypted_text


def check_correctness(original_text, decrypted_text):
    return original_text == decrypted_text


def main():
    # Read the raw text from the file
    try:
        with open('raw_text.txt', 'r') as file:
            raw_text = file.read()
    except FileNotFoundError:
        print("The file 'raw_text.txt' does not exist.")
        return
    
    # Get user inputs for n and m
    n = int(input("Enter the value for n: "))
    m = int(input("Enter the value for m: "))
    
    # Encrypt the text
    encrypted_text = encrypt(raw_text, n, m)
    
    # Write the encrypted text to a new file
    with open('encrypted_text.txt', 'w') as file:
        file.write(encrypted_text)
    
    print("Encryption complete. Encrypted text saved to 'encrypted_text.txt'.")
    
    # Decrypt the encrypted text
    decrypted_text = decrypt(encrypted_text, n, m)
    
    # Check if the decrypted text matches the original text
    if check_correctness(raw_text, decrypted_text):
        print("Decryption is correct! The text matches the original.")
    else:
        print("Decryption failed. The text does not match the original.")

if __name__ == "__main__":
    main()