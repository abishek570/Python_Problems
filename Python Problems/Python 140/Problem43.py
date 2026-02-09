## Disarium Number

n = int(input("Enter a number: "))

temp = n
ord = len(str(n))
sums = 0
while (ord>0) and temp>0:
    dig = temp%10
    sums+=dig**ord
    temp//=10
    ord-=1
    
if sums == n:
    print(f"{sums} is a Disarium number")
else:
    print(f"{n} is not a Disarium number")