'''
List comprehension
------------------
-->List coprehension is the shortest form of syntax to create a new list

syntax
------
-->[expression for loop condition]
use else
---------
-->[expression condition else loop]

eg
---
old_ = [1,2,3,4,5]
new_ = [i for i in old_ if i%2 == 0]
print(new_)

eg2
----
old_ = [1,2,3,4,5]
new_ = [i if i%2==0 else 'none' for i in old_ ]
print(new_)

Nested comprehension
---------------------
-->using list comprehension generating list inside list

eg
----
a = [[i*j for i in range(1,3)] for j in range(1,10)]
print(a)

eg2
---
of = [[1,2,3],
      [4,5,6],
      [7,8,9]]
data_=[num for i in of for num in i]
print(data_)

Generator
---------
-->A generator is special function which generate one value at time

eg
---
def all_():
    for j in range(1,10):
        yield j
j = all_()
print(next(j))

'''






























