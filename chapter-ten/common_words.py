# Exercise 10-10: Common Words

filename = "alice.txt"
# used gutenburg for txt file

def find_word(word):
    """Finds a word in a text file"""
    with open(filename) as file_object:
        contents = file_object.read()
        words = contents.lower().split()
        word_count = words.count(word)
    print(word_count)

find_word("alice")
find_word("the")
find_word("cat")