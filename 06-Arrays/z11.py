import random
def fmonths(n):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return months[n]

n = random.randint(0,11)
print(n+1, fmonths(n))