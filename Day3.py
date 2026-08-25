'''
Datatypes & typeconversions
---------------------------
1. Numaric Datatype
-------------------\
-->Float and integer is called as numaric datatype

1.float
-----
-->A number which contains decimal values,we call it as a float datatype



2. Sring
--------
-->string is sequence of char that are enclosed in '',"",""""""
-->String is immutable
eg:
---
any_ = 'python is a computer lnguage'
all_ = Ab,.&[)-+'

3.List
------
-->List is a collection of differnt datatypes
-->and it is represented by [] that are separated by ,
-->inside the list we call it as items
-->List is mutable
eg:
---
any_ = [1,'python;,(5,6)]
print(type(any_))

4.Tuple
-------
-->tuple is collection of different datatypes that are enclosed in () and tghose are separated by ,
-->tuple is immutable
eg
---
nums = (1,89.78,'python',[3,4],(8,9))
print(nums)

5.Dictionary
------------
-->Dictionary is collection of key: value pairs,keys and values are separated by :
-->key and value pair is call it as a item
-->and this items are saparated by ,
-->Dictionry is represent using {}
-->in key place we can use immutable datatypes
-->in values place we can use any datatype
eg
---
data_ = {1,2,
         'name':'vamsi',
         (2,3):'Tuple',}
print(data_)

6.Set
-----
-->set is collection unique elements and set can't allow any duplicate values inside it....
-->set is represented by {} and the elements are separated by ,
eg
--
an =  {1,2,3,3}
print(an)


typeconversion
--------------
float --> int,str

eg.1-->int()
---
price = 45.78
print(int(price))

eg.2-->str()
----
price = 45.78
con = str(price)
print(type(con))

integer --> float,str

eg.1-->float()
----
num = 78
print(float))

eg.2-->str()
----
num = 78
con = str(num)
print(type(con))

string-->int,float

eg.1-->int()
----
do = '3465'
print(int(do))

eg'2-->
----
do ='10.89'
print(float(do))


list --> tuple,string

eg.1-->tuple()
-----
nums = [1,2,3,4]
print(tuple(nums))

eg.2-->str(0
----
nums = [1,2,3,4]
print(str(nums))

tuple-->

eg-->list()
----
all_ = (1,2,4)
print(list(all_))

setr --> tuple,list

eg.1-->tuple()
----
all_ = {1,3,4}
print(tuple(all_))

eg.2-->list()
----
all_ = {1,3,4}
print(list(all_))

dictionary-->list

eg-->
----
details = [('name','vamsi'),('edu','BTech')]
print(dict(details))
























































'''
