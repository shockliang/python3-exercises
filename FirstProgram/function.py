

def my_function(str1, str2):
    print(str1)
    print(str2)


my_function("This is arg 1", "This is second arg")


def print_something(name="Someone", age="Unknow"):
    print("My name is", name, "and my age is", age)


print_something(None, 27)

print_something(age=35, name="Shock")


def print_people(*people):
    for person in people:
        print("This person is", person)


print_people("Shock", "David", "Jack", "Kingsman")


def do_math(num1, num2):
    return num1 + num2


result = do_math(5, 7)
result2 = do_math(11, 12)

print("First result", result, ", Second result", result2)
