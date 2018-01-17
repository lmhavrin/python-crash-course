# Exercise 3-10: Every Function

languages = ["Spanish", "English", "Romanian", "French"]

print(languages[-1].title())
# using title() method on last item in list
# dont need to do as already in title case, just for practice

languages.append("German")
# using append() method to add new element to end of list
print(languages)

languages.insert(1, "Latin")
# using insert() method to add element to chosen index in list
print(languages)

del languages[2]
# using del statment to delete item from list
print(languages)

popped_language = languages.pop()
# using pop() method, saving it variable for later use,
# and printing list and popped_language
print(popped_language)
print(languages)

languages.remove("Latin")
# using remove() method to remove value with unknown position
print(languages)

languages.sort()
# using sort() method to permanently change order of list in
# alphabetical order
print(languages)

print(sorted(languages, reverse=True))
# using sorted function to temporarily reverse order
# not permanent

languages.reverse()
# using reverse() method to change order of list permanently
# in reverse
print(languages)

print(len(languages))
# using len() to determine length of list
