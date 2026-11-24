character = input("Enter a word: ")
count = 0
counted = ""
for char in character :
	vowel_sample = 'aeiou'
	if char in vowel_sample and char not in counted:
		count += 1
		counted += char
print(count)