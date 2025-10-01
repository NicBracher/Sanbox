""" "CP1404/CP5632 Lecuture notes and programs - Nicholas Bracher"""

FILENAME = "secret_number.txt"


# def main():
#     secret = load_number(FILENAME)
#     get_valid_number()

#     while guess != secret:
#         print("Incorrect, try again.")
#         guess = int(input("Enter your guess: "))
#     print("Congratulations, you guessed it!")


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
        infile = open(filename, "r")  # 'r' or 'read' is default mode
        # The filename can be a variable or a string, i.e. magic_file or "magic_file.txt"
        # Additionally this defaults to the current working directory, but you can specify a path
        number = int(
            infile.read()
        )  # Its good practice to program like the file may not exsist
        # this is storing the contents of the file as an integer in a variable called number
        # with infile.read() the program will read the entire file unless you specify the bytes within the brackets
        # e.g. infile.read(5) will read the first 5 bytes of the file
    except ValueError:
        print("Invalid contents in file.")
        number = 1
        for (
            line
        ) in (
            infile
        ):  # This was just thrown in here as an example, when iterating through a file, always use the line variable name
            print(
                line
            )  # There is always a \n at the end of each line unless its the last line so use .strip() to remove it.
            # the .replace("\n", "") method can also be used to remove the newline character
    except FileNotFoundError:
        print("File not found.")
        number = 1
    else:
        infile.close()  # If you were to write to the file the name would be out_file.close
        # Make sure to always close a file when you are done with it.
    return number


# main()


# def do_this_now():
    """This is a practice function at pulling information out of a file."""
    in_file = open("data.txt", "r")
    for line in in_file:
        if line.startswith("#"):
            print(line.strip())
    in_file.close()


# do_this_now()


"""Example contents of data2.txt file:
Fender Stratocaster,2014,765.40\n
Gibson L-5 CES,1922,16035.40\n
Line 6 JTV-59,2010,1512.90\n"""


def second_do_this_now():
    """This is a practice function at pulling information out of a file."""
    # The below file doesn't exist yet but it should be a csv with name,age as the headers then a few lines of names and age where appropiate
    # This is another way of processing a file, theres no real difference.
    with open("data2.csv", "r") as in_file:
        # The below line will read the frist line of a file and becuase we're not doing anything with it, is just a way of moving the start of the file down to ignore headers.
        # in_file.redline()
        for line in in_file:
            # This will split the line into a list where each item is sperated by a comma
            parts = line.strip().split(",")
            guitar_name = parts[0]  # This is the first item in the list
            # This is the second item in the list
            purchase_year = int(parts[1])
            price = (parts[2])  # This is the third item in the list
            print(f"You bought {guitar_name} in {purchase_year} for ${price}")
    # No need to close the file when using 'with' as it automatically closes the file when done.


second_do_this_now()


# def try_except_examples():
# """example of try and except in practice with user input from the lectures."""
# try:
#     number = int(input("Enter a number: "))
#     print(10 / number)
# except ValueError:
#     print("Invalid input, please enter a valid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except (
#     Exception
# ):  # This is a catch all for any other exceptions that may occur, it should always be the last except block
# print("An unexpected error occurred.")


# try_except_examples()
#
