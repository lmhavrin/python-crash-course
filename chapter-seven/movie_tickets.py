# Exercise 7-5: Movie Tickets
prompt = "\nWelcome to the movies; What is your age?"
prompt += "\nEnter quit when finished."

while True:
    age = input(prompt)
    if age == "quit":
        break
    # break
    # if statment true loop will stop
    #if statement false loop will run rest of code

    age = int(age)

    if age < 3:
        print("You're ticket is free.")
    elif age >= 3 and age <= 12:
        print("The ticket is $10.")
    else:
        print("Your ticket is $15.")
