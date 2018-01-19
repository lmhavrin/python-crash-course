# Exercise 6-11: Cities

cities = {
    "chicago": {
        "country": "United States",
        "approximate population": "2.705 million",
        "fact": "among the largest cities in the US",
        },
    "manhattan": {
        "country": "united states",
        "approximate population": "1.645 million",
        "fact": "it is the heart of the 'big apple'",
        },
    "boston": {
        "country": "united states",
        "approximate population": 673184,
        "fact": "people love dunkin donuts"
        },
    }

for country, population in cities.items():
    print(country.title() + ":")
    print("\t" + population["country"].title() + " is the country this city resides in.")
    print("\t" + "A weird fact about " + country.title() + " is " + population["fact"] + " with a population of " +
        str(population["approximate population"]) + ".")
