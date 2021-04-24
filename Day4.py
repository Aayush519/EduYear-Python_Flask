# Divisibility Test
rangeStart = int(input("Enter start value of range: "))
rangeEnd = int(input("Enter end value of range: "))
for i in range(rangeStart,rangeEnd+1):
	if(i%5==0 and i%7==0):
		print("Number '{}' divisible by both 5 & 7".format(i))
	elif(i%5==0):
		print("Number '{}' is divisible by 5".format(i))
	elif(i%7==0):
		print("Number '{}' is divisible by 7".format(i))
	else:
		print("Number '{}' neither divisible by 5 nor 7".format(i))
print("\n")


# Sum of Series
firstElement = "2"
total = 0
for i in range(1,6):
	total += int(firstElement*i)
print("Total of Series:",total)
print("\n")

# User Control Quit
total = 0
while True:
	userInput = input("Enter any number or 'q' to exit the program: ")
	if(userInput=='q'):
		print("Exiting Program...")
		break
	total += int(userInput)
print("Total:",total)
print("\n")	


# Factorial of a number
userInput = int(input("Enter any integer: "))
tempInput = userInput
total = 1
while (userInput in range(1,userInput+1)):
	total *= userInput
	userInput -= 1
print("Factorial of {} =".format(tempInput),total)