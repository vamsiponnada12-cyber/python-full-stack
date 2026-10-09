'''
eg
---
words = input('Entre a word: ')
empty_str = ""
for i in words:
    empty_str = i + empty_str
    print(empty_str)
if empty_str == words:
        print(f'{i} is a palindrome')
else:
        print(f'{i} is not a palindrome')
        

eg-->find out the amstrong
--------------------------
num = int(input('Enter a number: '))
length_ = len(str(num))
amstrong = 0
for i in str(num):
    amstrong = amstrong + int(i)**length_
    print(amstrong)
if amstrong == num:
    print(f'{num} is a amstrong')
else:
    print(f'{num} is not a amstrong')


eg-->find out perfect number or not
-----------------------------------
num = int(input('Enter a number: '))
sum = 0
for i in range(1,num):
    if num%i == 0:
        sum += i
if sum == num:
    print(f'{num} is a perfect number')
else:
    print(f'{num} is not perfect number')

eg-->incresing method like 1,2,3,5,8,13,21...
-----------------------------
num = 0
num_1 = 1
print(num,num_1,end=' ')
for i in range(1,10):
    num_2 = num + num_1
    num = num_1
    num_1 = num_2
    print(num_2,end=' ')

'''








































