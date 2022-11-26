array = [[0,0,0],[0,0,0],[0,0,0]]

j = 0

for i in range(0,3):
    array[i][j] = 1
    j += 1

for subarray in array:
    for value in subarray:
        print(value, end=' ')
    print()