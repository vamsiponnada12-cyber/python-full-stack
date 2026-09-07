'''
Scope variables
---------------
1.Local variable
----------------
-->A variable is define inside the function call it as local variable,where the variable can only access with in that function

eg
---
def display():
    name = 'vamsi'
    print(name)
display()

2.Global variable
-----------------
-->A variable that is defined outside the function call and it can be access anywhere through out the program

eg
---
a = 90
def display():
    print(a)
display()
print(a)

Global keyword
--------------
-->Global is keyword used to reassign new values to a variables that was already define outside the function call

eg
---
a = 90
def display():
    global a
    a = 10
display()
print(a)

eg
---
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is a even')
    else:
        print(f'{num} is a odd')
even_odd(8)

eg
---
num = 2
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is a even')
    else:
        print(f'{num} is a odd')
even_odd(num)

Recuesive function
------------------
-->The function call itself until the base condition met

'''
def Fac(a):
    if a == 0 or a == 1:
        return a
    return a * Fac(a-1)
print(Fac(5))














































 
