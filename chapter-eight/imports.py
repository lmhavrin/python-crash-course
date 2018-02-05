# Exercise 8-16: Imports
# Using Exercise 8-10 Great Magicians

import practice_imports
practice_imports.say_hello("lauren")

from practice_imports import say_hello
say_hello("david")

from practice_imports import say_goodbye as sg
sg("david")

import practice_imports as pi
pi.say_goodbye("lauren")

from practice_imports import *
say_goodbye("Both of you")
