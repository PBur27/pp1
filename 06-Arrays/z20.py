array = [12,6,4,9,10]

def star(n):
    stars = ''
    for i in range(n):
        stars += '*'
    return stars

for num in array:
    print(f'{num}: ' + star(num))
    
