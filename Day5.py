'''
input farmating
---------------
integet-->int(input())
----------------------
a = int(input('Enter a integer: '))

float-->float(input())
----------------------
b = float(input('enter any decimal: '))
print(b + 7)

string-->input()
-----------------
a = input('Enter a string: ')
print(type(a))

list-->list(map(int,(input().split())))
---------------------------------------
nums = list(map(int,(input('Enter some numbers: ').split())))
print(nums)

tuple-->tuple(map(int,(input().split())))
------------------------------------------
nums = tuple(map(int,(input('Enter some numbers: ').split())))
print(nums)

---->
data_ = eval()



--->eg
-------
name = 'vamsi'
age = 22

print('my name is',name,'age is',age)
print('hello!',name)

print(f'my name is {name} and i am {age} years old')

eg--->
---
name = 'vamsi'
age = 23

print('my name is %s and ia am %d years old'%(name,age))



'''



















