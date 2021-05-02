#Index Values of Vowels
word = input("Enter the string to check the vowel indexes: ")
tempWord = word.upper()
for i in (range(len(word))):
    if(tempWord[i]=='A' or tempWord[i]=='E' or tempWord[i]=='I' or tempWord[i]=='O' or tempWord[i]=='U'):
        print(i,end=' ')

#Reverse words of string
inputString = input("Enter the string which you want to reverse: ")
inputList = inputString.split(' ')
ouputList = inputList[::-1]
outputString = ' '.join(ouputList)
print(outputString)

#Remove Duplicate elements
numOfElem = int(input("Enter the number of elements in list: "))
inputList = []
outputList = []
while numOfElem>0:
    listValue = int(input("Enter the element: "))
    inputList.append(listValue)
    numOfElem -= 1

for i in range(len(inputList)):
    if i not in outputList:
        outputList.append(inputList[i])
print("\nOriginal List:",inputList)
print("Updated List without Duplicate Elements:",sorted(outputList))
