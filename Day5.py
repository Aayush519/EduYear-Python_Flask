#Adding Elements in List
numberOfValues = int(input("Enter number of values in list: "))
tempInput = numberOfValues
commonList = []
while (numberOfValues>0):
	listValue = int(input("Enter the integer you want to add in list: "))
	commonList.append(listValue)
	numberOfValues -= 1
print('\n')

#Q1: Determine Odd and Even Number
evenCount = 0
oddCount = 0
for i in range(tempInput):
	if(commonList[i]%2==0):
		evenCount += 1
	else:
		oddCount += 1
print("Count of Even Numbers:",evenCount)
print("Count of Odd Numbers:",oddCount)
print('\n')

#Q2: Find Max and Min of List
maxValue = commonList[0]
minValue = commonList[0]
for i in range(tempInput):
	if(maxValue<commonList[i]):
		maxValue = commonList[i]
	if(minValue>commonList[i]):
		minValue = commonList[i]
print("Maximum Value in List:",maxValue)
print("Minimum Value in List:",minValue)
print('\n')

#Q3: To Check Whether the list is palindrome or not
reversedList = []
reversedList.extend(commonList)
reversedList.reverse()
countPalindrome = 0
for i in range(len(commonList)):
	if(commonList[i]==reversedList[i]):
		countPalindrome +=1
	else:
		break
if(countPalindrome==tempInput):
	print("List {} is Palindrome".format(commonList))
else:
	print("List {} is not Palindrome".format(commonList))
print('\n')

#Q4: To Print Palindrome Number
for i in range(len(commonList)):
	if(commonList[i]==reversedList[i]):
		print("Palindrome Value:",commonList[i])
	else:
		break