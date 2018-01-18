# Exercise 6-1: Person

person_one = {
    "first_name": "honey",
    "last_name": "koch",
    "age": 27,
    "city": "massachusetts",
    }

for person in person_one:
    persons_name = person_one["first_name"] + " " + person_one["last_name"]
    persons_age = person_one["age"]
    persons_city = person_one["city"]

print(persons_name.title() + " is " + str(persons_age) +
    " years old. And lives in " + persons_city.title() + ".")
