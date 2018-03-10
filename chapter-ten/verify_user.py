# Exercise 10-13: Verfiy User
import json

#Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

# Refactoring- Breaking up code into a series of functions that have specific jobs

def get_stored_username():
    """Get stored username if available."""
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name?")
    filename = "username.json"
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        question = input("Is " + username + " the correct username? Print yes or no.")
        if question == "yes":
            print("Welcome back, " + username + "!")
        elif question == "no":
            username = get_new_username()
            print("We'll rememver you when you come back, " + str(username) + "!")
        else:
            print("Please enter yes or no")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + str(username) + "!")
        # I missed this else statement; Was trying to do a loop for user input

get_new_username()
greet_user()
