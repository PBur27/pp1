file = open('numbers.txt', 'r')

file_content = file.readlines()

int_file_content = []
sum = 0

for line in file_content:
    int_file_content.append(int(line))
    sum += int(line)

print(sum, int_file_content)