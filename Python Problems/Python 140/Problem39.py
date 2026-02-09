## Transpose matrix calculator

m = [[1,2,3],
     [4,5,6],
    ]

result = [[0 for _ in range(len(m))] for _ in range(len(m[0]))]

for i in range(len(m[0])):
    for j in range(len(m)):
        result[i][j] = m[j][i]

print(result)

