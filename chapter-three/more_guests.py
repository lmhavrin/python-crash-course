# Exercise 3-6: More Guests
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

