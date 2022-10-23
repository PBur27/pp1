age = int(input("Enter the dog's age in human years: "))
age_dog = 0
i = 0

while i < age:
    if i < 2:
        age_dog += 10.5
    else:
        age_dog += 4
    i += 1

print(age_dog)