# Exercise 9-5: Login Attempts

class User():
    """Making a brief user profile"""

    def __init__(self, first_name, last_name, gender, age, hometown):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.hometown = hometown
        self.login_attempts = 0

    def describe_user(self):
        """Summarizes user information"""

        print("\nUser information for " + self.first_name.title() + " " + self.last_name.title() + " is as follows:")
        print("\n-" + self.gender.title() + "\n-" + str(self.age) + "\n-" + self.hometown.title())

    def greet_user(self):
        """Prints a personalized greeting to the user"""

        print("Welcome, " + self.first_name.title() + " " + self.last_name.title() + "!")

    def increment_login_attempts(self):
        """Increments login attempts by 1"""
        self.login_attempts += 1
        print("User attempted to login " + str(self.login_attempts) + " time[s].")

    def reset_login_attempts(self):
        """Resets login attempts to zero."""
        self.login_attempts = 0
        print("Login attempt reset to: " + str(self.login_attempts))

user_one = User("lauren", "havrin", "female", 27, "murrysville")

user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.reset_login_attempts()
user_one.increment_login_attempts()
