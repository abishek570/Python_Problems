## KEY: Word in the string, VALUE: Count of each words in the string

inp = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

inp = inp.split(" ")

# a = []
# b = []
# for i in inp:
#     if i not in a:
#         a.append(i)
#         b.append(inp.count(i))


# for i in range(len(a)):
#     print(f"{a[i]}: {b[i]}")

a = []
for i in inp:
    if i not in a:
        a.append(i)

b = {}
for i in a:
    b[i] = inp.count(i)

b = sorted(b.items())

for key,value in b:
    print(f"{key}: {value}")