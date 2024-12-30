def mulMat():
    mat1= []
    mat2 = []
    sum_matrix = []
    
    print("Enter the dimensions of the  first matrix")
    r1 = int(input("Enter the rows of 1st matrix: "))
    c1 = int(input("Enter the columns of 1st matrx: "))
    
    print("Enter the elements")
    
    for i in range(0,r1):
        row_list = []
        for j in range(0,c1):
            num = int(input("Enter the element: "))
            row_list.append(num)
        mat1.append(row_list)
        
        
    print("Enter the dimensions of the  2nd matrix")
    r2 = int(input("Enter the rows of 2nd matrix: "))
    c2 = int(input("Enter the columns of 2nd matrx: "))
    
    print("Enter the elements")
    
    for i in range(0,r2):
        row_list = []
        for j in range(0,c2):
            num = int(input("Enter the element: "))
            row_list.append(num)
        mat2.append(row_list)
    
    print("First Matrix")
    
    for i in range(0,r1):
        for j in range(0,c1):
            print(mat1[i][j], end = "")
        
    print("second  Matrix")
    
    for i in range(0,r2):
        for j in range(0,c2):
            print(mat2[i][j], end = "")
            
    res_mat = []
    if c1 ==  r2:
        for i in range(0,r1):
            for j in range(0,c1):
                res_mat[i][j] = 0
        
        for i in range(0,r1):
            for j in range(0,c2):
                for k in range(0,r2):
                    res_mat[i][j] = mat1[i][k] * mat2[k][j]
    
    for i in range(0,r1):
            for j in range(0,c1):
                print(res_mat[i][j], end = "") 
            print("\n")
mulMat()
        