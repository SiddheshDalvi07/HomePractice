my_list = [1,2,3,4,5,6,7,8,9,10]
new_list= list(map(lambda x:x*2,my_list))
print(new_list)

my_list = [1,2,3,4,5,6,7,8,9,10]
new_list= list(map(lambda x:x*5,my_list))
print(new_list)

my_list = [1,2,3,4,5,6,7,8,9,10]
new_list= list(filter(lambda x:x*5,my_list))
print(new_list)

my_list=[1,2,3,4,5,6,7,8,9,10]
new_list = list(filter(lambda x:(x%2==0),my_list))
print(new_list)

def plus5(x):
    return lambda x: x + 5

f=plus5(10)
print(f(10))


my_list=[1,2,3,4,5,6,7,8,9,10]
even_list=list(filter(lambda x:(x%2==0),my_list))
odd_list=list(filter(lambda x:(x%2!=0),my_list))
print("Even List : ", even_list)
print("Odd List : ", odd_list)

from functools import reduce
my_list=[1,2,3,4,5,6,7,8,9,10]
sum_list=reduce(lambda x,y:x+y,my_list)
print("Sum of the elements in the list is :", sum_list)

my_list=[1,2,3,4,5,6,7,8,9,10]
sum_list=reduce(lambda x,y:x*y,my_list)
print("Muliplication of the elements in the list is :", sum_list)

list1= [1,2,3]
list2= [1,2,3]
list3=[]
for i in range(len(list1)):
    sum = list1[i]+list2[i]
    list3.append(sum)

print(list3)

list1= [1,2,3]
list2= [4,5,6]
list4 = list(map(lambda x:x,(list1+list2)))
print(list4)


##recursive function

def fact(n):
    if n == 0 or n == 1:
        return 1                          #to stop infinite loop
    else:
        return n * fact(n-1)
        
print(fact(5))


##recursive function
def count(n):
    print(n)
    if n == 10:
        return n                 #to stop infinite loop
    else:
        return count(n + 1)


count(1)


