lines = []

while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
for line in lines:
    print(line.upper())
