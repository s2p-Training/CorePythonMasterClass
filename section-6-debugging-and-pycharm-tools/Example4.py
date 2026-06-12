# 1. Static variable equivalent (global variable)
my_static_variable = "This is some static data"
data = 100000


# 2. Stack / function call examples
def foo1():
    print("This might cause error")


def foo2():
    foo1()
    print("Function call foo2")


def foo3():
    foo2()
    print("Function call foo3")


# 3. Methods with return values
def method1(x):
    square = x * x
    print("Value of x^2 :", square)
    return square


def method2(y):
    num = y
    print("Value of Y :", num)
    return num


def method3(z):
    cube = z * z * z
    print("Value of z^3 :", cube)
    return cube


def display_sum(x1, y1, z1):
    sum_val = method1(x1) + method2(y1) + method3(z1)
    print("sum :", sum_val)
    print(sum_val)  # similar to byteValue()


# Loop example
def display_some_numbers():
    print("displaySomeNumbers method called")

    for i in range(100):  # similar to Integer.MAX_VALUE
        print("i = ",i)
        pass  # intentionally empty

    print("Not Sure When This Line Will Execute")
    print("End of displaySomeNumbers method call ends")


# Variable mutation (watch in debugger)
def mutate_variable(isSingle, isRich, isLoyal, isSmart, doesGym, isJavaDeveloper):
    x = 0

    if isSingle:
        x += 2
    else:
        x += 10

    if isRich:
        x += 4
    else:
        x += 10

    if isLoyal:
        x += 5
    else:
        x += 10

    if isSmart:
        x += 7
    else:
        x += 10

    if doesGym:
        x -= 10
    else:
        x += 4

    if isJavaDeveloper:
        x += 3000
    else:
        x -= 100

    return x


# Main execution
if __name__ == "__main__":
    print("This will be printed")
    print("First Lesson On Debugging")

    mutate_variable(False, True, False, True, True, True)
    display_some_numbers()
    display_sum(12, 13, 14)