# Exercise 6-3: Glossary

glossary = {
    "title()": "capitalizes first letter",
    "del": "deletes something from list permanently",
    "not in": "checks if something is in a list",
    "lower()": "lowercases everything",
    "upper()": "uppercases everything",
    }

for keys,values in glossary.items():
    print(keys + ":\n\t" + values)
# .items() a dictionary function that returns copy of key value pairs
#iteritems() another version of this
# can do for item in key, print item value or vice versa

