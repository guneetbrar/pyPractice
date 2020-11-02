import re
x = 'From: a friend: to a friend'
y = re.findall('^F.+:', x)
print(y)