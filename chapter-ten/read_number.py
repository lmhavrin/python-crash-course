# Exercise 10-11 Favorite Number CTD
import json

def read_number():
    """Get stored number if available"""
    try:
        filename = "favorite_num.json"
        with open(filename) as f_obj:
            number = json.load(f_obj)
            print(number)
    except FileNotFoundError:
        print("This file was not found..")

read_number()