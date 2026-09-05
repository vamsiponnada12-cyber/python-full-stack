'''
List
-----
indexing
---------
positive
--------
negetive
--------

eg
--
a = [1,2,3,4,'python']
print(a[4][-1])

all_ = [12,[1,'python',[1,4],(78,[6,7])],['java',78]]
print(all_[1][3][1])

-->

data = ['python',[1,2,(90,'details',[67,0]),(78,'student')]]

print(data[1][2][1][2])

len()
-----
-->the function is used to find the number of items present inside list

syntax
------
-->len(variable_name)
eg
---
data = ['python',[1,2,(90,'details',[67,0]),(78,'student')]]
print(len(data))

slicing
-------

eg
---
data_ = [1,2,3,4,5,6,7]
print(data_[2:6])

concatination
-------------

eg
---
a = [1,2]
b = [2,3]
print(a+b)

methods
-------

append()
--------
-->append method will add new items into list at last index position

syntax
------
-->variable_name.append(item)

eg
--
go = [1,2]
print(go)
go.append(3)
print(go)
go.append(4)
print(go)

-->
a = [1,2]
a.append([3,4])
print(a)


extend()
-------
-->extend() will add the items into a list at last index position, but it will give each value as one index inside
list

syntax
------
-->variable_name.extend(items)

eg
--
go = [1,2]
go.extend([3,4])
print(go)

eg
---
a = [2,3]
a.extend('python')
print(a)

pop()
----
-->pop() is used to remove items from the list and it will delete based on the index position

syntax
------
-->variable_name.pop(index_position)

eg
--
n = [1,2,3,4,]
n.pop(3)
print(n)

eg
--
a = [1,2,3,4,5,'python']
a.pop(5)
print(a)

remove()
-------
-->remove() will delete items based on the value given init..

syntax
-------
-->variable_name.remove(value)

eg
--
m = [1,2,3,4,5,6,'python']
m.remove(5)
print(m)

'''
prices = list(map(int,input().split()))
new_price = int(input())

prices.append(new_price)
prices.sort()

print(prices)
print(len(prices))










































































