import math
import argparse


def calculate_months(principal, monthly_payment, interest):
    nominal_interest = calculate_nominal_interest(interest)
    x = monthly_payment / (monthly_payment - nominal_interest * principal)
    months_required = math.ceil(math.log(x, 1 + nominal_interest))
    years = math.floor(months_required / 12)
    months = months_required % 12

    if years > 0 and months > 0:
        print(f"It will take {years} years and {months} months to repay this loan!")
    else:
        time_str = f"{years} years" if years > 0 else f"{months} months"
        print(f"It will take {time_str} to repay this loan!")
    overpaid = math.ceil(monthly_payment * months_required - principal)
    print(f"Overpayment = {overpaid}")


def calculate_monthly_payment(principal, number_of_months, interest):
    nominal_interest = calculate_nominal_interest(interest)
    monthly_payment = math.ceil(principal * ((nominal_interest * (1 + nominal_interest) ** number_of_months) /
                                             ((1 + nominal_interest) ** number_of_months - 1)))
    overpaid = math.ceil(monthly_payment * number_of_months - principal)
    print(f"Your monthly payment = {monthly_payment}")
    print(f"Overpayment = {overpaid}")


def calculate_nominal_interest(interest):
    nominal_interest = interest / (12 * 100)
    return nominal_interest


def calculate_principal(monthly_payment, interest, number_of_months):
    nominal_interest = calculate_nominal_interest(interest)
    result = monthly_payment / (
            (nominal_interest * (1 + nominal_interest) ** number_of_months) /
            ((1 + nominal_interest) ** number_of_months - 1))
    return math.ceil(result)


def calculate_differentiate_payment(principal, periods, interest):
    nominal_interest = calculate_nominal_interest(interest)
    total_paid = 0
    for i in range(1, periods + 1):
        payment = math.ceil((principal / periods
                             + nominal_interest * (principal - ((principal * (i - 1)) / periods))))
        total_paid = total_paid + payment
        print(f"Month {i}: payment is {payment}")
    overpaid = math.ceil(total_paid - principal)
    print(f"Overpayment = {overpaid}")


def is_positive_number(value):
    return value is not None and value > 0


parser = argparse.ArgumentParser()
parser.add_argument("--payment", type=float, required=False, help="Monthly payment amount")
parser.add_argument("--principal", type=int, required=False, help="Loan principal")
parser.add_argument("--periods", type=int, required=False, help="Number of months to repay")
parser.add_argument("--interest", type=float, required=False, help="Annual interest rate")
parser.add_argument("--type", type=str, required=False, help="Type of payment calculation")

args = parser.parse_args()

if args.type not in ("diff", "annuity") or args.interest is None:
    print("Incorrect parameters")
elif args.type == "diff":
    if args.payment is not None or not all(map(is_positive_number, [args.principal, args.periods, args.interest])):
        print("Incorrect parameters")
    else:
        calculate_differentiate_payment(args.principal, args.periods, args.interest)
elif args.type == "annuity":
    if args.periods is None:
        if args.payment <= 0:
            print("Incorrect parameters")
        calculate_months(args.principal, args.payment, args.interest)
    elif args.payment is None:
        calculate_monthly_payment(args.principal, args.periods, args.interest)
    elif args.principal is None:
        loan_principal = calculate_principal(args.payment, args.interest, args.periods)
        print(f"Your loan principal = {loan_principal}!")
