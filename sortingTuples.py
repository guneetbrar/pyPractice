d = {'a':12, 'x':220, 'i':1, 'z':1}
d.items()
print(sorted(d.items()))

for k,v in sorted(d.items()):
    print(k,v)