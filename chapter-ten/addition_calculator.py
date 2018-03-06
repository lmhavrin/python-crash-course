# Exercise 10-7: Addition Calculator
# Already wrapped code in while loop, pass should allow user
# to enter numbers even if they already made a mistake
# and entered text instead of number

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
        pass
    else:
        print(total)
