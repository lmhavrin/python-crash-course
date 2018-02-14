# Exercise 9-1: Restaurant

class Restaurant():
    """Defining basics of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the two restaurant name and cuisine type"""
        print("The restaurant name is " + self.restaurant_name + " and the food type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        """Print if the restaurant is open"""
        print("The " + self.restaurant_name.title() + " is now open!")

restaurant_one = Restaurant("Casa Bonita", "Mexican")

print("-" + restaurant_one.restaurant_name)
print("-" + restaurant_one.cuisine_type)

restaurant_one.describe_restaurant()
restaurant_one.open_restaurant()

# Remember to use the self.attribute in all methods
