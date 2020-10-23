counts = {}
names = ['guneet', 'george', 'nancy', 'alice', 'arcadio', 'pilar', 'arcadio', 'guneet']
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

# Improved Histogram
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)