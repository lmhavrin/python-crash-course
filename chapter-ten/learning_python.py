# Exercise 10-1 Learning Python

filename = "learning_python.txt"

# Program that reads the file and prints out what I wrote three times

for _ in range(0,3):
    with open("learning_python.txt") as python_summary:
        for line in python_summary:
            print(line.strip())
    print('')

print("Reading in the entire file: ")
with open(filename) as file_object:
    lines = file_object.read()
    print(lines)

print("Looping over file object: ")
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.strip())

print(" ")

print("Storing lines in a list: ")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())