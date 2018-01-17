# Exercise 4-10: Slices
cubes = [value**3 for value in range(1,11)]

print("The first three items in the list are: " + "\n" + str(cubes[0:3]))
# as with range() function, python stops one item before the second index you specify

print("Three items from the middle of the list are: " + "\n" + str(cubes[4:7]))

print("The last three items in the list are: " + "\n" + str(cubes[-3:]))
