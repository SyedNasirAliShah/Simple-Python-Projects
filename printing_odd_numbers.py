user_input = int(input("Enter the number:"))
m = 1
for i in range(1, user_input + 1):
    for j in range(m, m + 1):
        if j % 2 != 0:
            print(j, end = " ")
    m = m + 2