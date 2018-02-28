# Exercise 10-3: Guest

filename = "guest.txt"

with open("guest.txt", "a") as file_object:
    file_object.write(input("Whats your name?"))
