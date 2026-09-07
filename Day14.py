'''
Find odd and even
-----------------
eg
--
ran_ = int(input('Enter a number: '))
for j in range(1,ran_+1):
    if j%2 == 0:
        print(f'{j}is even')
    else:
        print(f'{j}is odd')
        
Find only odds
--------------
eg
---
ran_ = int(input('Enter a number: '))
for j in range(1,ran_+1):
    if j%2 != 0:
        print(f'{j} is odd')

Find only odds
--------------
eg
--

nums = [23,78,97,5]
for i in nums:
    if i%2 ==0:
        print(f'{i} is even')
    if i%2 != 0:
        print(f'{i} is odd')
find vowels
-----------
eg
--
words_ = input('Entar a word: ')
vowels = 'aeiouAEIOU'
count = 0
for  i in words_:
    if i in vowels:
        count += 1
        print(f'{i} is vowels')
print(count)

remove duplicates
-----------------
eg
---

digits = [1,2,3,1,5,3]
empty_ = []
for i in digits:
    if i not in  empty_:
        empty_.append(i)
print(empty_)

find duplicates
---------------

eg
----
digits = (1,2,3,1,5,3)
empty_ = ()
for i in digits:
    if i in  empty_:
        print(f'{i} is duplicate')
    else:
    empty_.append(i)



        

'''



























































