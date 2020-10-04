data = 'From ironman@marvel.com Sun Oct 4,2020 14:42:00'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
domain = data[atpos+1 : sppos]
print(domain)