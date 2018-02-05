# Exercise 8-14: Cars
def car_info(manufacturer, model, **other_info):
    """Stores info about a car in a dictionary"""
    car = {}
    car["Manufacturer"] = manufacturer
    car["Model"] = model
    for key, value in other_info.items():
        car[key] = value
    return car

car_one = car_info("Subaru", "WRX", awd=True, color= "blue")
car_two = car_info("Saturn", "sl2", awd=False, color= "yellow")

print(car_two)
print(car_one)
