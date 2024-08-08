# def anagram(str1,str2):
#     s1 = str1.lower()
#     s2 = str2.lower()
#     if len(s1) != len(s2):
#         return False
    
#     count1 = {}
#     count2 = {}

#     for char in s1:
#         if char in count1:
#             count1[char]+=1
#         else:
#             count1[char]=1

#     for char in s2:
#         if char in count2:
#             count2[char]+=1
#         else:
#             count2[char]=1

#     return count1 == count2

# if anagram('listen','silen'):
#     print("its an anagram")
# else:
#     print("it is not")

# def armstrong(n):
#     temp = n
#     sum = 0 
#     digit = len(str(n))
#     while temp > 0 :
#         digits = temp%10
#         sum += digits**digit
#         temp = temp//10
#     return sum == n

# print(armstrong(153))

# def binarysearch(arr,x):
#     low = 0 
#     high = len(arr)-1
#     mid=0
#     while low <= high:
#         mid = (high+low)//2
#         if arr[mid] < x:
#             low = mid+1
#         elif arr[mid] > x:
#             high = mid - 1
#         else:
#             return mid
    
#     return -1

# print(binarysearch([2,3,4,10,40],10))

# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact
# print(factorial(5))  

# def fibonacci(n):
#     n1 = 0
#     n2 = 1
#     print(n1)
#     print(n2)
#     for i in range(1,n):
#         sum=n1+n2
#         print(sum)
#         n1 = n2
#         n2 = sum

# fibonacci(10)


# def foobar(n):
#     for i in range(1,n+1):
#         if (i%3==0 and i%5==0):
#             print("foobar")
#         elif (i%3==0):
#             print("foo")
#         elif (i%5==0):
#             print("bar")
#         else:
#             print(i)
        
# foobar(30)


# arr=[1,2,3,4,5,6,7]
# x=5
# def linearsearch(arr,x):
#     for i in range(len(arr)):
#         if arr[i]==x:
#             return i
#     return -1

# print(f'element {x} is present at index {linearsearch(arr,x)}')


# def palindrome(str):
#     string = str.lower()
#     length = len(string)
#     ispalindrome = True
#     for i in range(0,length//2):
#         if string[i] != string[length-i-1]:
#             ispalindrome = False
#             break
#     return ispalindrome

# print(palindrome("radar"))


# def prime(n):
#     if n<=1:
#         return False
#     elif n==2:
#         return True
#     else:
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#         return True
    
# for i in range(1,100):  
#     if prime(i):
#         print(i,end=' ')
    

# def reversenumber(n):
#     digit=len(str(n))
#     rev=0
#     while n>0:
#         rem=n%10
#         rev=rev*10+rem
#         n=n//10
#     return rev

# print(reversenumber(1234))

# def reversearray(arr):
#     reversed_arr = []
#     for i in range(len(arr)-1,-1,-1):
#         reversed_arr.append(arr[i])
#     return reversed_arr

# print(reversearray([1,2,3,4,5]))