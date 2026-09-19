'''
Tuple
-----
-->Tuple is collection of differnt datatypes that separated by , and represented by ()
-->it is immutable
-->we can pass a tuple values and that can be asign to the variables,but should match same number variables and values inside the tuple

eg
--
t = (1,'python',[3,4],(7,9))
print(t[3])

eg
--
t = (1,'python',[3,4],(7,9))
print(t[3][1])

indexing
--------

-->if items is not presnt in the tuple , it will raise value Error

eg
---
t = (1,'Python',[3,4],(7,9))
print(t.index('python'))

len()
-----

eg
--
t = (1,'Python',[3,4],(7,9))
print(len(t))


name,age =('vamsi',22)
print(name,age)

max()
-----
-->used to find out the max value from the tuple

eg
--
so = (67,89,56,45)
print(max(so))

min()
------
-->used to find out the least value from the tuple

eg
--
so = (67,89,56,45)
print(max(so))

count()
-------
-->count is used to count an item present in the tuple

eg
--
so = (67,89,56,45,56)
print(so.count(56))

concatination()
---------------

eg
--
so = (67,89,56,45)
do = (67,56)
print(so+do)

'''

my_values = {10, 20, 5}
print(max(my_values) + min(my_values))
















































