"""Making a list of lines from a file"""

filename = "py_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

"""Reading line by line"""

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())
#         # print line adds new line and txt object adds new line

"""Reading an entire file"""

# with open("py_digits.txt") as file_object:
#     contents = file_object.read()
#     print(contents.rstrip)
