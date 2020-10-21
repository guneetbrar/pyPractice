line = 'From stephen.dude@gmail.com Sat Jan 5 1992 09:12:12'

words = line.split()
email = words[1]
pieces = email.split('@')
domain = pieces[1]
print(domain)