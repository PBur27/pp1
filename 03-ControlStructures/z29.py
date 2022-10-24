number_list = []

while True:
    a = int(input('Enter number: '))
    if a == 0:
        break
    number_list.append(a)

number_sum = 0
number_mean = 0

number_sum = sum(number_list)
number_mean = sum(number_list)/len(number_list)

print(f"Result: quantity = {number_sum}, mean = {number_mean}")