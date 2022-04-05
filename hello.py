print("WORDS AND SHAPES")

print("Hello World")

print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")

print("    /\ ")
print("   /  \ ")
print("  /    \ ")
print(" /      \ ")
print("/________\ ")
print("\n")

print("VARIABLES")

character_name = "Bruno"
character_age = 28
print("There once was a man named " + character_name + ",")
print("he was " + str(character_age) + " years old.")
character_name = "Nobru"
print("He really liked the name " + character_name + ",")
print("but didn't like being " + str(character_age) + ".")

print("\n")

print("STRINGS")

phrase = "\"Giraffe Academy\" "
print(phrase + "is cool")
print(phrase.lower())  #lowercase
print(phrase.upper())  #uppercase
print(phrase.upper().isupper())   #boolean
print(len(phrase))   #lenght
print(phrase[0])   #select specific element
print(phrase.index("ffe"))    #index of the element
print(phrase.replace("Giraffe", "Elephant"))
print(phrase.replace("f", "t"))

print("\n")

print("NUMBERS")

print(2)
print(-2.0987)
print(3 * (6 / 2))
print(10 % 3)

my_num = -5
print(my_num)
print(str(my_num) + " is my favorite number")
print(abs(my_num))  #absolute num
print(pow(4, 6))   #power (potência)
print(max(4, 6))   #show max num
print(min(4, 6))   #show min num
print(round(3.4))  #round num

from math import *

print(floor(3.7))    #round num below
print(ceil(3.3))     #round num above
print(sqrt(36))      #square root

print("\n")

print("LISTS")

friends = ["Gil", "Ian", "Guilherme", "Gil", "Bernardo", "Sérgio"]
print(friends[1:])
print(friends[1:3])
friends[-2] = "Caio"
print(friends[0] + " and " + friends[-2] + " are my closest friends")

friends.append("Josimar")
print(friends)
friends.insert(1, "Karen")
print(friends)
friends.remove("Josimar")
print(friends)
friends.pop()
print(friends)
print(friends.index("Guilherme"))
print(friends.count("Gil"))
friends.sort()
print(friends)
friends.reverse()
print(friends)
friends2 = friends.copy()
print(friends2)

lucky_numbers = [13, 5, 7, 11, 49]
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
print(friends + lucky_numbers)
friends.extend(lucky_numbers)
print(friends)
friends.clear()
print(friends)

print("\n")

print("TUPLES")

coordinates = (4, 5)
print(coordinates[-1])

coordinates = [(4, 5), (6, 7), (50, 55)]
print(coordinates[2])
print("\n")

print("FUNCTIONS")


def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age) + ".")


say_hi("Bruno", 28)
say_hi("Deborah", 35)


def cube(num):
    return num * num * num


result = cube(4) + 2
print(str(result) + " is you result.")
print("\n")

print("IF STATEMENTS")

is_male = False
is_tall = True

if is_male or is_tall:
    print("You are either a male or tall or both")
else:
    print("You are neither a male nor tall")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are tall, but not a male")
else:
    print("You are neither male nor tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(3, 5, 4))

print("\n")

print("DICTIONARIES")

monthConversions = {
    "Jan": "January",
    2: "February",
    "Mar": "March",
    "Apr": "April",
    5: "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get(2))
print(monthConversions.get("Luv", "Not a valid key"))