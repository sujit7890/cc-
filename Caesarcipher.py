def caesar_cipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

if __name__ == "__main__":
    plaintext = input("Enter the plain text: ")
    key = int(input("Enter the key: "))
    encrypted_text = caesar_cipher(plaintext, key)
    print("Encrypted text:", encrypted_text)