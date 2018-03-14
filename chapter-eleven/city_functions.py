# Exercise 11-1: City, Country & Exercise 11-2: Population

def city_country(city, country, population=''):
    """Returns a neatly formatted city, country"""
    if population:
        city_count = city.title() + ", " + country.title() + " -Population: " + str(population)
    else:
        city_count = city.title() + ", " + country.title()
    return city_count
