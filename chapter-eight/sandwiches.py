# Exercise 8-12 Sandwiches
def make_sandwich(*sandwich_items):
    print("Here is a summary of what your want in your sandwich: ")
    for items in sandwich_items:
        print("-" + items.title())

make_sandwich("lettuce", "tomato", "cheese", "bacon", "mayonaise")
make_sandwich("turkey", "bacon", "cheddar")
make_sandwich("ham", "cheese")
