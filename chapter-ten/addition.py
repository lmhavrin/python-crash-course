# Exercise 10-6: Addition
prompt = "Give me two numbers, and I will add them"
prompt = "Enter q to quit"

while True:
    number_one = input("First Number: \n")
    if number_one == "quit":
        break
    number_two = input("Second Number: \n")
    if number_two == "quit":
        break

    try:
        total = int(number_one) + int(number_two)
    except ValueError:
        if number_one != int(number_one) or number_two != int(number_two):
            print("Please provide a number")
    else:
        print(total)
