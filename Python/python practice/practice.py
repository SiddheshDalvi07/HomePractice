# def anagram(str1,str2):
#     s1 = ''.join(sorted(str1.lower()))
#     s2 = ''.join(sorted(str2.lower()))
#     if s1 == s2:
#         return "it is anagram"
#     else:
#         return "it is not anagram"

# str1 = input("enter the string 1 : ")
# str2 = input("enter the string 2 : ")
# print(anagram(str1,str2))


# def armstrong(num):
#     digit = len(str(num))
#     temp = num
#     sum = 0
    
#     while temp > 0:
#         digits = temp % 10
#         sum += digits** digit
#         temp //= 10

        
#     if sum == num:
#         return "it is an armstrong number"
#     else:
#         return "it is not an armstrong number"
    

# num = int(input("enter the number : "))
# print(armstrong(num))


# def armstrong(num):
#     digit = len(str(num))
#     sum = 0
    
#     for digits in str(num):
#         sum += int(digits) ** digit

#     if sum == num:
#         return "It is an Armstrong number"
#     else:
#         return "It is not an Armstrong number"
    

# num = int(input("Enter the number: "))
# print(armstrong(num))

# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact

# n = int(input("Enter the number: "))
# print(f'The factorial of {n} is {factorial(n)}')

# def fibonaci(n):
#     n1 = 0
#     n2 = 1
#     temp = 0
#     print(n1)
#     print(n2)
#     for i in range(1,n):
#         temp = n1 + n2
#         n1 = n2
#         n2 = temp
#         print(temp)     

# n = int(input("Enter the number: "))
# fibonaci(n)

# def palindrome(str):
#     str=str.lower()
#     length = len(str)
#     ispalindrome = "It is palindrome"
#     for i in range(length//2):
#         if str[i]!=str[length-i-1]:
#             ispalindrome= "It is not a palindrome"
#             break
#     return ispalindrome

# str = input("enter the string: ")
# print(palindrome(str))

# def foobar(n):
#     for i in range(1,n+1):
#         if i%3==0 and i%5==0:
#             print ("foobar")
#         elif i%3==0:
#             print ("foo")
#         elif i%5==0:
#             print ("bar")
#         else:
#             print (i)

# n = int(input("Enter the number: "))
# foobar(n)


# def anagram(str1,str2):
#     str1=str1.lower()
#     str2=str2.lower()
#     if len(str1)!=len(str2):
#         return False
    
#     count1 = {}
#     count2 = {}

#     for char in str1:
#         if char in count1:
#             count1[char]+=1
#         else:
#             count1[char]=1

#     for char in str2:
#         if char in count2:
#             count2[char]+=1
#         else:
#             count2[char]=1
    
#     return count1 == count2

# str1 = input("enter the string 1: ")
# str2 = input("enter the string 2: ")

# if anagram(str1,str2):
#     print("anagram")
# else:
#     print("not anagram")


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
        
# n = int(input("Enter the number: "))
# if prime(n):
#     print("prime")
# else:
#     print("not prime")

    
# print("Prime numbers between 1 and 100:")
# for number in range(1, 101):
#     if prime(number):
#         print(number, end=" ")    

# arr = [1,22,45,67,88]

# x = 45

# def linear(arr,x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i
#     return -1

# print(f'element {x} is present at index {linear(arr,x)}')

# def binary(arr,x):

#     low = 0 
#     high = len(arr)-1
#     mid = 0 


#     while low <= high:

#         mid = (high+low) // 2

#         if arr[mid] < x :
#             low = mid + 1

#         elif arr[mid] > x :
#             high = mid - 1

#         else:
#             return mid
        
#     return - 1


# arr = [23,34,1,34,55]
# x = 1


# if binary(arr,x) != -1:
#     print("Element is present at index",binary(arr,x))
# else:
#     print("Element is not present in array")
