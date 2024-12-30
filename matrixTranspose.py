A = [[1,2,3],
     [4,5,6]]
result = [[9,8],
     [6,5],
     [3,2]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result[j][i] = A[i][j] 
        
for r in result:
    print(r)