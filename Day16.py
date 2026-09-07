'''
Functions
----------
-->A function is a block of code that can be executed only when is called...
-->A function start with def keyword and the line is called defination line, where we can define the function name
-->And if we wnt to execute the program in the function, need to call the function name define at def line 

syntax
-------
def fun_name(parameters):
    pass
fun_name(arguments)
eg
---
def add_(a,b):
    print(a+b)
add_(6,7)

Arguments
---------

positional arguments (or) required arguments
---------------------------------------------
-->The arguments should be exact number same at def line and calling, incase if they are not same number it will raise an error

eg
----
def add_(a,b):
    print(a+b)
add_(6)

eg
---
num = 0
num_1 = 1
def feb_(num,num_1):  
    print(num,num_1,end=' ')
    for i in range(1,10):
        num_2 = num + num_1
        num = num_1
        num_1 = num_2
        print(num_2,end=' ')
feb_(num,num_1)

default arguments
-----------------
-->the default  arguments where the function will only consider the dta at calling, even data present at def line..


eg
---
def feb_(num,num_1):
    print(num+num_1)
feb_([2,3],[5,8])

eg
---
def data_(a=1,b=4):
    print(a+b)
data_(3,4)

eg
---
def prime(num=10,count=1) :
    for j in range(1,num+1):
        if num%j == 0:
             count += 1
             print(count)
    if count == 2:
        print(f'{num} is a prime')
    else:
        print(f'{num} not a prime')
prime(num = int(input('Enter a number: ')),count = 0)


keyword arguments
-----------------
-->keyword arguments are sending arguments in a pair(a=2),and the pass order is not consider....

eg
---
def data_(age,name,batch,location):
    print(name)
    print(location)
    print(batch)
    print(age)
data_(name = 'vamsi',age = 22,batch = 6,location = 'vizag')

variable length arguments
-------------------------
-->Adding a (* call its a args) before a variable at parameters we can pass tuple of argumentsn and can be access with indexing

eg
---
def all_(*name):
    print(name)
all_('teja','vamsi','lokesham','ranjith')

keyword length arguments
------------------------
-->put in ** to data  

eg
---
def details(**data_):
    print(data_.keys())
details(name='vamsi',age=21,location='vizag',batch=6)

return
------
-->Retturn keyword used inside the functuion, once the return is executed means it will get back to calling with return values..

eg
--
def all_(a,b):
    return(a-b)
print(all_(7,9))

'''





















































































































