print("FUNCTIONS")


def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age) + ".")


say_hi("Bruno", 28)
say_hi("Deborah", 35)


def cube(num):
    return num * num * num


result = cube(4) + 2
print(str(result) + " is you result.")
