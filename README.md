# Password Generator

## 🛠️ Overview
The generate_password function is a robust tool for creating strong, secure passwords that meet customizable constraints. It ensures your passwords include a mix of uppercase letters, lowercase letters, numbers, and special characters for enhanced security.

### Key Features:
- Customizable password length.
- Guaranteed inclusion of specific character types (numbers, special characters, uppercase, lowercase).
- Cryptographically secure randomization using Python's secrets module.
- Ensures all specified constraints are met.

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 🔧 How it Works
The generate_password function takes several parameters:

- length: Total length of the password (default: 16 characters).
- nums: Minimum number of digits to include (default: 1).
- special_chars: Minimum number of special characters to include (default: 1).
- uppercase: Minimum number of uppercase letters to include (default: 1).
- lowercase: Minimum number of lowercase letters to include (default: 1).

The `generate_password` function takes several parameters:

- `length`: Length of the password (default is 16 characters)
- `nums`: Number of digits to include in the password (default is 1)
- `special_chars`: Number of special characters to include in the password (default is 1)
- `uppercase`: Number of uppercase letters to include in the password (default is 1)
- `lowercase`: Number of lowercase letters to include in the password (default is 1)

The function generates a password by randomly selecting characters from a pool of uppercase letters, lowercase letters, digits, and special characters. It ensures that the generated password meets the specified constraints by using regular expressions to count the occurrences of each character type.

## Usage

To generate a password, simply run the script `generate_password.py`. Here's an example:


This repository is for educational purposes only and has an MIT License

### Show your support

Give a ⭐ if you like these projects!
# Contributors
- [Vadym Makohon](https://github.com/VadymMakohon)
