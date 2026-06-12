# Boolean Type Conversion Method
if __name__ == '__main__':

    b_flag1 = bool("Hello")
    print(b_flag1)

    b_flag2 = bool(0)
    print(b_flag2)

    b_flag3 = bool(1)
    print(b_flag3)

    b_flag4 = bool()
    print(b_flag4)

    b_flag5 = bool(None)
    print(b_flag5)

    b_flag6 = bool("False") # LoL This Returns True XD
    print(b_flag6)

    b_flag7 = bool(12)
    print(b_flag7)

    b_flag8 = bool(12+3j)
    print(b_flag8)

    b_flag9 = bool("") # Returns False
    print(b_flag9)