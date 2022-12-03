source = []

similar = []
result = 0

def readfile(file):
    f = open(file, "r")
    rf = f.readlines()
    for lines in rf:
        new_string = lines.replace('\\n', '')
        source.append(new_string)

readfile("Day 3\input.txt")

for value in range(0, len(source), 3):
    elf1 = source[value]
    elf2 = source[value+1]
    elf3 = source[value+2]
    for part in set(elf1):
            if part in elf2 and part in elf3:
                similar.append(part)

for char in similar:
    if char.isupper() and char != "\\n":
        result += ord(char) - ord('A') + 27
    elif char.islower() and char != "\\n":
        result += ord(char) - ord('a') + 1

print(result)

