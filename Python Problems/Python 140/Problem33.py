## Largest number in an array

n = [211,427,432,294,214]
for i in n:
    i = int(i)
largest = n[0]
for j in n:
    if j > largest:
        largest = j
else:
    print(largest)
