array = [[True,False],[True,True],[False,False]]
for i in range(0, 3):
    for j in range(0, 2):
        if array[i][j] == True:
            array[i][j] = False
        else:
            array[i][j] = True

print(array)