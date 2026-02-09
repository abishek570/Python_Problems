## arr[i][j] = i*j

X, Y = map(int, input("Enter two digits (X, Y): ").split(' '))

result = [[0 for _ in range(Y)] for _ in range(X)]

print(result)

for i in range(X):
    for j in range(Y):
        result[i][j] = i*j

for i in result:
    print(i)