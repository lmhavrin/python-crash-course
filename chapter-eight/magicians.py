# Exercise 8-9: Magicians
magicians = ["bob", "larry", "joe", "bill"]

def show_magicians(magicians):
    """Goes through a list of magicians and prints them"""
    # edited for styling functions 8-17
    for magician in magicians:
        print("-" + magician.title())

show_magicians(magicians)
