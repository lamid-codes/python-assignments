
numberCollected = int(input("Enter a number: "))
count = 0
sumOfDigits = 0
reversedNumber = 0
extractedDigits = 0
while numberCollected != 0:
	extractedDigits = numberCollected % 10
	reversedNumber = (reversedNumber * 10) + extractedDigits
	count += 1
	sumOfDigits = sumOfDigits + extractedDigits
	numberCollected = numberCollected // 10
	if reversedNumber = numberCollected :
		print("Is a palindrome")
	else:
		print("is not a palindrome")