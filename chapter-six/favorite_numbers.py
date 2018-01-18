# Exercise 6-2: Favorite Numbers

favorite_numbers = {
    "david": [4, 7, 10, 12],
    "lauren": [25, 18, 23, 14],
    "kim": [5, 23, 19, 74],
    "sarah": [20, 21, 22],
    "bambi": [3],
    }

for name, numbers in favorite_numbers.items():
    print(name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + str(number))
