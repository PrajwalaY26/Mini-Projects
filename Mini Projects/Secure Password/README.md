# Secure Password Program

Welcome to the Secure Password Program! This is a simple Python application designed to help you secure your existing password by replacing a set of characters with corresponding 'password-secure' characters.

## About

The application takes your password as input and replaces certain characters based on a predefined set of tuples. Each tuple contains a character from the password and its 'password-secure' replacement. The application then returns your new, more secure password.

## How it Works

The script uses a predefined set of tuples, `SECURE`, where each tuple contains a character from the password and its 'password-secure' replacement. The program then replaces each occurrence of the character in the password with its 'password-secure' counterpart.

Here is an example of the tuples used:

```python
SECURE = (('s', '$'), ('and', '&'), 
            ('a', '@'), ('o', '0'), ('i', '1'),
            ('I', '|'))
```

In this example, every occurrence of 's' in the password will be replaced with '$', 'and' with '&', 'a' with '@', 'o' with '0', 'i' with '1', and 'I' with '|'.

## Usage

To use this program, simply run it and when prompted, enter your password. The program will then print out your 'password-secure' password.

For example:

```shell
Enter your password
Indians123
Your secure password is |nd1@n$123
```

In this example, the user entered "Indians123" as their password. The program then replaced the characters according to the `SECURE` tuples and printed out the secure password "|nd1@n$123".

## Setup

To run this application, you need Python installed on your system. If you don't have Python installed, you can download it from the official site.

## Note

This program is a simple demonstration of how you can increase the security of a password. It is not intended to be used as a real-world password security solution. Always follow best practices for password security.
