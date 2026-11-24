loopNumber = 0
counter = 0
average = 0
mainNumber = 0 
for number in range(100) :
	newnumber = int(input("Enter a number: "))
	newnumber += loopNumber
	counter += 1
	average = newnumber / counter
	if newnumber == -1:
		break
	print(average)
