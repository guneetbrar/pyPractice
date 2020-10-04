smallest = None
for value in [9, 12, 2, -1, 20, 99] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
        print(smallest, value)
print('Smallest number found is: ', smallest)