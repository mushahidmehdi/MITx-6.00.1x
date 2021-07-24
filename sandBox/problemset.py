#   s = 'abcdefghijklmnopqrstuvwxyz'
#   start = 0
#   newList = []
#   remaining = s
#   for i in range(len(s)-1):
#       if s[i+1] < s[i]:
#           end = i+1
#           newList.append(s[start:end])
#           start = end
#           remaining = s[start:]
#   newList.append(remaining)
#   print(newList) 
#   
#   l = ''
#   for i in newList:
#       if len(i) > len(l):
#           l = i
#   
#   print(l)
#   
#   


# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

#	minMonthlyPay = minMonthlyPayRate * previousBal
#	monthlyUnpaidBal = previousBal * minMonthlyPay
#updateBalEachMonth = montlyUnpaidBal + (monthlyInterestRate + monthlyUnpaidBal)

# month = 0
# monthlyInterstRate = annualInterestRate / 12
# while month < 12:
# 	minPayment = balance * monthlyPaymentRate
# 	balance = balance - minPayment
# 	interest = balance * (annualInterestRate / 12)
# 	balance = balance + interest
# 	month += 1
# 	print('Remaining balance: ' + "%.2f" % (balance))
#	print(balance)

#   month = 0
#   balance = 3329
#   original = balance
#   annualInterestRate = 0.2
#   minPayment = 10
#   while balance != 0 and balance > 0 :
#       minPayment += 10
#       balance = original
#       while month < 12:
#           month +=1
#           balance = balance - minPayment
#           interest = balance * (annualInterestRate / 12)
#           balance = balance + interest
#       month = 0
#   print(minPayment)

annualInterestRate = 0.2
balance = 3329

monthlyInterestRate = annualInterestRate / 12
init_bal = balance
upper_bound = (init_bal* (1 + monthlyInterestRate)**12) / 12
lower_bound =  init_bal/ 12
eplison = 0.03

while abs(balance) > eplison:
	monthlyPaymentRate = (upper_bound + lower_bound)/2
	balance = init_bal	
	for i in range(12):
		balance = balance - monthlyPaymentRate 
		interest = balance * monthlyInterestRate
		balance = balance + interest
	
	if balance > eplison:
		lower_bound = monthlyPaymentRate
	elif balance < -eplison:
		upper_bound = monthlyPaymentRate
	else:
		break

print("Lowest payment: " "%.2f"% monthlyPaymentRate)