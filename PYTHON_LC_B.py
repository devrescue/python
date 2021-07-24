#Create matrix
matrix = [[col for col in range(4)] for row in range(0,4)]
print(matrix)

transposedMatrix = [[row[i] for row in matrix] for i in range(4)]
print(transposedMatrix)

#tmB = transposedMatrixB
tmB = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for r in range(4):
    for c in range(4):
        tmB[c][r] = matrix[r][c]

print(tmB)