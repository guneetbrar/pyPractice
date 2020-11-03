import re
hand = open('test.txt')
numlist = list()
for line in hand :
    line = line.rstrip()
    stuff = re.findall('^Myword: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(num)
print('Maximum:', max(numlist))

