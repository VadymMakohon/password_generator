# Password Generator

## How it Works

The `generate_password` function takes several parameters:

- `length`: Length of the password (default is 16 characters)
- `nums`: Number of digits to include in the password (default is 1)
- `special_chars`: Number of special characters to include in the password (default is 1)
- `uppercase`: Number of uppercase letters to include in the password (default is 1)
- `lowercase`: Number of lowercase letters to include in the password (default is 1)

The function generates a password by randomly selecting characters from a pool of uppercase letters, lowercase letters, digits, and special characters. It ensures that the generated password meets the specified constraints by using regular expressions to count the occurrences of each character type.

## Usage

To generate a password, simply run the script `generate_password.py`. Here's an example:

```bash
$ python generate_password.py
Generated Password: H3llo@W0rld!

## Contributors
- [Vadym Makohon](https://github.com/VadymMakohon)
