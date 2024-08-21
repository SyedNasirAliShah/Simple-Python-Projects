user = int(input("Enter a number:"))
m = 1
j=0
for i in range(1, user+1):
    while(True):
        count = 0
        for j in range(1, m + 1):
            if m % j == 0:
                count = count + 1
        if count == 2:
            m = m + 1
            break
        m = m + 1
    print(j, end=" ")