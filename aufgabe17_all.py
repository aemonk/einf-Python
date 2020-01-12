# aufgabe17.py
# write it in two lines of code

CODE1 = {'A': '.-', 'B': '-...', 'C': '-.-.',
				'D': '-..', 'E': '.', 'F': '..-.',
				'G': '--.', 'H': '....', 'I': '..',
				'J': '.---', 'K': '-.-', 'L': '.-..',
				'M': '--', 'N': '-.', 'O': '---',
				'P': '.--.', 'Q': '--.-', 'R': '.-.',
				'S': '...', 'T': '-', 'U': '..-',
				'V': '...-', 'W': '.--', 'X': '-..-',
				'Y': '-.--', 'Z': '--..',

				'0': '-----', '1': '.----', '2': '..---',
				'3': '...--', '4': '....-', '5': '.....',
				'6': '-....', '7': '--...', '8': '---..', '9': '----.'

}

CODE = {'W': '.......-', 'O': '.....-', 'E': '..-', 'R': '......-', 'L': '....-', 'H': '...-', ' ': '--', 'D': '.-'}
# test = ".... . .-.. .-.. --- .-- --- .-. .-.. -.."

# list comprehension and lambda
'''
def morse_encode(text, code_table):
	lst = []
	for i in text:
		x = i.upper()
		if x in code_table:
			y = code_table[x]
			lst.append(y)
	erg = " ".join(lst)
	return erg
'''
def morse_encode1(text, code_table):
	ret=""
	for character in text:
		if character.upper() in code_table:
			ret += " " + code_table[character.upper()]
	return ret.strip()

def morse_encode(text, code_table):
	return " ".join([code_table[character.upper()] for character in text if character.upper() in code_table])
	#return " ".join(b) #ret.strip()


if __name__ == '__main__':
	print(morse_encode('Hello World', CODE))
	print()
	print(morse_encode("1 3 3 7", CODE))
	print("List comprehension")
	print(morse_encode1('Hello World', CODE))
	print()
	print(morse_encode1("1 3 3 7", CODE))
