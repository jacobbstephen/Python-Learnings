A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
B = [[9,8,7],
     [6,5,4],
     [3,2,1]]
result = [[9,8,7],
     [6,5,4],
     [3,2,1]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]
        
for r in result:
    print(r)