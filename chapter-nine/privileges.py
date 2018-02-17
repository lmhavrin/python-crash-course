from user import User

# Exercise 9-8: Privileges

# class User():
#     """Making a brief user profile"""

#     def __init__(self, first_name, last_name, gender, age, hometown):
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.gender = gender.title()
#         self.age = age
#         self.hometown = hometown.title()

#     def describe_user(self):
#         """Summarizes user information"""

#         print("\nUser information for " + self.first_name.title() + " " + self.last_name.title() + " is as follows:")
#         print("\n-" + self.gender.title() + "\n-" + str(self.age) + "\n-" + self.hometown.title())

#     def greet_user(self):
#         """Prints a personalized greeting to the user"""

#         print("Welcome, " + self.first_name.title() + " " + self.last_name.title() + "!")

class Admin(User):
    """Creating a child class of User"""

    def __init__(self, first_name, last_name, gender, age, hometown):
        """Initializes attributes of the parent class"""
        super().__init__(first_name, last_name, gender, age, hometown)
        self.privileges = Privileges()
        print(first_name.title() + " " + last_name.title() + " is an administrator.")

class Privileges():
    """Creating a class that stores admins privileges"""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """Lists the administrators set of privileges"""
        print("The set of privileges for this administrator are as follows: ")
        if self.privileges:
            """I forgot if and else statment"""
            for privilege in self.privileges:
                print("-" + str(privilege.title()))
        else:
            print("This user has no privileges.")

admin_one = Admin("lauren", "havrin", "female", 27, "murrysville")

admin_one_p = [
    "can add user",
    "can ban user",
    "can delete post",
    "can add post"
    ]

admin_one.privileges.privileges = admin_one_p

admin_one.privileges.show_privileges()



