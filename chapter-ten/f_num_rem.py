# Exercise 10-12: Favorite Number Remembered
import json

def favorite_number():
    """Prompts for a users favorite number"""
    while True:
        f_number = input("What is your favorite number? ")
        prompt = print("Enter q to quit.")
        if f_number == "q":
            break
        else:
            try:
                f_number = int(f_number)
                filename = "favorite_num.json"
                with open(filename, "w") as f_obj:
                    json.dump(f_number, f_obj)
            except ValueError:
                print("Please enter a number or 'q' to quit.")


def read_number():
    """Get stored number if available"""
    try:
        filename = "favorite_num.json"
        with open(filename) as f_obj:
            number = json.load(f_obj)
            print("I know your favorite number, its " + str(number) + "!")
    except FileNotFoundError:
        print("This file was not found..")


favorite_number()
read_number()

# same code, combined into two files per exercise 10-12
