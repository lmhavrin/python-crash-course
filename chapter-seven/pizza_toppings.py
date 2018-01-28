# Exercise 7-4: Pizza Toppings
prompt = "Please enter all the pizza toppings you like."
prompt += "\nEnter quit when you have finished listing toppings."

pizza_topping = []

active = True
while active:
    topping = input(prompt)
    pizza_topping.append(topping)

    if topping == "quit":
        active = False
    else:
        print("\nAdding " + topping + " to your list.")

