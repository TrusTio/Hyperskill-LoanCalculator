import math
import argparse


def calculate_months(principal, monthly_payment, interest):
    nominal_interest = calculate_nominal_interest(interest)
    x = monthly_payment / (monthly_payment - nominal_interest * principal)
    months_required = math.log(x, 1 + nominal_interest)
    return math.ceil(months_required)


def calculate_monthly_payment(principal, number_of_months, interest):
    nominal_interest = calculate_nominal_interest(interest)
    monthly_payment = math.ceil(principal * ((nominal_interest * (1 + nominal_interest) ** number_of_months) /
                                    ((1 + nominal_interest) ** number_of_months - 1)))
    return monthly_payment


def calculate_nominal_interest(annual_interest):
    nominal_interest = annual_interest / (12 * 100)
    return nominal_interest


def calculate_principal(monthly_payment, interest, number_of_months):
    nominal_interest = calculate_nominal_interest(interest)
    principal = monthly_payment / (
                (nominal_interest * (1 + nominal_interest) ** number_of_months) /
                ((1 + nominal_interest) ** number_of_months - 1))
    return math.ceil(principal)

parser = argparse.ArgumentParser()
parser.add_argument("--payment", type=float, required=False)
parser.add_argument("--principal", type=int, required=False)
parser.add_argument("--periods", type=int, required=False)
parser.add_argument("--interest", type=float, required=True)

args = parser.parse_args()

if args.periods is None:
    total_months = calculate_months(args.principal, args.payment, args.interest)
    years = math.floor(total_months / 12)
    months = total_months % 12

    if years > 0 and months > 0:
        print(f"It will take {years} years and {months} months to repay this loan!")
    else:
        time_str = f"{years} years" if years > 0 else f"{months} months"
        print(f"It will take {time_str} to repay this loan!")
elif args.payment is None:
    monthly_payment = calculate_monthly_payment(args.principal, args.periods, args.interest)
    print(f"Your monthly payment = {monthly_payment}")
elif args.principal is None:
    loan_principal = calculate_principal(args.payment, args.interest, args.periods)
    print(f"Your loan principal = {loan_principal}!")
