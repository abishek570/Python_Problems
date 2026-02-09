def square_digits(s1):
    leng = len(str(s1))
    temp = s1
    new_str = ""

    while temp>0:
        rem = temp%10
        new_str+=str(rem**2)
        temp//=10

    return int(new_str)

print(square_digits(9119)) 