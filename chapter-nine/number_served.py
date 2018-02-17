# Exercise 9-4: Number Served

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

restaurant = Restaurant("Casa Bonita", "Mexican")
print("This restaurant has served " + str(restaurant.number_served) + " customers.")

restaurant.number_served = 20

print("This restaurant has now served " + str(restaurant.number_served) + " customers.")

restaurant.set_number_served(100)

restaurant.increment_number_served(1000)