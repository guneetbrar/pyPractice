fhand = open('test.txt')
for line in fhand:
    line = line.rstrip()
    if not '@gmail.com' in line:
        continue
    print(line)