# Exercise: 7-8 Deli
# A for loop is useful for looping through a list
# A while loop is useful for looping through a list AND MODIFYING IT

sandwich_orders = ["turkey", "roast beef", "chicken", "BLT", "ham"]
finished_sandwiches = []

while sandwich_orders:
    making_sandwich = sandwich_orders.pop()

    print("I made your " + making_sandwich + " sandwich.")
    finished_sandwiches.append(making_sandwich)

print("\n Here are the list of sandwiches finished: ")
for sandwich in finished_sandwiches:
    print("-" + sandwich.title())