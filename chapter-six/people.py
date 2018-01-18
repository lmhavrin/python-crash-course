# Exercise 6-7: People

person_one = {
    "first_name": "honey",
    "last_name": "koch",
    "age": 27,
    "city": "massachusetts",
    }

person_two = {
    "first_name": "lauren",
    "last_name": "havrin",
    "age": 26,
    "city": "chicago",
    }

person_three = {
    "first_name": "david",
    "last_name": "basaraba",
    "age": 28,
    "city": "chicago",
    }

people = [person_one, person_two, person_three]

for person in people:
    persons_name = person["first_name"] + " " + person["last_name"]
    persons_age = person["age"]
    persons_city = person["city"]

    print("\n" + persons_name.title() + " is " + str(persons_age) +
        " years old and lives in " + persons_city.title() + ".")
