# Exercise 10-4: Guest Book
filename = "guest_list.txt"

prompt = "What is your name?"

while True:
    name = input(prompt)

    if name != "quit":
        print("Welcome to the guest list " + name + "!")

        with open(filename, "a") as file_object:
            file_object.write(name + " was added to the guest list. \n")

    if name == "quit":
        break
        # Had trouble removing quit from lists; Correct formatting
        # nesting & if statements resolved that