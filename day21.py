'''
import math
print(math.pi)
print(math.ceil(4.3))
print(math.floor(5.6))
print(math.sqrt(25))
print(math.sin(21))
print(math.pow(4,3))
print(math.cos(5))

import random
print(random.randint(100000,999999))
print(random.randrange(1,100))
colour=['vamsi redd','white','blck','green','yellow','voilet']
print(random.choice(colour))
random.shuffle(colour)
print(colour)


import platform
print(platform.python_version())
print(platform.system())
print(platform.platform())
print(platform.processor())

import collection
data= [pytho
s








from collections import defaultdict
data = defaultdict(list)
data=['python'].append('ranjith')
data=['java'].append('vammsi')
print(data)

from datetime import datetime
today = datetime.today()
print(today.month)
print(today.day)
print(today.year)
print(today.hour)
print(today.minute)
print(today.second)


from datetime import datetime
now = datetime.today()
print(now.strftime('%d-%m-%y'))
print(now.strftime('%H-%M-%S'))
print(now.strftime('%a'))


import random
attempts = 3
num = random.randrange(1,100)
print(num)
while attempts > 0:
    game=int(input('enter a number between 1 to 100:'))
    if game == num:
        print('your guess is correct')
        break
    else:
        attempts-=1

if attempts == 3:
    print('prize money is 1000')
elif attempts == 2:
    print('prize money is 700')
elif attempts ==1:
    print('prize money is 500')
else:
    print('asha dosa neeku ey bokka raledhu tharvatha try chesuko')

'''

import itertools
a = itertools.count(45)
print(next(a))
print(next(a))

b=itertools.repeat('python',6)
for j in b:
    print(j)
    
c=itertools.cycle(['python','java','c'])
for j in c:
    print(j)
                











































































