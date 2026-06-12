
def foo1():
    print("Statement-A")
    print("Statement-B")
    print("Statement-C")

def foo2():
    print("Statement-1")
    print("Statement-2")

def foo3():
    print("Start Of foo3")
    print("Statement-a")
    print("Statement-b")
    print("Statement-c")
    print("Statement-d")
    print("End Of foo3")

if __name__ == '__main__':
    print("Start Of Program")
    foo2()
    foo1()
    foo3()
    print("End Of Program")