def exchange_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

num1 = 10
num2 = 20
print("Before swapping:", num1, num2)
num1, num2 = exchange_without_temp(num1, num2)
print("After swapping:", num1, num2)



