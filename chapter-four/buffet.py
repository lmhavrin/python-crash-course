# Exercise 4:13 Buffet

buffet = ("chicken", "fish", "potatoes", "green beans", "apple pie")

print("This restaurant buffet table offers: ")
for item in buffet:
    print("-" + item.title())

# Modifying a tuple does not work
#buffet[0] = "steak"

buffet = ("steak", "fish", "potatoes", "asparagus", 'apple pie')
print("\n This restaurant buffer table now serves: ")
for value in buffet:
    print("-" + value.title())

# you cannot modify a tuple, but can assign a new variable that holds a tuple,
# and modify the list that way

# style guide
# four spaces per indent level
# each line lesss than 80 characters

# 4-14 and 4-15 code REVIEWED