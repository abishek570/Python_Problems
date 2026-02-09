s1 = str(input("Enter the first string: "))
s2 = str(input("Enter the second string: "))

count = 0 
for i in range(len(s1)):
    if s1[i] == s2[i]:
        pass
    else:
        count+=1

print(count)

