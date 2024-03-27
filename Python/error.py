#syntax error, it will not execute the code
#prin("hello world"

#logical error, it will execute the code but it will not give correct output
# a=4
# b=10
# print(a+b+1)

#runtime  error, it will execute the code but it will give the error at the runtime
# a = int(input("enter the number:"))
# b = int(input("enter the number:"))
# print(a/b)
# ZeroDivisionError: division by zero

#exception handling
# try: 
#     a = int(input("enter the number:"))
#     b = int(input("enter the number:"))
#     print(a/b)
# except Exception as e:  
#     print("you can't divide any number by zero")
#     print(e)
# finally:
#     print("resource closed")

# try: 
#     a = int(input("enter the number:"))
#     b = int(input("enter the number:"))
#     print(a/b)
# except ZeroDivisionError as e:  
#     print("you can't divide any number by zero")
#     # print(e)
# except Exception as e:
#     print("Something went wrong")
# finally:
#     print("resource closed")

# try: 
#     a = int(input("enter the number:"))
#     b = int(input("enter the number:"))
#     print(a/b)
# except ZeroDivisionError as e:  
#     print("you can't divide any number by zero")
#     # print(e)
# except ValueError as e:
#     print("You should enter the integer value only")
# except Exception as e:
#     print("Something went wrong")
# finally:
#     print("resource closed")


class Division:
    def  __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def division(self):
        try:
            result = self.num1 / self.num2
            print(result)
        except ZeroDivisionError as e:  
            print("you can't divide any number by zero")
            
d1 = Division(5,0) 
d1.division()

d2 = Division(15,10) 
d2.division()