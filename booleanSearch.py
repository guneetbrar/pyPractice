found = False
print('Before ', found)
for value in [0, 1, 2, 3, 4, 400, 15, 3, 200] :
    if value == 3 :
        found = True
    print(found, value)
print('After ', found)
