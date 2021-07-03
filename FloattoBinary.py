n = float(input("Enter a decimal number between 0-1: "))

p = 0

while ((2**p)*n)%1 != 0:
	p += 1
print("The value of p is " + str(p))


num = int((2**p)*n)
print("The int number is " + str(num))


result = ""
while (num > 0):
	result = str(num%2) + result
	num = num//2

print("The Result value is: " + str(result))

for i in range(p - len(result)):
	result = '0' + result

print("the length of result " + str(len(result)))

result = result[0:-p] + '.' + result[-p:]
print("The Binary represention of " + str(n) + " is " + str(result))
print(len(result))
