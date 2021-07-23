balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

#	minMonthlyPay = minMonthlyPayRate * previousBal
#	monthlyUnpaidBal = previousBal * minMonthlyPay
#updateBalEachMonth = montlyUnpaidBal + (monthlyInterestRate + monthlyUnpaidBal)

monthlyInterestRate = annualInterestRate / 12
remainingBal = balance * monthlyPaymentRate + monthlyInterestRate

