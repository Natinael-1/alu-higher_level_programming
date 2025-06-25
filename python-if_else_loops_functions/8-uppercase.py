#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    result = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:  # Check if lowercase
            result += chr(ord(c) - 32)      # Convert to uppercase
        else:
            result += c
    print(result)
