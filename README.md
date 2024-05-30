# Password Validation and Hashing System

This project demonstrates a secure approach to password validation and hashing, ensuring that plaintext passwords are never directly exposed. The system obfuscates the password on the client-side before validation and hashes it before sending it to the server, where it is re-hashed for additional security.

## Features

- **Client-Side Validation**: Ensures the password meets complexity requirements using regex.
- **Client-Side Hashing**: Hashes the password on the client-side before sending it to the server.
- **Server-Side Hashing**: Re-hashes the received password on the server before storing it.

## How It Works

1. **Password Input**: User inputs a password in the form.
2. **Password Obfuscation**: The client-side script shuffles the characters of the password to obfuscate its original order.
3. **Character Counting**: The script counts the number of alphabets, numbers, and special characters in the obfuscated password.
4. **Regex Validation**: The script checks if the password meets the complexity requirements.
5. **Client-Side Hashing**: If the password is valid, it is hashed using the Web Crypto API.
6. **Password Submission**: The hashed password is sent to the server.
7. **Server-Side Re-Hashing**: The server re-hashes the received password and stores it securely.

## Prerequisites

- Web browser with JavaScript enabled.
- Python 3.x with Flask and Werkzeug installed.

## Setup and Usage

1. Implement the client-side validation, hashing, and submission in HTML and JavaScript.
2. Implement the server-side password handling and hashing in Python using Flask.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Inspired by discussions in COMP9044 about Regex
