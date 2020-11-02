fhand = open('Pride and Prejudice.txt')
# if len(fhand) < 1 : fhand = 'Pride and Prejudice.txt'
# hand = open(fhand)

di = dict()
for line in fhand :
    line = line.rstrip()
    words = line.split()
    for word in words :
        # idiom: retrieve/create/update counter
        di[word] = di.get(word, 0) + 1

lst = list()
for k,v in di.items() :
    # print(v,k)
    newt = (v,k)
    lst.append(newt)

# print('Flipped', lst)

lst = sorted(lst, reverse=True)
print('Sorted top 5: ')
for v,k in lst[:5] :
    print(k,v)