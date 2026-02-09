def custom_list(n):
    a = []
    for i in range(1,n+1):
        if i%4 == 0:
            a.append(i*10)
        else:
            a.append(i)
    return a

print(custom_list(25))

sorted