file = open('countries.txt', 'r')

file_content = file.readlines()

i = 1

for line in file_content:
    print(f"{i} " + line, end='')
    i += 1
