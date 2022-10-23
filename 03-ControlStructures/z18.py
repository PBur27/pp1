a = int(input("Enter the amount in PLN "))
print(f"The amount of {a} PLN in coins:")
coin5 = a//5
coin2 = (a%5)//2
coin1 = (a%5)%2

print(f"5zł - {coin5}")
print(f"2zł - {coin2}")
print(f"1zł - {coin1}")