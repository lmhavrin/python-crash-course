# Exercise 10-11: Favorite Number
import json

# ORIGINAL CODE

# def favorite_number():
#     """Prompts for a users favorite number"""
#     while True:
#         try:
#             f_number = int(input("What is your favorite number?"))
#             prompt = print("Enter q to quit")
#             if f_number == "q":
#                 break
#         except ValueError:
#             print("Please enter a number...")
#         filename = "favorite_num.json"
#         with open(filename, "w") as f_obj:
#             json.dump(f_number, f_obj)

# favorite_number()

# tried to do an if, elif, and else statment but did not work that way
# added way too much too soon

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

favorite_number()
