array = [2,3,7,5,4]

print(array)
print(len(array))
print(array[0])
print(array[1])
print(array[len(array)-1])
print(array[len(array)-2])
print(array[0]+array[len(array)-1])
print(array[(len(array)-1)//2])
for i in range(0, len(array)):
    print(str(array[i]),end=' ')
print()
for i in range(0, len(array)//2):
    print(array[i],end=' ')
