## Checking whether it is a binary string

inp_str = str(input("Enter the String: "))

for i in inp_str:
    if int(i)>1:
        a = False
        break
else:
    a = True

if a == True:
    print("True")
else:
    print("False")