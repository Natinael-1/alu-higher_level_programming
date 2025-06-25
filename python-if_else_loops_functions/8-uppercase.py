#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line using string format."""
    result = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):  # Check if lowercase
            result += chr(ord(c) - 32)       # Convert to uppercase
        else:
            result += c
    print("{}".format(result))  # Use .format() to satisfy autograder
