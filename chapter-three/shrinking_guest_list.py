# Exercise 3-7: Shrinking Guest list
dinner_guest = ["Johnny Cash", "Elvis Presley", "Gandhi"]

print(dinner_guest[0] + ", Would you like to come to dinner?")
print("\n" + dinner_guest[1] + ", Would you like to come to dinner?")
print("\n" + dinner_guest[2] + ", Would you like to come to dinner?")

print("\n" + dinner_guest[2] + " can't make it to dinner.")

dinner_guest[2] = "George Washington"
print("\n" + dinner_guest[2] + ", Would you like to come to dinner?")
# and...would repeat dinner_guest[0] and dinner guest[2] again

print("\n" + "Update: Found a bigger dinner table, and I can invite three more guests!")

dinner_guest.insert(0, "John Lennon")
dinner_guest.insert(2, "John F Kennedy")
dinner_guest.insert(-1, "Andy Warhol")

for guest in dinner_guest:
    print("\n" + guest + ", Would you like to go to dinner?")

print("\n" + "New dinner table won't arrive in time for the dinner, and I can only invite two.")

uninvited_one = dinner_guest.pop()
print("\n" + uninvited_one + ", Sorry I cannot invite you to dinner anymore. :(")

uninvited_two = dinner_guest.pop()
print(uninvited_two + ", Sorry I cannot invite you to dinner anymore. :(")

uninvited_three = dinner_guest.pop()
print(uninvited_three + ", Sorry I cannot invite you to dinner anymore. :(")

uninvited_four = dinner_guest.pop()
print(uninvited_four + ", Sorry I cannot invite you to dinner anymore. :(")

print("\n" + dinner_guest[0] + " and " + dinner_guest[1] + "; You're still invited!")


print(dinner_guest)
del dinner_guest[0]

print(dinner_guest)

del dinner_guest[0]
print(dinner_guest)
