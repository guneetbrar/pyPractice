import re

x = 'From guneet.brar@gmail.com was sent on Tuesday'
y = re.findall('^From (\S+@\S+)', x)
print(y)