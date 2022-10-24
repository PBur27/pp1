a = 8
b = 17

for i in range(0, a+1):
    if i == 0 or i == a:
        for i in range(0, b):
            print('*', end='')
        print('')
    else:
        print("*" + " "*(b-2) + "*")
