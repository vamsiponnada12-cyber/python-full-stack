'''
if statement
------------
elif
----
-->elif statement is used to check more possible outcomes or more conditions

eg
---
a = 90
b = 780
c = 67
if a>b and a>c:
   print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
eg
--
num = 7
num_2 = 3
user_opt = int(input('Enter \n1.add \n2.sub \n3.mul \n4.pow'))
if user_opt == 1:
    print(num + num_2)
elif user_opt == 2:
    print(num - num_2)
elif user_opt == 3:
    print(num * num_2)
else:
    print(num ** num_2)

nested if
---------
-->if inside an if statement is called nested if

eg
---
app_details = {'pin':1234}
import random
user_pass = int(input('Enter your password: '))
otp = random.randint(1000,9999)
if user_pass == app_details['pin']:
    print('password is correct')
    print(otp)
    user_otp = int(input('Enter 4 digit otp: '))
    if user_otp == otp:
        print('welcome to the app')
    else:
        print('incorrect otp')
else:
    print('password is incorrect')


eg
--
a = int(input("Entre a number: "))
if a%2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')


'''
marks_ = int(input("Enter ur marks: "))
if marks_>90:
    print('A+')
elif marks_>80:
    print('A')
elif marks_>70:
    print('B+')
elif marks_>60:
    print('B')
elif marks_>50:
    print('c')






























































































