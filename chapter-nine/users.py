# Exercise 9-3: Users

class User():
    """Making a brief user profile"""

    def __init__(self, first_name, last_name, gender, age, hometown):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.hometown = hometown

    def describe_user(self):
        """Summarizes user information"""

        print("\nUser information for " + self.first_name.title() + " " + self.last_name.title() + " is as follows:")
        print("\n-" + self.gender.title() + "\n-" + str(self.age) + "\n-" + self.hometown.title())

    def greet_user(self):
        """Prints a personalized greeting to the user"""

        print("Welcome, " + self.first_name.title() + " " + self.last_name.title() + "!")

user_one = User("lauren", "havrin", "female", 27, "murrysville")
user_one.describe_user()
user_one.greet_user()

user_two = User("david", "havrin", "male", 23, "lake forest")
user_two.describe_user()
user_two.greet_user()
