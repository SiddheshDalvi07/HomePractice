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

try: 
    a = int(input("enter the number:"))
    b = int(input("enter the number:"))
    print(a/b)
except ZeroDivisionError as e:  
    print("you can't divide any number by zero")
    # print(e)
except ValueError as e:
    print("You should enter the integer value only")
except Exception as e:
    print("Something went wrong")
finally:
    print("resource closed")