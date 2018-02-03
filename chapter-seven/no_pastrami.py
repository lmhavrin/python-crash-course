# Exercise 7-9: No Pastrami
sandwich_orders = ["turkey", "pastrami", "roast beef", "pastrami", "chicken", "pastrami", "BLT", "ham", "pastrami"]
finished_sandwiches = []

print("The deli has run out of pastrami sandwiches.")

while sandwich_orders:
    while "pastrami" in sandwich_orders:
        sandwich_orders.remove("pastrami")
    making_sandwich = sandwich_orders.pop()

    print("I made your " + making_sandwich + " sandwich.")
    finished_sandwiches.append(making_sandwich)

print("\n Here are the list of sandwiches finished: ")
for sandwich in finished_sandwiches:
    print("-" + sandwich.title())