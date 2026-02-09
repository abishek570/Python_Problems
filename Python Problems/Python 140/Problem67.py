## Removing duplicates

y_dict = {
 'a': 10,
 'b': 10,
 'c': 10,
 'd': 10,
 'e': 10
}

s = set()

for i in y_dict.values():
    s.add(i)

print(list(s))