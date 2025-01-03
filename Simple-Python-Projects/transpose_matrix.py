def transpose(matrix):

    
    result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    print(result)
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]
    print("The transpose is ")
    for i in range(len(result)):
        print(f"{result[i]}", end = " ")
        print()


rows = int(input("Enter the number of rows:"))
columns = int(input("Enter the number of columns:"))
matrix = [[0 for _ in range(columns)] for _ in range(rows)]
print(f"Enter {rows} X {columns} matrix")
for i in range(rows):
    for j in range(columns):
        matrix[i][j] = int(input())
for i in range(len(matrix)):
    print(matrix[i], end=" ")
    print()
transpose(matrix)
