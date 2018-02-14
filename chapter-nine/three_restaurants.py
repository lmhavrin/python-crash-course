# Exercise 9-2: Three Restaurants
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

# Create three different instances from the class, and call describe_restaurant() for each instance

restaurant_two = Restaurant("Noodle Bar", "Asain Fusion")
restaurant_three = Restaurant("So Gong Dong", "Korean")
restaurant_four = Restaurant("Chipolte", "Fast food")

restaurant_two.describe_restaurant()
restaurant_three.describe_restaurant()
restaurant_four.describe_restaurant()
