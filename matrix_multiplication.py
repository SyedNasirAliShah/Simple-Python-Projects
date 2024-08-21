def matMul(matrix1, matrix2):
    if len(matrix1[0]) == len(matrix2):
        res = 0
        result = [[0 for _ in range(len(matrix2[0]))]
              for _ in range(len(matrix1))]
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] = result[i][j] + matrix1[i][k] * matrix2[k][j]
        print(f"MULTIPLICATION IS:")
        for i in range(len(result)):
            print(f"{result[i]}", end=" ")
            print()
    return 1

def showMatrices(matrix1, matrix2):
    print(f"MATRIX 1")
    for i in range(len(matrix1)):
        print(f"{matrix1[i]}", end=" ")
        print()
    print(f"MATRIX 2")
    for i in range(len(matrix2)):
        print(f"{matrix2[i]}", end=" ")
        print()


if __name__ == "__main__":
    rows = int(input("Enter number of rows(matrix1):"))
    columns = int(input("Enter number of columns(matrix1):"))
    print(f"Enter the {rows} X {columns} matrix1:")
    matrix1 = [[0 for _ in range(columns)] for j in range(rows)]
    for i in range(rows):
        for j in range(columns):
            user = int(input())
            matrix1[i][j] = user
    rows = int(input("Enter number of rows(matrix2):"))
    columns = int(input("Enter number of columns(matrix2):"))
    print(f"Enter the {rows} X {columns} matrix2:")
    matrix2 = [[0 for _ in range(columns)] for j in range(rows)]
    for i in range(rows):
        for j in range(columns):
            user = int(input())
            matrix2[i][j] = user
    showMatrices(matrix1, matrix2)

    matMul(matrix1, matrix2)
