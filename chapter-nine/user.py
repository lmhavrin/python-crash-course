# 9-12 Multiple Modules

class User():
    """Making a brief user profile"""

    def __init__(self, first_name, last_name, gender, age, hometown):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.gender = gender.title()
        self.age = age
        self.hometown = hometown.title()

    def describe_user(self):
        """Summarizes user information"""

        print("\nUser information for " + self.first_name.title() + " " + self.last_name.title() + " is as follows:")
        print("\n-" + self.gender.title() + "\n-" + str(self.age) + "\n-" + self.hometown.title())

    def greet_user(self):
        """Prints a personalized greeting to the user"""

        print("Welcome, " + self.first_name.title() + " " + self.last_name.title() + "!")