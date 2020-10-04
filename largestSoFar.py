largest_so_far = -1
print('Before the loop largest so far: ', largest_so_far)
for value in [1, 2, -10, 22, 100, 9928, 2921390, 0, 99] :
    if largest_so_far < value :
        largest_so_far = value
        print(largest_so_far)
print('After the loop largest so far: ', largest_so_far)
