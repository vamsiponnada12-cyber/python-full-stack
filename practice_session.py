'''

#price = 5000 #check the type(price)
#accessing input from the user
price = int(input('Enter a price: '))
#discount_= 0.1 #type(discount)
disc_= float(input('Entre the discount in betweeen 0.1 and 0.2: '))
gst = 0.18
final_price = price - (price*disc_)
final_price = final_price + (final_price*gst)
print(f'Final price is: {final_price} ')

#operators --> Arithmetic,Assignment,Comparision,Membership,Logical,Isentity,Bitwise

#Assignment --> = (assigns),+= (update the value)

price = 2000

price += 500
print(price)

#comparision --> = compare the values <, >, <=, >=, ==, !=

#membership --> in, not in --> its checks for the value in a collection

#we will have diff price -> diff discount ->gst same


prices = [15000,200,13000,25000,35000]

final_prices = []
#price <= 15000 then discount is 10%
#price >5000 --> to apply a discount
#price >20000 --> 15%
#get the final price in a list
for price in prices:
    if price<=15000 and price>5000:
     price = price-(price*0.1)
     final_prices.append(int(price))
     
    elif price>20000:
        price = price-(price*0.15)
        final_prices.append(int(price))
     
    elif price < 5000:
        final_prices.append(int(price))
print(final_prices)

        
-------------------------------------------------------------------------------------      

#students marks analyzer:
#for,while
##3 imp steps in program -->1)input 2)output 3)logic
#1.

marks = []
for mark in range(3):
    mark = int(input('Enter a number: '))
    marks.append(mark)
#print(marks)
marks.insert(0,90)
marks.extend([75,85])
#use a condition to check for 75, then remove it using
#remove()
if 75 in marks:
    marks.remove(75)
#remove final mark using pop() and display the
    #remove value.
print(marks.pop())
#print(marks)
#Display the final list and its length using len()
print('Final list of marks is',marks)
print('length of list is',len(marks))


--------------------------------------------------------------------------------
#1.
----------------
#students marks analyzer:
#for,while
##3 imp steps in program -->1)input 2)output 3)logic
#1.

marks = []
for mark in range(3):
    mark = int(input('Enter a number: '))
    marks.append(mark)
#print(marks)
marks.insert(0,90)
marks.extend([75,85])
#use a condition to check for 75, then remove it using
#remove()
if 75 in marks:
    marks.remove(75)
#remove final mark using pop() and display the
    #remove value.
print(marks.pop())
#print(marks)
#Display the final list and its length using len()
print('Final list of marks is',marks)
print('length of list is',len(marks))


#2.You have a list containing unsorted and repeated numbers.
----------------------------------------------------------------------------------------------------------------------------

numbers = [20,10,30,20,40,20]
print('sort listed is: ')
numbers.sort()
print(numbers)
print('descending order list: ')
numbers.reverse()
print(numbers)
number = int(input('Enter the number: '))
if number in numbers:
    print('count is: ',numbers.count(number))
    print('index position is: ',numbers.index(number))
else:
    print('number not found')
print('smallest number is :',min(numbers))
print('largest number is: ',max(numbers))
print('sum of all numbers is: ',sum(numbers))

-->
#3
----
numbers = [10,15,20,25,30,35]
even = []
odd = []
for number in numbers:
    if number%2==0:
        even.append(number)
    else:
         odd.append(number)
         
print(even)
print(odd)
print('first 3 elements: ',numbers[:3])
print('last 3 elements: ',numbers[-3:])
f = numbers.copy()
numbers.clear()
print('backup list is: ',f)
print('empty list is: ',numbers)


--------------------------------------------------------------------------------------------------------------


print("hello world")

#perform operation as below
a = 15
b = 25
print(a+b)

#Tokens--> keywords,variables,operators,pinctuators [],(),{}
#variables should not start with number,space,symbol,and no spacial char and no spac between words

batch = ['pfs-6','da-6']
print(batch)
print(type(batch)) #Everythin is an object(POP-->DOP)
#len()-->returns the number of itmes in a collection

print(len(batch))
#IDLE is colorcoding editor (voilet --> built-in functions)

#Add 3 more students names into it

#list --> collections --> append(), extend(), insert()

batch.append('vamsi')
print(batch)
batch.extend(['mani','nani'])
print(batch)
print(len(batch))


batch.insert(0,'sai') #inserts given value at sepicific index
print(batch)
print(len(batch))

batch.insert(-1,'python')#value before index
print(batch)
print(len(batch))

#Indexing --> [] --> index starts at 0 and ends at len(obj)-1
#Also in reverse manner it is -1 to len(obj)
#print(batch[0])
#print(batch[34]) #IndexError --> length is only 7 we are accessing extra

print(batch[:3])
print(batch[4:6])
#last 3 elements --> we prefer negative index values 
print(batch[-3:])
#first 3 elements
print(batch[:3])

#striding --> [start:end:step]

print(batch[::2]) #its skips 1 elements from start
print(batch[::3]) #its skips 2 elements from start
print(batch[1:5:2]) # first perform batch[1:5] --> then skip 1 element


---------------------------------------------------------------------- -------------------------------      


batch = ['sai','pfs-6','da-6','vamsi','akash','python','anil']
#print (batch[2:6:3]) # first 2:6 --> skip 2 elements
#print(batch[1:7:-2]) # in this case we come in reverse order
#print(batch[-1:4:-1])
#print(batch[-1:4:2])
#in above cases be careful while applying negative step count

#lets include tuplu in above list(tuples are immutable)

batch.insert(2,("vizag","hyd","vjy"))

print(batch)
print(len(batch))
#as we have a tuple inside a list
print(len(batch[2]))
print(batch[2][:2])#("vizag","hyd")
print(batch[2][1])# this returns 'hyd' --> string
print(batch[2][::2])
print(batch[2].index('hyd'))#tuple will have only count,index
#index --> first occurance
#count --> returns the count the objects
print(batch[2].count('codegnan'))#returns count as 0 and index will raise error, where as count will return 0

batch.insert(3,['pfs','da','jfs'])
print(batch)
#how let us apply some of list functions in above batch list
print(batch[3])
print(batch[3][1])
#to convert only jfs as upper case --> JFS
batch[3][2] = batch[3][2].upper()
print(batch[3][2])
#how we wanted to add a new coruse in batch[3] position --> MySQL
batch[3].append('CSS')
print(batch[3])
print(batch)

batch.remove('akash')
print(batch)

#remove --> value,pop --> index
#batch[2].remove('hyd')#raise AttributeError
#del batch[2][1] #tuple is immutable so we cant insert/remove
batch.clear()
print(batch)#we want remove entire data but keep thye list as it is --> clear()

-->

#lets work on dictionaries
#dict --> {k:v}, keys must be unique
#keys can be int, float, string, list
details = {}
#print(len(details))
details['batch'] = ['PFS_6']
#print(details)
details['course'] = ['python']
#print(details)
#print(len(details))
details['Students'] = ['sai','mani',]
#print(details)

#we want to update the dictionary
details.update({'branch':('Hyd','vizag'),
                'subjects':{'python','aptitude','softskills'}})
#print(details)
#print(len(details))
#first always check the type --> keys()
#keys(),values(),items()

print(details.keys())#return only keys
details['batch'].extend(['JFS','DA'])
print(details)
details['Students'].extend(['nani','ranjith'])
print(details)# here key should be checked

details['subjects'].add('DSA')#set is unique and unordered
print(details)


#task --> details --> list, set, dictionary

'''
































