# Exercise 7-10: Dream Vacation
responses = {}

active = True

while active:
    user_name = input("Welcome to dream vacation poll! What is your name?")
    user_dream_vacation = input("If you could visit one place in the world, where would you go?")

    responses[user_name] = user_dream_vacation

    another_user = input("Would you like to let another person enter their name and dream vacation? Reply no to quit; Otherwise say yes to poll")

    if another_user == "no":
        active = False

print("The results of the poll are: ")
for user_name, user_dream_vacation in responses.items():
    print(user_name.title() + " would like to visit " + user_dream_vacation.title() + "!")
