#!/usr/bin/python3
def print_last_digit(number):
    """Print the last digit of a number and return its value."""
    last_digit = abs(number) % 10  # Get the last digit (handles negatives)
    print(last_digit, end="")      # Print without newline
    return last_digit
