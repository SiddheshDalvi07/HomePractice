



def calculate_monthly_payment(loan_amount, years, annual_interest_rate):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    num_payments = years * 12
    monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / ((1 + monthly_interest_rate) ** num_payments - 1)
    return monthly_payment

def main():
    loan_amount = float(input("Enter the loan amount: $"))
    years = int(input("Enter the number of years: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in percentage): "))
    monthly_payment = calculate_monthly_payment(loan_amount, years, annual_interest_rate)
    print(f"\nFor a loan amount of ${loan_amount:.2f} over {years} years with an annual interest rate of {annual_interest_rate:.2f}%, the monthly payment is: ${monthly_payment:.2f}")

if __name__ == "__main__":
    main()
