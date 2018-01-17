# Exercise 4-12: More Loops
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
for food in my_foods:
    print("-" + food.title())

print("\n My friends favorite foods are: ")
for value in friend_foods:
    print("-" + value.title())

