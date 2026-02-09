def triangular_dot(ranging):
    a = 1
    for i in range(2,ranging+1):
        a+=i
    return a

print(triangular_dot(215))