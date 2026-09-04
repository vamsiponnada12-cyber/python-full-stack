'''
strings
--------

operations
-----------

indexing
--------
-->indexing is used to get char that you looking to access
types
-----
1.positive indexing
-------------------
-->positive indexing starts from 0 index

syntax
------
-->print(variable_name[index_position])
eg
---
txt = 'vamsi'
print(txt[3])

2.negative indexing
-------------------
-->negative indexing starts from -1 index

syntax
------
-->print(variable_name[negative index_position])
eg
--
txt = 'vamsi'
print(txt[-1])

len()
-----
-->len() is a built-in function that is used to get number of char present in the string
syntax
------
-->len(variable_name)
eg
--
txt = 'python is a programming language'
print(len(txt))

slicing
--------
-->this used to access the particular part from the string
syntax
------
-->variable_name[start:end]
eg
---
txt = 'python is a programming language'
print(txt[12:])
print(txt[:13])
print(txt[12:13])


txt = 'madam'
rev = txt[::-1]
print(rev)

upper()
-------
-->uper to convert all small char to capital cahr
eg
--
txt = 'python is a programming language'
print(txt.upper())


lower()
-------
-->used to convert all cap into small
eg
--
txt = 'PYTHON'
print(txt.lower())


inex()
------
-->index is used to know the index position of an char

eg
--
txt = 'python is a programming language'
print(txt.index('i',9))

replace()
---------
-->used to replace the orginal to duplicate
eg
--
txt = 'python is a programming language'
print(txt.replace('python','java'))


split()
-------
-->this method is use to superate the string based on given substring
eg
---
txt = 'python is a programming language'
print(txt.split(' '))


count()
-------
-->






'''
txt = 'python is a programming language'
print(txt.count('a',1,26))





































































