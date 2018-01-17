# Exercise 4-11: My Pizzas, Your Pizzas

favorite_pizza = ["green peppers", "jalepeno", "mushroom"]

friend_pizza = ["green peppers", "jalepeno", "mushroom"]

favorite_pizza.append("pineapple")
print(favorite_pizza)

friend_pizza.insert(2, "olive")
print(friend_pizza)

print("\n My favorite pizzas are: ")
for pizza in favorite_pizza:
    print("-" + pizza.title())

print("\n My friends favorite pizzas are: ")
for f_pizza in friend_pizza:
    print("-" + f_pizza.title())
