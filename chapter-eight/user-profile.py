# Exercise 8-13 User Profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile["first name"] = first
    profile["last name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("albert", "einstein",
                            location="princeton",
                            field = "physics")

user_profile_two = build_profile("lauren", "havrin",
                                location="highland park",
                                field = "nursing",
                                loves_pets = "yes",)

print(user_profile)
print(user_profile_two)
