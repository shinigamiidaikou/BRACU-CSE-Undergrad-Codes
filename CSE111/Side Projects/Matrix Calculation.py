m1 = []  # Matrix 1
m2 = []  # Matrix 2


def addMatrix(A, B):
    '''
    ====================  Matrix Add Function  =====================
    ----------------------------------------------------------------
    # The function takes 2 parameters which are 2 matrices
    # Namely A & B, and calculates C = (A + B).
    # If number of columns & rows of the 2 matrices are not equal-
    # it will show that the calculation is not possible.
    ## Otherwise, it calculates & returns matrix C.
    '''
    C = list()
    if len(A) == len(B):
        equal_state = True
        for i in range(len(A)):
            if len(A[i]) != len(B[i]):
                equal_state == False
                break
        if equal_state is False:
            return "Addition can't be Calculated. No of rows not same"
        else:
            for i in range(len(A)):
                row_list = list()
                for j in range(len(A[i])):
                    row_item = A[i][j] + B[i][j]
                    row_list.append(row_item)
                C.append(row_list)
            return C
    else:
        return "Addition can't be Calculated. No of columns not same"


def subsMatrix(A, B):
    '''
    ================  Matrix Substract Function  ====================
    -----------------------------------------------------------------
    # The function takes 2 parameters which are 2 matrices
    # Namely A & B, and calculates C = (A - B).
    # If number of columns & rows of the 2 matrices are not equal-
    # it will show that the calculation is not possible.
    # Otherwise, it calculates & returns matrix C.
    '''
    C = list()
    if len(A) == len(B):
        equal_state = True
        for r in range(len(A)):
            if len(A[r]) != len(B[r]):
                equal_state == False
                break
        if equal_state is False:
            return "Addition can't be Calculated. No of rows not same"
        else:
            for r in range(len(A)):
                row_list = list()
                for c in range(len(A[r])):
                    row_item = A[r][c] - B[r][c]
                    row_list.append(row_item)
                C.append(row_list)
            return C
    else:
        return "Addition can't be Calculated. No of columns not same"


def multipyMatrix(A, B):
    '''
    ==================  Matrix Multiply Function  ====================
    ------------------------------------------------------------------
    # The function takes 2 parameters which are 2 matrices
    # Namely A & B, and calculates C = A * B.
    # Theoretically, The number of columns in Matrix-A must be equal to-
    # the number of rows in Matrix-B. It won't be calculable otherwise.
    '''
    C = list()
    if len(A[0]) != len(B):
        print("Can't be multiplied.\nReason: The number of columns in Matrix A is not equal to the number of rows in Matrix B")
    else:
        for m in range(len(A)):
            row_list = list()
            for i in range(len(B[0])):
                element = 0
                for j in range(len(B)):
                    element += A[m][j] * B[j][i]
                row_list.append(element)
            C.append(row_list)
        return C


def transpose(m):
    '''
    =========================  Transpose Function  ==========================
    -------------------------------------------------------------------------
    # The function will transform called matrix to the transpose of the matrix.
    # The function takes a matrix as the only argument and transposes it.
    # After the operation, it returns the new matrix
    
    # Definition:
    # [The transpose of a matrix means the rows of the matrix will become
    # the columns of the matrix, the columns will become rows of the matrix]
    '''
    t = list()
    for i in range(len(m)):
        if i == 0:
            for j in range(len(m[i])):
                t.append([m[i][j]])
        else:
            for j in range(len(m[i])):
                t[j].append(m[i][j])
    return t


def takeRowColInput():
    row = int(input("Please enter the number of rows in the matrix: "))
    col = int(input("Please enter the number of columns in the matrix: "))
    matrixInitialization(m1, row, col)
    matrixInitialization(m2, row, col)
    printMatrix(m1)
    printMatrix(m2)


def matrixInitialization(m, row, col):
	for r in range(row):
		l = []
		for c in range(col):
			l.append(0)
		m.append(l)


def printMatrix(m):
    for row in range(len(m)):
        print("| ", end="")
        for col in range(len(m[row])):
            print(m[row][col], end=" ")
        print("|")
    print()


def takeMatrixInput(m):
    for row in range(len(m)):
        for col in range(len(m[row])):
            m[row][col] = int(input(f"Enter value for [{row},{col}] : "))
    printMatrix(m)


takeRowColInput()
takeMatrixInput(m1)
takeMatrixInput(m2)

addRes = addMatrix(m1, m2)  # m1+m2
print('Result of addition:')
printMatrix(addRes)

subRes = subsMatrix(m1, m2)  # m1-m2
print('Result of substraction:')
printMatrix(subRes)

mulRes = multipyMatrix(m1, m2)  # m1*m2
print('Result of multiplication:')
printMatrix(mulRes)

m1 = transpose(m1)
print('Transpose of A:')
printMatrix(m1)

m2 = transpose(m2)
print('Transpose of B:')
printMatrix(m2)
