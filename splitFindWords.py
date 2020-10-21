han = open('test.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    # Guardian statement
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[2])
