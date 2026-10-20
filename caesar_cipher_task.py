def caesar_cipher(text, key, choice):
    result = ""

    for char in text:
        if char.isalpha():
            shift = key if choice == 1 else -key
            result += chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def main():
    print("1. Encryption")
    print("2. Decryption")

    choice = int(input("Enter your choice: "))
    text = input("Enter Plain Text: ")
    key = int(input("Enter Key: "))

    result = caesar_cipher(text, key, choice)
    print("Result:", result)


main()