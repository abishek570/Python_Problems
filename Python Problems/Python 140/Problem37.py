## matrix addition

m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 =[[9,8,7],[6,5,4],[3,2,1]]

result = []

for i in range(len(m1)):
    row = []
    for j in range(len(m1[0])):
        row.append(m1[i][j]+m2[i][j])
    result.append(row)
print(result)

## matrix subtraction

m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 =[[9,8,7],[6,5,4],[3,2,1]]

result = []

for i in range(len(m1)):
    row = []
    for j in range(len(m1[0])):
        row.append(m1[i][j]-m2[i][j])
    result.append(row)
print(result)
