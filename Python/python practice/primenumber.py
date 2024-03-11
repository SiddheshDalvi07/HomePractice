# def primenumber(n):
#     if (n == 1 or n < 0):
#         print("neither composite nor prime number") 
#     elif (n ==2):
#         print("2 is a prime number")
#     else:
#         for i in range(2,n):
#             if(n%i ==0):
#                 print(f'{n} is not a prime number')
#                 break
#         else:   
#             print(f'{n} is a prime number')
               
       
                              

# num = int(input("Enter the number :"))
# primenumber(num)



def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

print("Prime numbers between 1 and 100:")
for number in range(1, 101):
    if is_prime(number):
        print(number, end=" ")
