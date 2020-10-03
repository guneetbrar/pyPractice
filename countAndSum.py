count = 0
sum = 0
print('Before ', count, sum)
for number in [0,15, 22, 12, 44, 100, 1999, 1995] :
    count = count + 1
    sum = sum + number
    print(count, sum)
print('After ', count, sum)