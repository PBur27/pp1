fibonacci = [0, 1]
for i in range(2, 51):
    fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
print(fibonacci)