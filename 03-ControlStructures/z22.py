for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print(i,' Bingo')
    elif i % 3 == 0:
        print(i,' Three')
    elif i % 5 == 0:
        print(i,' Five')
    else:
        print(i)
