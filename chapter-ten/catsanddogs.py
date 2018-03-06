#Exercise 10-8 Cats and Dogs
# Exercise 10-9: Silent Cats and Dogs
# All you had to do for exercise 10-9 is put in a pass

def read_file(filename):
    """Reads a file and prints contents to screen"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        #print(filename + " is the file that is missing!")
        pass
    else:
        print(contents)

filename_one = "cats.txt"
read_file(filename_one)

filename_two = "dogs.txt"
read_file(filename_two)

filename_three = "rabbits.txt"
# not a file that exists
read_file(filename_three)