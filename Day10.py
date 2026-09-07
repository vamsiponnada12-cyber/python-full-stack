'''
Accessing
---------
-->dict can access by calling key,we will get value from that key
syntax
------
-->dict['key']

get()
-----
-->get() method is also used to get the value from that key

syntax
------
-->dict.get(key)

eg
---
data ={'name':'Teja',
       'balance':8000,
       'adr':12345678934,
       'PANC':'TZPS2696H',
       2:[3,4]}

print(data['name'])
print(data['balance'])
print(data['adr'])
print(data['PANC'])
print(data.get(2))

update()
--------
-->method is used to update a key, incase if the key is not present inside dict then it add that key:value

syntax
------
-->dict.update({key:value})

eg
--
data_ ={'name':'Teja',
       'balance':8000,
       'adr':12345678934,
       'PANC':'TZPS2696H',
       2:[3,4]}


data_.update({'name':'nikhil'})
print(data_)
data_.update({'number':8688697834})
print(data_)

-->there is another way to update a key

syntax
------
-->dict[key] = value

eg
---
data_ ={'name':'Teja',
       'balance':8000,
       'adr':12345678934,
       'PANC':'TZPS2696H',
       2:[3,4]}

data_['name'] = 'sony'
print(data_)
data_['Ac'] = 3425677921345
print(data_)

values()
--------
-->values() methods is used to get all the value from the dict

syntax
------
-->dict.values()

eg
---
data_ ={'name':'Teja',
       'balance':8000,
       'adr':12345678934,
       'PANC':'TZPS2696H',
       2:[3,4]}
print(data_.values())

keys()
------
-->keys() method is used to get the all the key from the dict

syntax
------
-->dict.keys()

eg
--
data_ ={'name':'Teja',
       'balance':8000,
       'adr':12345678934,
       'PANC':'TZPS2696H',
       2:[3,4]}
print(data_.keys())

items()
-------
-->items() method will get the key:value separated from the dict

syntax
------
-->dict.items()

eg
--
data_ ={'name':'Teja',
       'balance':8000,
       'adr':12345678934,
       'PANC':'TZPS2696H',
       2:[3,4]}
print(data_.items())

clear()
-------
-->used to delete entire dict values

syntax
------
-->dict.clear()
eg
--
data_ ={'name':'Teja',
       'balance':8000,
       'adr':12345678934,
       'PANC':'TZPS2696H',
       2:[3,4]}
data_clear()
print(data_)

del()
----
-->
eg
--

data_ ={'name':'Teja',
       'balance':8000,
       'adr':12345678934,
       'PANC':'TZPS2696H',
       2:[3,4]}

print(data_)
del data_['adr']
print(data_)

if statement
------------
-->if condition become true, then it will execute inside block of code
-->incase it becomes false, then it bwill never enter inside the block

eg
---
age = 20
if age>=18:
   print('eligible to vote')
print(age)

if-else
-------
-->else for if statement is a fall-back statement,incase if condition is false then else block will execute

eg
--
age = 15
if age>=18:
   print(f'your {age} eligible to vote')

else:
    print(f'your {age} you have to wait {18 - age}')


a = 90
b = 780
if a>b:
    print(a)
else:
    print(b)


'''












    






































      
