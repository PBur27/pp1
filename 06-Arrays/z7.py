array = [1,2,3,4,5]
array[len(array)-1] -= 1
array[len(array)-1] += 4
array[len(array)//2] = array[len(array)//2] * 2
for i in range(0, len(array)):
    array[i] += 3
print(array)
