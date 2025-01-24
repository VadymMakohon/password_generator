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

## 📋Example Workflow:

1. The function ensures each specified character type is included by pre-selecting the required amount.
2. Any remaining characters are randomly selected from a pool of all character types.
3. The selected characters are shuffled for randomness and returned as a secure password.

## 🚀 Usage

Prerequisites:
- Make sure you have Python 3 installed on your machine.

Steps to Run:
1. Clone the repository:
- `bash` `git clone https://github.com/VadymMakohon/password_generator.git`
- `cd password_generator`
2. Run the script:
- `python generate_password.py`
3. Example Output:
- `Generated password: P@ssw0rd!23XyZ4&`

To generate a password, simply run the script `generate_password.py`. Here's an example:


This repository is for educational purposes only and has an MIT License

## 💬 Show your support

Give a ⭐ if you like these projects!

# 🤝 Contributors
- [Vadym Makohon](https://github.com/VadymMakohon)
