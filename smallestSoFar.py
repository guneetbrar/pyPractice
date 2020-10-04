smallest_so_far = 0
for value in [1, 2, 10, -11, 22, -9999, -0.0002, -999999.9991, -1000000.022123] :
    if smallest_so_far > value :
        smallest_so_far = value
        print(smallest_so_far)
print('Smallest number so far is: ', smallest_so_far)