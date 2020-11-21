import random
import lab3
db = lab3.Database()
for i in range(10):
    db.insert('mynums', random.randint(1,200))
    print()
for i in range(20,30):
    db.insert('mystrs', str(i))
for i in range(20,40,2):
    db.insert('mytuples', (i, i*i))
db.insert('mynums', 'Apple') # Error, no coincide tipo
db.remove('mystrs', '25') # OK
db.remove('mytuples', (22,'484')) # Error, dato no está en la colección
ret = db.search('SELECT mynums WHERE >= 50 ASC')
for i in ret:
    print(i) # e.g. 50, 64, 82, por el random