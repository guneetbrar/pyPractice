d = {'a':12, 'x':220, 'i':1, 'z':1}
tmp = list()
for k,v in d.items() :
    tmp.append((v,k))
print(tmp)
tmp = sorted(tmp)
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)