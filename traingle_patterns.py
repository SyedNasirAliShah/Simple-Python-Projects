# T_PATTERN 1:

for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=' ')
    print()

# T_PATTERN 2:

for i in range(-4, 1):
    for j in range(i, 1):
        print('*', end=" ")
    print()

# T_PATTERN 3:

for i in range(-4, 1):
    for j in range(i,0):
        print(" ",end=' ')
    for k in range(-4, i+1):
        print("*", end=' ')
    print()

# T_PATTERN 4:

for i in range(-4,1):
    for j in range(-4,i):
        print(' ',end=' ')
    for k in range(i,1):
        print('*',end=' ')
    print()

# PYRAMID 1

for i in range(1, 6):
    for j in range(i, 6):
        print(' ', end=' ')
    for k in range(0, 2*i-1):
        print('*', end=' ')
    print()

# PYRAMID 2:

for i in range(-4,1):
    for j in range(-4,i):
        print(' ',end=' ')
    for k in range(2*i-1,0):
        print('*',end=' ')
    print()

# DIAMOND:

x = int(input('Enter number of rows:'))
for i in range(1, x):
    for j in range(i, x):
        print(' ', end=' ')
    for k in range(0, 2 * i - 1):
        print('*', end=' ')
    print()

for i in range(-x+1, 1):
    for j in range(-x+1, i):
        print(' ', end=' ')
    for k in range(2 * i - 1, 0):
        print('*', end=' ')
    print()