# Exercise 6-9: Favortie Places
favorite_places = {
    "david": ["netherlands", "romania", "germany"],
    "lauren": ["bahamas", "chicago"],
    "bob": ["pennsylvania"]
    }
# EVERYTHING MUST BE IN LIST FORMAT EVEN IF ONE ITEM
#INSIDE DICTIONARY
for person, places in favorite_places.items():
    print(person.title() + " 's favorite places are: ")
    for place in places:
        print("\t-" + place.title())
# MUST LOOP in a loop to get values
