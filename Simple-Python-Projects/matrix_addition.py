def matrixAddition(m1, m2):
    result = [[0 for _ in range(len(m2[0]))]
              for _ in range(len(m1))]
    for i in range(0, len(m1)):
        for j in range(0, len(m1[i])):
            result[i][j] = m1[i][j] + m2[i][j]
    print("Addition is:")
    for i in range(len(m1)):
        print(f"{result[i]}")


def showMatrix(m1, m2):
    print(f"The matrices of order {len(m1)} x {len(m2[0])} is:")
    for i in range(len(m1)):
        print(f"{m1[i]} \t {m2[i]}", end=" ")
        print()
    print()

rows = int(input("Enter the rows of matrix:"))
columns = int(input("Enter the columns of matrix:"))
m1 = [[0 for _ in range(columns)] for _ in range(rows)]
m2 = [[0 for _ in range(columns)] for _ in range(rows)]

print(f"Your matrix is of order {rows} X {columns} ")
print("Enter the values for first matrix:")
for i in range(len(m1)):
    for j in range(len(m2[0])):
        user = int(input())
        m1[i][j] = user

print("Enter the values for second matrix:")
for i in range(len(m1)):
    for j in range(len(m2[0])):
        user = int(input())
        m2[i][j] = user
showMatrix(m1, m2)
print()
matrixAddition(m1, m2)