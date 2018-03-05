# Exercise 10-5: Programming Poll

filename = "program_poll.txt"

prompt = "Why do you like programming?"

while True:
    question = input(prompt)

    if question != "quit":
        print(question)

        with open(filename, "a") as file_object:
            file_object.write(question + "\n")

    if question == "quit":
        break
