# Exercise 6-6: Polling

favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
    "lauren": "python",
    "david": "ruby",
    }

take_poll = ["mark", "will", "david", "lauren", "joe", "stephanie"]

for people in take_poll:
    if people in favorite_languages:
        print("Thank you for taking the poll.")
    else:
        print("Please take the poll.")
