# Exercise 6-5 Rivers

rivers = {
    "nile": "egypt",
    "amazon": "south america",
    "yangtze": "china",
    }

print("Name of three famous rivers around the world: ")

for river in rivers.keys():
    print("-" + river.title())

print("\nWhere these three famous rivers are located: ")

for name in rivers.values():
    print("-" + name.title())
    # keys and values at the end of dictionary

for key, value in rivers.items():
    print("\nThe " + key.title() + " runs in " + value.title() + ".")
