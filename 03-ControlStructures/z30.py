from pickletools import int4


n = int(input("How many prime numbers do you want to print? "))
i = 2

while n > 0:
    prime = True
    for j in range(2, i//2+1):
        if i%j == 0:
            prime = False
            break
    if prime == True:
        print(i)
        n -= 1
    i += 1