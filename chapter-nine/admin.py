# Exercise 9-7: Admin

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

class Admin(User):
    """Creating a child class of User"""

    def __init__(self, first_name, last_name, gender, age, hometown, privileges=[]):
        """Initializes attributes of the parent class"""
        super().__init__(first_name, last_name, gender, age, hometown)
        self.privileges = privileges

    def show_privileges(self):
        """Lists the administrators set of privileges"""
        print("The set of privileges for the administrator are as follows: ")
        for privilege in self.privileges:
            print("-" + str(privilege.title()))

admin = Admin("lauren", "havrin", "female", 27, "murrysville", ["can add user", "can ban user", "can delete post", "can add post"])

admin.show_privileges()
