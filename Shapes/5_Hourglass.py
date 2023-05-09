size = 5

for i in range(size, 0, -1):
    for j in range(size - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()
for i in range(2, size + 1):
    for j in range(size - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()
