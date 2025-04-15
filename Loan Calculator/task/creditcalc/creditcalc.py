import math
def calculate_months(principal, monthly_payment):
    months_required = math.ceil(principal / monthly_payment)
    print(f"It will take {months_required} months to repay the loan")

def calculate_monthly_payment(principal, number_of_months):
    monthly_payment = math.ceil(principal / number_of_months)
    if monthly_payment * number_of_months > principal:
        last_payment = principal - (monthly_payment * (number_of_months - 1))
        print(f"Your monthly payment = {monthly_payment} and the last payment = {last_payment}")
    else:
        print(f"Your monthly payment = {monthly_payment}")

principal = int(input("Enter the loan principal: "))
user_choice = input("""What do you want to calculate? 
type "m" for number of monthly payments,
type "p" for the monthly payment:
""")

if user_choice == "m":
    monthly_payment = int(input("Enter the monthly payment: "))
    calculate_months(principal, monthly_payment)
else:
    number_of_months = int(input("Enter the number of months: "))
    calculate_monthly_payment(principal, number_of_months)
