switch = 0
i = 1

while True:
    if i == 6:
        switch = 1
    for j in range(0, i):
        print('*', end=' ')
    print('\n')
    if switch == 0:
        i += 1
    else:
        i -= 1
    if i < 1:
        break
