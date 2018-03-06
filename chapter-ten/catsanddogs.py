# Exercise 10-8: Cats and Dogs
def read_file(filename):
    """Reads a file and prints contents to screen"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print(filename + " is the file that is missing!")
    else:
        print(contents)

filename_one = "cats.txt"
read_file(filename_one)

filename_two = "dogs.txt"
read_file(filename_two)

filename_three = "rabbits.txt"
# not a file that exists
read_file(filename_three)