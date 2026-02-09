## Harshad Number

a = int(input())
leng = len(str(a))
c = str(a)
b = 0
for i in range(leng):
    b+=int(c[i])

if a%b==0:
    print("It is a harshad number")
else:
    print("Its not a harshad number")