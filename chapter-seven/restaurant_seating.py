# Exercise 7-2: Restaurant Seating

group = input("How many people are in your dinner group?")
group = int(group)

if group > 8:
    print("You will have to wait for a table for a party of " + str(group) + ".")
else:
    print("Your table is ready!")