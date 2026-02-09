## Sum of values in a dictionary

y_dict = {
 'a': 10,
 'b': 10,
 'c': 10,
 'd': 10,
 'e': 10
}

sums = 0
for i in y_dict.values():
    sums=sums+i

print("Sum of the values in the dictionary: ",sums)

