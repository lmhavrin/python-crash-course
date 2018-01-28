# Exercise 7-3: Multiples of Ten

number = input("Give me a number please!")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of ten.")
elif number % 10 != 0:
    print(str(number) + " is not a multiple of ten.")


