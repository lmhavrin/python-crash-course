# Exercise 5-8: Hello Admin

current_users = ["joebob", "bobbyjoe", "cat lady", "admin", "bicyclist"]

for user in current_users:
    print("\n-Hello " + user + "!")
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Welcome back " + user + ", thank you for logging in again.")
