## Binary number calculator

n1 = int(input())

a = []
temp = n1
while temp>0:
    dig = temp%2
    a.append(dig)
    temp = temp//2
a.reverse()
b = []
for i in a:
    b.append(str(i))
b = "".join(b)

if b == bin(n1)[2:]: # It has a prefixed string "0b"
    print(True)
else:
    print(False)


## Octal number calculator

a = []
temp = n1
while temp>0:
    dig = temp%8
    a.append(dig)
    temp = temp//8
a.reverse()
b = []
for i in a:
    b.append(str(i))
b = "".join(b)

if b == oct(n1)[2:]: # It has a prefixed string "0o"
    print(True)
else:
    print(False)

## Hexadecimal calculator 

print(hex(n1)[2:])

