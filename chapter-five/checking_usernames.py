# Exercise 5-10: Checking Usernames

current_users = ["joebob", "bobbyjoe", "cat lady", "admin", "bicyclist"]

new_users = ["JOEBOB", "cat lady", "beatin4u", "whatever", "lotsofcats"]

for new_user in new_users:
    if new_user in current_users:
        print("\n-Please enter a new username, this is in use.")
    else:
        print("\n-This username is available!")
# basically, in for loop comparing two lists
# loop through list with placeholder
#user placeholder to compare to second list