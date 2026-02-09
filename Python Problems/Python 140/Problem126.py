
def multiply_nums(string):
    a = string.split(",")
    mul = 1
    for i in a:
        mul*=int(i)
    return mul

print(multiply_nums("1, 2, 3, 4"))