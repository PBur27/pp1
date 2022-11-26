array = [[3,9,2],[2,4,5],[0,4,8]]

sum = 0

for subarray in array:
    for num in subarray:
        if num%2 == 0:
            sum+= num

print(sum)