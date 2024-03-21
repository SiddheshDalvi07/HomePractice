#python core modules
#math module
import math               #1

m = math.factorial(5)
print(m)

m = math.pi  
print(m)

import math as mt           #2

m = mt.factorial(5)
print(m)

m = mt.pi  
print(m)

from math import factorial , pi        #3

m = factorial(5)
print(m)

m = pi  
print(m)

from math import *             #4

m = factorial(5)
print(m)

m = pi  
print(m)

print(math.pow(4,3))
print(math.sqrt(16))
print(math.ceil(4.5))
print(math.floor(4.5))
print(math.factorial(5))
print(math.gcd(9,24))          #greatest common divisor of two numbers
print(math.pi)                               
print(math.lcm(7,3))      #least common multiple                         

#datetime module
import datetime as dt
now = dt.datetime.now()     #1 Current date and time
print("Current date and time : ", now,type(dt)) 

dt1 = dt.datetime(2024,3,1,13,2,59,29)    #2 Datetime object
print("Datetime object:",dt1)
print(dt1.hour)
print(dt1.minute)
print(dt1.second)
print(dt1.microsecond)

date= dt.date.today()            #3 Today's Date
print("Today's Date is:",date)
print(date.month)
print(date.year)
print(date.day)

time1= now.time()                 #4 Time Now is
print("Time Now is:",time1)

date_after_2days = now + dt.timedelta(days=2)       #5 Date after 2 days using timedelta
print("Date after 2 days:",date_after_2days)

date_after_2days_3weeks = now + dt.timedelta(days=2,weeks=3)       #5 Date after 2 days and 3weeks using timedelta 
print("Date after 2 days and 3weeks:",date_after_2days_3weeks)

#strftime : it is format and represent date and time in string format
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")      #6
print("Formatted DateTime:", formatted_now)

formatted_date = date.strftime("%B %d,%Y")                     #7
print("Formatted Date:", formatted_date)

#%d  - Day of the month (e.g., 02)
#%m  - Month in digit  (e.g., 02 for February)
#%Y  - Year with century (e.g., 2009)
#%H  - Hour (00 to 23)
#%I  - Hour (01 to 12)
#%p  - AM/PM
#%M  - Minutes (00 to 59)
#%S  - Seconds (00 through 59) 
#%b  - Month  name in abbreviated form (e.g., Jan)
#%A  - Full weekday name (e.g., Sunday)
#%B  - Month  name in full form (February)
#%a  -  Abbreviated weekday name (e.g., Sun)

s = now.strftime("%a %d %m")
print(s)

s = now.strftime("%A %b %Y")
print(s)


#os module - used to deal with directories eg.  creating , deleting files or folders etc.
import os

print(os.getcwd())
# os.mkdir("NewFolder")   #creating a new folder named NewFolder
# os.rmdir("NewFolder")
# os.makedirs("folders2/subfolder1/subfolder2")    #recursively creates multiple sub-directories if they don’t exist already
# os.removedirs("folders2/subfolder1/subfolder2")
# os.rename("sample.txt","newname.txt")       # renaming file from sample.txt to newname.txt







#python external modules


#python user defined modules

def percentage(**kwargs):

    for sub in kwargs:

        # get argument name

        sub_name = sub

        # get argument value

        sub_marks = kwargs[sub]

        print(sub_name, "=", sub_marks)

        _ = dict(kwargs)

    print(_)

percentage(math=56, english=61, science=73)

def sum1(*args):
    s=0
    for i in args:
        s+=i
    print(s)

sum1(10,20,30,40,50,60)


def mul1(*args):
    m=1
    for i in args:
        m*=i
    print(m)

mul1(10,20,30)

def add(x,y):
    return x+y

def  subtract(x,y):
    return x-y

person = {"name":"rohan","age":21,"rollno":8}

x = 10

print("value of name ",__name__)


"""special variable __name__  is a builtin variable which holds the name of  the module. 
if the same module or program run then value of variable will be __main__ or as a module 
in other program run then value of variable will be filename 
"""

if  __name__ == '__main__':
    print("code executed as a program")
else:
    print("code executed as module")