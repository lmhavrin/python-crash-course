# Exercise 7-6: Three Exits
# Movie Ticket Revamped
prompt = "\nWelcome to the movies, what is your age?"
prompt += "\n Enter quit when finished."

active = True
while active:
    age = input(prompt)

    if age == "quit":
        active = False
        break

    age = int(age)

    if age < 3:
        print("You're ticket is free.")
    elif age >= 3 and age <= 12:
        print("The ticket is $10.")
    else:
        print("Your ticket is $15.")
