import re

x = 'From guneet.brar@gmail.com was sent on Tuesday and he got $120.22'
y = re.findall('\$[0-9.]+', x)
print(y)