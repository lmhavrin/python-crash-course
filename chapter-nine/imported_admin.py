# Exercise 9-11 Imported Admin

# Imported from Exercise 9-8 Privileges

from privileges import User, Admin, Privileges

admin_two = Admin("david", "havrin", "male", "24", "lake forest")

admin_two_p = [
    "can ban user"
    ]

admin_two.privileges.privileges = admin_two_p

admin_two.privileges.show_privileges()
