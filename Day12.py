'''
FOR statement
-------------
-->for loop is used to iterate over a sequence or iterable datatyes

eg
----
nums = [12,3,5,61]
for num in nums:
    print(num)
    

else in for
-----------
-->unlike if else, else block in for statementis executed after completed of all iterations

eg
---
nums = 'python'
for num in nums:
    print(num)
else:
    print('for ended')


eg--> find even and odd given below
---
val_ = [1,2,3,4,5,6,7,8]
for j in val_:
    if j%2 == 0:
        print(f'{j} is even')
    else:
        print(f'{j} is odd')

break
-----
-->the break used to stop iteration based on the condition given

eg
---
nums = [1,2,3,4,5]
for num in nums:
    print(num)
    if num == 3:
        break
        
continue
--------
-->the continue is keyword used to skip the current iteration based on the condition

eg
---
nums = [1,2,3,4,5,6,7,8]
for num in nums:
    if num == 6:
        continue
    print(num)

pass
----

eg
---
for j in range(1,11):
    if j == 15:
        print(j)
    else:
        pass

assert
------
-->assert is a keyword used to check the condition, incase the condition is false, it will rise the error(Assertion error)

eg
---
age = 15
assert age >= 18, 'not eligble to vote'
print('your eligble to vote')

while loop
----------

eg
---
num = 1
while num < 5:
    print(num)
    num += 1

'''

1.find out the number is even or odd ?
2.remove duplicates from the list?
3.number os owels in the string?
4.



































