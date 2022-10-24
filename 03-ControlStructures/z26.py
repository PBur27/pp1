code = '1234'
i = 0

while True:
    user_code = input("Enter the PIN code: ")
    if user_code == code:
        print("Correct!")
        break
    else:
        print("Incorrect...")
        if i == 2:
            print("Sorry, your payment card has been blocked.")
            break
    i += 1