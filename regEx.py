import re
x = 'I have 3 numbers, 2 are even and 1 is odd. Can python figure out that I have more than 0 numbers?'
y = re.findall('[0-9]+', x)
print(y)