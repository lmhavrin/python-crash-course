# Exercise 6-4: Glossary Two

glossary = {
    "title()": "capitalizes first letter",
    "del": "deletes something from list permanently",
    "not in": "checks if something is in a list",
    "lower()": "lowercases everything",
    "upper()": "uppercases everything",
    }

#for keys,values in glossary.items():
#   print(keys + ":\n" + values)

glossary["sorted()"] = "lists alphabetical order but doesnt permanently effect list"
glossary["keys()"] = "method that returns list of all keys"
glossary["items()"] = "method that returns a list of key-value pairs"
glossary["str()"] = "method that represents non string values as strings"
glossary["sort()"] = "changes the order of a list permanently"

for keys, values in glossary.items():
    print("\n" + keys + ":\n" + values)
