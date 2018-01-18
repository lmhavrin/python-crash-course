# Exercise 5-2: More Conditional Tests

# checking or equality with strings

wine = "red"
if wine == "red":
    print("I would like some red wine!")
    print(wine == "red")

#checking for inequality with strings

ice_cream = "vanilla"
if ice_cream != "chocolate":
    print("\nSorry, we only have vanilla ice cream...")

# tests using upper() function

car = "BMW"
if car == 'bmw'.upper():
    print(car)

# tests using lower() function

name = "Lauren Havrin"
print(name.lower() == "Lauren Havrin")

# numerical tests for equality inequality, greater and less than
age = 27

if age < 10:
    print("You are less than 10 years old.")
elif age >= 25 and age <= 30:
    print("\nYou are between ages 25-30.")

#Using an and, or keyword and testing whether an item is in, not in a list

dogs = ["dalmation", "terrier", "boxer", "poodle"]
if "dalmation" in dogs:
    print("\n-Dalmation is in the list")
if "goldendoodle" not in dogs:
    print("-Sorry no goldendoodles today")
if "dalmation" or "terrier" in dogs:
    print("-Both are on the list!")
if "boxer" and "terrier" in dogs:
    print("-We have both boxer and terrier on the list!")
