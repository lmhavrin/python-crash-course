# Exercise 10-2: Learning C

filename = "learning_python.txt"

with open(filename) as f:
    lines = f.readlines()

# Originally put empty string oustide of loop than assigned new string in loop
# so new modified list could be accessed outside of a loop

for line in lines:
    line = line.strip()
    print(line.replace("python", "C"))
