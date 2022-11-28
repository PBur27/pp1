file = open('z15.txt', 'r')

file_content = file.readlines()

i = 0

while i <= len(file_content):
    print()
    key = input('Press Enter to print text ')
    print()
    if key == '':
        for i in range(i, i+5):
            print(file_content[i], end='')
            if i == len(file_content) - 1:
                break
    if i == len(file_content) - 1:
                break