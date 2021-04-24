#Age Calculator
yearOfBirth = int(input("Enter Year Of Birth: "))
currentYear = int(input("Enter Current Year: "))
print("Age is:",currentYear-yearOfBirth,end=' years')

#Calculator
firstNumber = int(input("Enter First Number: "))
secondNumber = int(input("Enter Second Number: "))
print("Addition:",firstNumber+secondNumber)
print("Subtraction:",firstNumber-secondNumber)
print("Multiplication:",firstNumber*secondNumber)
print("Floor Division:",firstNumber//secondNumber)
print("Decimal Division:",firstNumber/secondNumber)
print("Remainder:",firstNumber%secondNumber)
print("{} Power of the {} :".format(secondNumber,firstNumber),firstNumber**secondNumber)

#'y' count calculator
userString=input("Enter any string which should only contain words:")
print("Count of 'y':",userString.count('y'))

#print even indexed number of string
userString=input("Enter any string which should only contain words: ")
print("Even indexed string:",userString[::2])