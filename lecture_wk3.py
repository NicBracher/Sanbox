""" "CP1404/CP5632 Lecuture notes and programs - Nicholas Bracher"""

FILENAME = "secret_number.txt"


def main():
    secret = load_number(FILENAME)
    get_valid_number()

    while guess != secret:
        print("Incorrect, try again.")
        guess = int(input("Enter your guess: "))
    print("Congratulations, you guessed it!")


# Exceptoon-based error checking can be found on the programming patterns page

"""
is_valid_input = False
while not is_valid_input:
    try:
        age = int(input("Age: "))
        if age < 0:
            print("Age must be >= 0")
        else:
            is_valid_input = True
    except ValueError:
        print("Invalid (not an integer)")
print("Next year you will be", age + 1)
"""


def get_valid_number():
    """Get a valid number from the user."""
    is_valid_input = False
    while not is_valid_input:
        try:
            guess = int(input("Enter your guess: "))
            is_valid_input = True
        except ValueError:
            print("Invalid input, please enter a valid number.")
    return guess


def load_number(filename):
    """Load a number from a file."""
    try:
        infile = open(filename, "r") # 'r' or 'read' is default mode
        # The filename can be a variable or a string, i.e. magic_file or "magic_file.txt" 
        # Additionally this defaults to the current working directory, but you can specify a path
        number = int(infile.read()) # Its good practice to program like the file may not exsist
        # this is storing the contents of the file as an integer in a variable called number
        # with infile.read() the program will read the entire file unless you specify the bytes within the brackets
        # e.g. infile.read(5) will read the first 5 bytes of the file
    except ValueError:
        print("Invalid contents in file.")
        number = 1
        for line in infile: # This was just thrown in here as an example, when iterating through a file, always use the line variable name
            print(line) # There is always a \n at the end of each line unless its the last line so use .strip() to remove it.
            # the .replace("\n", "") method can also be used to remove the newline character
    except FileNotFoundError:
        print("File not found.")
        number = 1
    else: 
        infile.close() # If you were to write to the file the name would be out_file.close 
        # Make sure to always close a file when you are done with it.
    return number



# main()


def do_this_now():
    """This is a practice function at pulling information out of a file."""
    in_file = open("data.txt", "r")
    for line in in_file:
        if line.startswith("#"):
            print(line.strip())
    in_file.close()    


do_this_now()