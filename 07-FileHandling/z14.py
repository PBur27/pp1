filename = input('Enter filename (without .txt): ')

with open(f"{filename}.txt") as file:

    print(f"File name: {filename}.txt \nNumber of lines: {len(file.readlines())}")