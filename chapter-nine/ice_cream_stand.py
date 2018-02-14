# Exercise 9-6: Ice Cream Stand

class Restaurant():
    """Defining basics of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints the two restaurant name and cuisine type"""
        print("The restaurant name is " + self.restaurant_name + " and the food type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        """Print if the restaurant is open"""
        print("The " + self.restaurant_name.title() + " is now open!")

    def set_number_served(self, customers):
        """Method that lets you set the number of customer that have been served"""
        self.number_served = customers
        print(str(customers) + " customers were served today.")

    def increment_number_served(self, customers):
        """Allows you to increment the number of customers served"""
        if customers >= self.number_served:
            self.number_served += customers
            print(str(self.number_served) + " total customers were served, and the count is continuing as the day progresses.")
        else:
            print("You cant roll back on customers served!")

class IceCreamStand(Restaurant):
    """Child Class of Restaurant"""
    def __init__(self, restaurant_name, cuisine_type, flavors=[]):
        """Initializes attributed of the parent class"""
        super().__init__(restaurant_name, cuisine_type)
        # Only initiating in super what is shared between two classes
        self.flavors = flavors

    def display_flavors(self):
        """Displays Ice cream flavors"""
        print("Here is a list of all the ice cream flavors: ")
        print(self.flavors)

ice_cream = IceCreamStand("Baskin Robbins", "Ice cream", ["vanilla", "chocolate", "strawberry"])

ice_cream.display_flavors()


