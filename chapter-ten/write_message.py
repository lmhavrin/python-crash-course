# Writing to an empty file

filename = "programming.txt"

with open(filename, "w") as file_object:
    file_object.write("I love programming! \n")
    # dont open a file in write mode if file does exist
    # will erase the file
    # can only write strings in a file

# Appending a file practice

with open(filename, "a") as file_object:
    file_object.write("I also love finding meaning in large databases. \n")
    file_object.write("I love creating apps that can run in a browser. \n")