count = 0
for count in range(1,100):
	count += 1
	number = int(input("Enter a number: "))
	if number < 1 and number > 100:
		continue
	if number >= 1 and number <= 100:
		print("Correct")