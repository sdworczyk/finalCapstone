import math

#The formula for simple interest is: A = P*(1 + r*t)
#The formula for compound interest is: A = P * math.pow((1+r),t)
#'r' = interest rate, 'P' = deposit amount, 't' = number of years, 'A' = total amount after investment
#Bond repayment formula: = (i * P)/(1 - (1 + i)**(-n))
#'P' = preset value of the house, 'i' = monthly interest rate, 'n' = number of months in which the bond will be repaid

print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")

choice = input("Enter either investment or bond to proceed: ")
while choice.capitalize() != 'Investment' and choice.capitalize() != 'Bond':
    choice = input("Please choose investment or bond to proceed: ")

if choice.capitalize() == 'Investment':
    P = float(input("Please enter the amount of money you would like to deposit: "))
    while P <= 0:
        P = float(input("The deposit can't be less than or equal to zero. Please re-enter the amount you would like to invest: "))
    r = float(input("Please enter the interest rate as a percentage using only numbers: "))
    while (r <= 0):
        r = float(input("The interest rate can't be less than or equal to zero. Please re-enter the interest rate: "))
    t = int(input("Please enter the number of years you plan to invest: "))
    while (t <= 0):
        t = int(input("The number of years can't be less than or equal to zero. Please re-enter the number of years: "))

if choice.capitalize() == 'Investment':
    interest_type = input("Please choose which interest you would like to calculate. Simple or Compound?: ")
    while interest_type.capitalize() != 'Simple' and interest_type.capitalize() != 'Compound':
        interest_type = input("You can only choose between Simple and Compound interest calculators: ")
    if interest_type.capitalize() == 'Simple':
        A = P * (1 + (r / 100) * t)
        print(f"Simple Interest after {t} year/s: {A:.2f}")
    if interest_type.capitalize() == 'Compound':
        AC = P * math.pow((1 + r / (100)), t)
        print(f"Compound Interest after {t} year/s: {AC:.2f}")

if choice.capitalize() == 'Bond':
    PV = float(input("Please enter the preset value of the house: "))
    while PV <= 0:
        PV = float(input("The preset value can't be lower or equal to zero. Please re-enter the value: "))
    i = float(input("Please enter the interest rate: "))
    while i <= 0:
        i = float(input("The interest rate can't be lower or equal to zero. Please re-enter the interest rate: "))
    n = int(input("Please enter the number of months the bond will be repaid in: "))
    while n <= 0:
        n = int(input("The number of months can't be lower or equal to zero. Please re-enter the number of months: "))
    repayment = (i * PV)/(1 - (1 + (i))**(-n))
    print(f"Total monthly repayment after {n} months is: {(repayment/100)/12:.2f}." + f" Total repayment is: {repayment/100:.2f}.")

# The while loops prompt the user if an unacceptable value is entered and asks to re-enter it.