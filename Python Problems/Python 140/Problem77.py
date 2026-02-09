s1 = map(str, input("Enter the string: ").split(" "))

s2 = []

## For removing duplicates and sorting in alphabetic order

for i in s1:
    if i not in s2:
        s2.append(i)

s2 = " ".join(sorted(s2))

print(s2)