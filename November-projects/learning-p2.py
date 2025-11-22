import math
print(math.ceil(2.2))
print(math.log(2))

print("dwarf planet" == "dwarf planet")
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

print(type(5))
print(type(range(5)))
for x in "python":
    print(x)
number = 100
while number > 0:
    print(number)
    number //= 2
command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command)

def greet(name):
    print(f"Hi {name}")

def get_greeting(name):
    return f"Hi {name}"



message = get_greeting("Mosh")
file = open("learned.txt", "w")