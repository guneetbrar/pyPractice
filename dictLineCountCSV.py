import csv
fname = input('Enter the file name: ')
if len(fname) < 1 : fname = 'type.csv'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    # print(di)
    # If splitting a sentence then use the code below to split words from the sentence
    # wds = lin.split()
    # print(wds)
    for lin in hand:
        oldcount = di.get(lin,0)
       # print(lin,'old',oldcount)
        newcount = oldcount + 1
        di[lin] = newcount
       # print(lin,'new', newcount)

    largest = -1
    theword = None
    for k,v in di.items() :
        # print(k,v)
        if v > largest :
            largest = v
            theword = k
    print('Largest - ', k,largest)

    smallest = 2
    for k,v in di.items() :
        if v < smallest :
            smallest = v
    print('Smallest - ', k, smallest)

