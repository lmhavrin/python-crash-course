# Exercise 8-17: Styling Functions

# Exercise 8-9: Magicians
magicians = ["bob", "larry", "joe", "bill"]

def show_magicians(magicians):
    """Goes through a list of magicians and prints them"""
    print("Here is a list of magicians: ")
    for magician in magicians:
        print("-" + magician.title())

show_magicians(magicians)

