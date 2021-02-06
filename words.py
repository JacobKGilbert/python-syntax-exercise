def print_upper_words(words):
	'''Prints inputed words as all uppercase.'''
	for word in words:
		print(word.upper())

def print_upper_words_e(words):
	'''Print words only beginning with e in uppercase'''
	for word in words:
		if word.startswith('e') or word.startswith('E'):
			print(word.upper())

def print_upper_words_filtered(words, must_start_with):
	'''Print words only beginning with given letter in uppercase'''
	for word in words:
		for letter in must_start_with:
			if word.startswith(letter):
				print(word.upper())

print_upper_words(['hello', 'hey', 'goodbye', 'yo', 'yes'])
print_upper_words_e(['hello', 'ello'])
print_upper_words_filtered(["hello", "hey", "goodbye", "yo", "yes"],
					must_start_with={"h", "y"})