source = []

similar = []
result = 0

def readfile(file):
    f = open(file, "r")
    rf = f.readlines()
    for lines in rf:
        source.append(lines)

readfile("Day 3\input.txt")

def splitsource(original):
    for line in original:
        half = len(line)//2
        first = line[:len(line)//2]
        second = line[len(line)//2:]
        for part in set(first):
            if part in second:
                similar.append(part)

splitsource(source)

for char in similar:
    if char.isupper():
        result += ord(char) - ord('A') + 27
    else:
        result += ord(char) - ord('a') + 1

print(similar)
print(result)

#     for line in range(len(original)):