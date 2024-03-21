



def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def main():
    numbers = [2, 3, 4, 5]
    result = multiply(numbers)
    print(f"The multiplication of all the numbers in the list {numbers} is: {result}")

if __name__ == "__main__":
    main()