# Exercise 6-8: Pets

animal_one = {
    "name": "freddy",
    "type": "dog",
    "owner": "patricia",
    }

animal_two = {
    "name": "ratha",
    "type": "cat",
    "owner": "david",
    }

animal_three = {
    "name": "neo",
    "type": "cat",
    "owner": "patrick",
    }

pets = [animal_one, animal_two, animal_three]

for pet in pets:
    print("\n" + pet["name"].title() + " is a " + pet["type"] +
        ", that lives with " + pet["owner"].title() + ".")
