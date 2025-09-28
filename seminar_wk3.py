"""Program that asks user for a low and high number then prints 'n' smiley faces."""

LOW = 1
HIGH = 10

def main():
    first_number = get_valid_number("Enter a number: ", LOW, HIGH)
    for i in range(number):
        print(f":)")


def get_valid_number(prompt, low, high):
    """Get a valid number from the user."""
    number = int(input(prompt))

    while number < low or number > high:
        print(f"Invalid number. Please enter a number between {low} and {high}.")
        number  = int(input(prompt))
    return number


main()