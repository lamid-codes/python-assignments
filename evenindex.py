count = 0
character = input("Enter a word: ")
for char in character:
	if count % 2 == 0:
		print(char)
	count += 1