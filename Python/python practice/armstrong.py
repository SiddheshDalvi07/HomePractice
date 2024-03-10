def is_armstrong(n):
    temp = n
    sum = 0
    digit = len(str(n))

    while temp > 0:
        digits = temp % 10
        sum += digits** digit
        temp //= 10

    return sum == n

number = int(input("Enter the number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
