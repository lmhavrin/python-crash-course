# Exercise 9-12: Multiple Modules
from user import User
from privileges import Admin, Privileges

admin_three = Admin("david", "basaraba", "non-binary", 28, "highland park")

admin_three_p = [
    "can ban user",
    "can edit post",
    "can delete post",
    ]

admin_three.privileges.privileges = admin_three_p

admin_three.privileges.show_privileges()