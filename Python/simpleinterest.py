
# S.I = P * N *R 

def calculate_simple_interest(p, n, r):
    return p * n * r

set1_p = float(input("Enter the principal for set 1: "))
set1_n = float(input("Enter the number of years for set 1: "))
set1_r = float(input("Enter the annual interest rate for set 1: "))

set2_p = float(input("Enter the principal for set 2: "))
set2_n = float(input("Enter the number of years for set 2: "))
set2_r = float(input("Enter the annual interest rate for set 2: "))

set3_p = float(input("Enter the principal for set 3: "))
set3_n = float(input("Enter the number of years for set 3: "))
set3_r = float(input("Enter the annual interest rate for set 3: "))

interest1 = calculate_simple_interest(set1_p, set1_n, set1_r)
interest2 = calculate_simple_interest(set2_p, set2_n, set2_r)
interest3 = calculate_simple_interest(set3_p, set3_n, set3_r)

print(f"The simple interest for set 1 is {interest1}") #literals 
print("The simple interest for set 2 is",interest2)
print("The simple interest for set 3 is",interest3)