def checkValidity(name, symbol):
	'''
	All chemical symbols must be exactly two letters, 
	so B is not a valid symbol for Boron.

	Both letters in the symbol must appear in the element name,
	but the first letter of the element name does not 
	necessarily need to appear in the symbol.
	So Hg is not valid for Mercury, but Cy is.

	The two letters must appear in order in the element name. 
	So Vr is valid for Silver, but Rv is not. 
	To be clear, both Ma and Am are valid for Magnesium, 
	because there is both an a that appears after an m, 
	and an m that appears after an a.

	If the two letters in the symbol are the same, 
	it must appear twice in the element name. 
	So Nn is valid for Xenon, but Xx and Oo are not.
	'''
	#Condition 1
	if len(symbol) != 2:
		return False

	#Condition 4 quick check
	if symbol[0].lower()==symbol[1].lower():
		count = 0
		for letter in name:
			if letter == symbol[0].lower():
				count += 1
		if count >= 2:
			return True

	#Condition 2
	for letter in symbol:
		if letter not in name:
			return False

	#Condition 3 and Condition 4
	idx=0
	for letter in name.lower():
		if letter == symbol[0].lower():
			substring = name[idx+1:]
			print substring
			if symbol[1] not in substring:
				return False
		else:
			idx += 1

	return True

print checkValidity('Venkmine', 'Kn')