# Exercise 8-11: Unchanged Magicians
def show_magicians(magicians):
    for magician in magicians:
        print("-" + magician.title())

def make_great(magicians):
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_m = "The great " + magician
        great_magicians.append(great_m)

    for great in great_magicians:
        magicians.append(great)

    return magicians

magicians = ["bob", "larry", "joe", "bill"]
show_magicians(magicians)

great_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)
