lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

for i in range(lower_limit, upper_limit):
    length = len(str(i))
    sum = 0
    temp = i
    while temp>0:
        dig = temp%10
        sum+=dig**length
        temp//=10
    if i == sum:
        print("Yes", i)
    