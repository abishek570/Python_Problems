N = 2
M = 3

Grid = [[1,0,1],[-8,9,-2]]

a = []
for i in range(0,N):
    for j in range(0,M):
        a.append(Grid[i][j])

print(sum(a))