# EnkripsiDeskripsi_CaesarCipher_SourceCode

This project implements text encryption and decryption using the Caesar Cipher method. Caesar Cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

### Project Description

The project consists of two main functions:
1. `encrypt(plaintext, key)`: Encrypts the given plaintext using the provided key.
2. `decrypt(ciphertext, key)`: Decrypts the given ciphertext using the provided key.

Additionally, the `main()` function provides a user interface to choose between encryption, decryption, or exiting the program.

### How it Works

1. **Encryption**:
    - For each character in the plaintext:
        - If the character is an alphabet letter, it is shifted by the key value.
        - The shift considers whether the character is uppercase or lowercase.
        - Non-alphabet characters remain unchanged.
    - The shifted characters are combined to form the encrypted text.

2. **Decryption**:
    - For each character in the ciphertext:
        - If the character is an alphabet letter, it is shifted back by the key value.
        - The shift considers whether the character is uppercase or lowercase.
        - Non-alphabet characters remain unchanged.
    - The shifted characters are combined to form the decrypted text.

### Features

- **Encrypt Text**: Encrypts the input plaintext using a key (1-25).
- **Decrypt Text**: Decrypts the input ciphertext using a key (1-25).
- **User Interface**: Provides a menu-driven interface for user interaction.

### Usage

1. **Run the Program**:
    ```bash
    python caesar_cipher.py
    ```
2. **Menu Options**:
    - **1. Encrypt plaintext**: Encrypts the input plaintext.
    - **2. Decrypt ciphertext**: Decrypts the input ciphertext.
    - **3. Exit**: Exits the program.

3. **Input**:
    - **Plaintext/Ciphertext**: The text to be encrypted or decrypted.
    - **Key**: An integer between 1 and 25.

### Example

- **Encryption**:
    ```plaintext
    Enter plaintext: hello
    Enter key (1-25): 3
    Encrypted text: khoor
    ```

- **Decryption**:
    ```plaintext
    Enter ciphertext: khoor
    Enter key (1-25): 3
    Decrypted text: hello
    ```

### Contact

If you have any suggestions or feedback, please don't hesitate to contact me via LinkedIn or Email:
- **Email**: your_email@example.com
- **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/your-profile)

#CaesarCipher #Encryption #Decryption #Python #Security
