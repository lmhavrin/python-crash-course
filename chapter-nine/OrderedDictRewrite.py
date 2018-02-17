# Exercise 9-13: OrderedDict Rewrite

from collections import OrderedDict

glossary = OrderedDict()

#for keys,values in glossary.items():
#   print(keys + ":\n" + values)

glossary["sorted()"] = "lists alphabetical order but doesnt permanently effect list"
glossary["keys()"] = "method that returns list of all keys"
glossary["items()"] = "method that returns a list of key-value pairs"
glossary["str()"] = "method that represents non string values as strings"
glossary["sort()"] = "changes the order of a list permanently"

for keys, values in glossary.items():
    print("\n" + keys + ":\n" + values)

