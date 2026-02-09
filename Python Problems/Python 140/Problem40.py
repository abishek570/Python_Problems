## Sort the Names

n = int(input("Enter the count of names: "))

names = []
for i in range(n):
    name = str(input("Enter the name: "))
    names.append(name)
names.sort()
for j in names:
    a = j.capitalize()
    
    print(a)

string = str(input("Enter new names: "))

a = [i.capitalize() for i in string.split()]

for j in a:
    print(j)