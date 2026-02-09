## Method -- 1

a = int(input())

b = len(str(a))
if a == 1 or a == 7:
    print("It is a happy number")

elif a >1:
    while a>1:
        sums = 0
        temp = a
        while b>0 and temp>0:
            dig=temp%10
            sums+=dig**b
            temp//=10 
        a = sums
        if a ==1:
            print("It is a happy number")
            break
    else:
        print("It is not a happy number")

## Method -- 2

def is_happy_number(num):
    seen = list() # To store previously seen numbers
    
    while num != 1 and num not in seen:
        seen.append(num)
        num = sum(int(i) ** 2 for i in str(num))
        print(seen)
    return num == 1

    # Test the function with a number
num = int(input("Enter a number: "))
if is_happy_number(num):
    print(f"{num} is a Happy Number")
else:
    print(f"{num} is not a Happy Number")