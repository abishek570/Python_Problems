## Curzon Number

s1 = int(input("Enter the number: "))

def curzon(s1):
    a = (2**s1)+1
    b = (2*s1)+1
    if (a%b==0):
        return True
    else:
        return False
    
print(curzon(s1))
