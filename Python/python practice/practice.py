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


# def prime(n):



