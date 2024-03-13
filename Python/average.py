a = int(input("Enter a string: "))
b = int(input("Enter a string: "))
c = int(input("Enter a string: "))

def average(a,b,c):
    return (a + b + c) / 3
print(f"The average of the three strings is {int(average(a,b,c))} ") 


"""f-strings (formatted string literals) allow you to embed expressions directly inside string literals, 
making it easy to format strings with variables or expressions. 
The expressions inside curly braces {} are evaluated and replaced with their values."""



