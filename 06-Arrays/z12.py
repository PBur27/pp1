array = [[2,5,4],[9,0,3]]

print(array)
print(len(array),len(array[0]))
print(array[0][1])
print(array[1][2])
for num in array[1]:
    print(num,end=' ')
print('\n')
for row in array:
    for num in row:
        print(num,end=' ')
    print()
print('\n')
for row in array:
    print(row[len(row)-1])