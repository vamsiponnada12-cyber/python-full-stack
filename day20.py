'''
Modules
--------
1.built-in modules
-------------------
-->the modules are developed by programmer and those comes with installation

eg
---
1.match


2.os(location)
--------------
eg
---
import os
print(os.getcwd())

3.sys(system and version finding)
---------------------------------
eg
---
import sys
print(sys.path)
print(sys.version)

4.random(otp based)
-------------------
import random
print(random.randint(1000,9999))

2.user-defined modules
----------------------
-->

-->importing specific function from the module

syntax
------
-->from module import function

eg
---
from modules_practice import add_
print(add_(90,7))

eg
---
from modules_practice import pw
print(pw(2,4))


using alias name
----------------

syntax
-------
-->import modules as alias

eg
---
import modules_practice as mp
print(mp.add_(3,4))


'''
import math

correct_pin = "1234"
balance = 5000
access_granted = False


for i in range(3):
    pin = input().strip()
    
    if pin == correct_pin:
        access_granted = True
        print("Access Granted")
        
        withdrawal = float(input().strip())
        
        total_deduction = withdrawal + (withdrawal * 0.02)
        final_balance = math.floor(balance - total_deduction)
        
        print(final_balance)
        break

    else:
        print("Card Blocked")





















