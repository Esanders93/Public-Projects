#  This program calculates different variables of a loan, given parameter inputs from the command line.
#  The variable calculated is the variable missing from the user's input

import math
import argparse

#  Defines parser to accept inputs via the command line
parser = argparse.ArgumentParser(description = "This program calculates missing variables of your differentiated loan")

parser.add_argument("--type", help = "Choose between 'annuity' payment or differentiated ('diff') payment.")

parser.add_argument("--principal", help = "Input your principal loan amount.")

parser.add_argument("--payment", help = "Input your monthly payment")

parser.add_argument("--periods", help = "Input the number of periods")

parser.add_argument("--interest", help = "Input your annual interest")

args = parser.parse_args()

parameters = [args.type, args.principal, args.payment, args.periods, args.interest]

counter = 0  # Defining counter to count "None" parameters
error = False  # Variable defined to check for input errors

if (args.type != "diff" and args.type!= "annuity"):  # Checks to see if loan type was inputted correctly
    error = True
    print("Type")

if args.type == "diff" and args.payment != None:  # Checks if user input constant payment and differtential payment type
    error = True

if args.interest == None:  # Checks for interest input
    error = True

for i in range(0, len(parameters)):  # Looping through list of parameters
    if parameters[i] != None:  # Checks for input in list
        counter += 1
        if "-" in parameters[i]:  # Checking to see if a "-" sign was incorrectly submitted
            error = True

if counter < 4:  # Tests if user input less than 4 parameters
    error = True

if error == True: print("Incorrect parameters")  # Lets user know that parameters were incorrectly submitted

if error == False:  # Runs loan calculations under the condition there are no input errors

    # Calculations for the annuity loan type
    if args.type == "annuity":

        # Calculates the payment given other parameters
        if args.payment == None:

            principal = int(args.principal)
            periods = int(args.periods)
            interest = float(args.interest)
            i = interest / 1200  # Interest is annual percentage rate, whereas i is monthly interest percentage

            # Calculates payment and overpayment
            payment = int(math.ceil(principal * ((i * ((1 + i) ** periods)) / ((1 + i) ** periods - 1))))
            overpayment = payment * periods - principal  # Calculates overpayment of loan due to final month's payment

            print(f"Your annuity payment = {payment}!")
            print(f"Overpayment = {overpayment}")


        # Calculates the length of the loan in periods (months) given other parameters
        elif args.periods == None:

            principal = int(args.principal)
            payment = int(args.payment)
            interest = float(args.interest)
            i = interest / 1200  # Interest is annual percentage rate, whereas i is monthly interest percentage
            periods = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
            years = periods // 12
            months = periods % 12
            if periods > 1 and years > 0 and months > 0:
                print(f"It will take {years} years and {months} months to repay this loan!")
            elif months == 0 and years > 0:
                print(f"It will take {years} years to repay the loan")
            else:
                print(f"It will take {periods} months to repay the loan")

            overpayment = periods * payment - principal # Calculates overpayment of loan due to final month's payment

            print(f"Overpayment = {overpayment}")

        # Calculates loan principal given other parameters
        else:

            periods = int(args.periods)
            payment = int(args.payment)
            interest = float(args.interest)

            i = interest / 1200  # Interest is annual percentage rate, whereas i is monthly interest percentage
            args.principal = math.ceil(payment / ((i * ((1 + i) ** periods)) / ((1 + i) ** periods - 1)))
            overpayment = payment * periods - args.principal

            print(f"Your loan principal = {args.principal}!")
            print(f"Overpayment = {overpayment}")

    # Calculations for the differentiated loan type
    if args.type == "diff":

        # Calculates the payment given other parameters
        if args.payment == None:

            principal = int(args.principal)
            periods = int(args.periods)
            interest = float(args.interest)
            i = interest / 1200  # Interest is annual percentage rate, whereas i is monthly interest percentage
            diff_payments = []
            payment_total = 0
            for m in range(1, periods + 1):
                diff_payment_m = math.ceil((principal / periods) + i * (principal - ((principal * (m - 1)) / periods)))
                print(f"Month {m}: payment is {diff_payment_m}")

                payment_total += diff_payment_m
                diff_payments.append(diff_payment_m)

            print(f"\nOverpayment = {payment_total - principal}")



        


