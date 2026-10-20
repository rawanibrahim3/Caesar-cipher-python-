
# Caesar Cipher

## Description
This project implements the Caesar Cipher encryption and decryption algorithm using Python.

The program allows the user to choose encryption or decryption, enter a text message, and provide a numeric key.

## Features
- Encrypts text using the Caesar Cipher.
- Decrypts text using the Caesar Cipher.
- Preserves spaces, numbers, and punctuation.

## Requirements
- Python 3

## How to Run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the following command:

   ```bash
   python "caesar_cipher task.py"
   ```

4. Choose an option:
   - `1` for Encryption
   - `2` for Decryption
5. Enter the plain text and the numeric key.

## Example
```text
1. Encryption
2. Decryption
Enter your choice: 1
Enter Plain Text: hello
Enter Key: 3
Result: khoor
```

## How It Works
The Caesar Cipher shifts each alphabetic character by a specified key:
- Encryption shifts letters forward.
- Decryption shifts letters backward.
- The modulo operation (`% 26`) keeps letters within the English alphabet.

## Note
This project is intended for educational purposes. The Caesar Cipher is not secure enough to protect sensitive information.
