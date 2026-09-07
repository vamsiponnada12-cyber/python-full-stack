'''
Lambda function
---------------
-->Lambda function is small anonymous function
-->Lambda can take n number of arguments, but only with one expression
-->The function is defined by using lambda keyword

syntax
------
-->lamda arguments : expression
eg
--
add_ = lambda a,b,c,d: a+b+c+d
print(add_(10,20,30,50))

eg-->Find even number?
---
even = lambda num : num % 2 == 0
print(even(4))

eg-->Find greter value?
--
num = lambda a,b : a if a>b else b
print(num(20,10))

eg-->Find cube value?
--
num = lambda a :  a**3
print(num(3))

Filter
------
-->filter () function will perform only on selected elements of iterables

eg
---
nums = [1,2,3,4,5]
data = filter(lambda a : a % 2 == 0,nums)
print(list(data))

map()
-----
-->Map() function will perform on all elements of a it erables

syntax
-------
-->map(lambda arguments: expression, iterables)

eg
---
nums = [1,2,3,4,5]
data = map(lambda a : a + 6,nums)
print(list(data))

eg
---
nums = [1,2,3,4,5]
data = map(lambda a : a % 2 == 0,nums)
print(list(data))

Reduce()
--------
-->The reduce() function repeatedly applie a function to the elements and reduce them to one final value.
-->It is available in the functools module.

syntax
------
-->reduce(lambda arguments : expression, iterable)

eg
---
from functools import reduce
nums = [1,2,3,4,5]
data_ = reduce(lambda a,b: a+b,nums)
print(data_)

eg
---
from functools import reduce
data_ = reduce(lambda a,b : a+b,range(1,10))
print(data_)

'''







































