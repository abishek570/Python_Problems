## Matrix Multiplication

m1 = [[1,2,3],
      [4,5,6]
      ]

m2 =[[9,8],
     [6,5],
     [2,1]
    ]

a = len(m1)
a1 = len(m1[0])
b = len(m2)
b1 = len(m2[0])

result = [[0 for _ in range(b1)] for _ in range(a)]

print(result)

for i in range(a):
      for j in range(b1):
         for k in range(a1):
            result[i][j]+=m1[i][k]*m2[k][j]
print(result)
    
