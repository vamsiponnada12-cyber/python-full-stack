'''
Exception handling
-------------------
-->This is the way of handling errors
--> we can write any number exception for one code writen at try block

try
---
-->the try block where we can write a code which may contain errors

syntax
-------
-->try:
      code lines
      
except
------
-->This will handle eroors that are raised at try block

eg
---
try:
    print(7/0)
    print(num)
except ZeroDivisionError:
    print('division by zero')
except NameError:
    print('name error')
syntax
------
-->except NameEroor:
    print("NameError")

else
-----
-->the else blosk will execute, if no error at try block

eg
---
try:
    print('Hello world')
except ZeroDivisionError:
    print('division by zero')
except NameError:
    print('name error')
else:
    print('No Error')
    
finally
--------
-->This block will execute regardless with the error at try block

eg
---
try:
    print('Hello world')
except ZeroDivisionError:
    print('division by zero')
except NameError:
    print('name error')
else:
    print('No Error')
finally:
    print('End')

File Handling
-------------
-->The file handler is a object, which is used to creat,update,read,and delete..

r-->the (r)
w-->
a-->
'''

with open('dem.txt','x') as file:
    (file.write('python class'))dwq









































