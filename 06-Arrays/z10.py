import random
array = [random.randint(1,20) for i in range(12)]

print(array)

odd_sum = 0
even_sum = 0

for i in range(0, len(array)):
    if array[i] % 2 == 0:
        even_sum += array[i]
    else:
        odd_sum += array[i]

print(f"odd sum = {odd_sum}, even sum = {even_sum}")