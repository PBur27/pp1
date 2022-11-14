array = [-15,8,-31,47,-2,19]

a_min = 0
a_max = 0

for i in range(0, len(array)-1):
    if array[i] < a_min:
        a_min = array[i]
    elif array[i] > a_max:
        a_max = array[i]
    
print(a_min, a_max)