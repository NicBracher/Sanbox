"""This is a basic prgram to demonstrate how python is used."""

def main():
    name = input("Enter your name: ")
    print("Hello", name)
    age = int(input("Enter your age: "))
    print("You will be", age + 1, "next year.")
    print(f"You are currently {age} years old and your name is {name} and you are the coolest!!!.")
    user_number = input("Choose a number between 0 and 100 and I will count to that number for you: ")
    for i in range(0, int(user_number) + 1):
        print(i, end=' ')


main()