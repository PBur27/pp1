import mymath

while True:
    a = mymath.read_number()
    b = mymath.generate_number()

    if a == b:
        print('YOU WIN')
        break
