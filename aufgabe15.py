# aufgabe15.py

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


def morse_encode(text, code_table):
	lst = []
	for i in text:
		x = i.upper()
		if x in code_table:
			y = code_table[x]
			lst.append(y)
	erg = " ".join(lst)
	return erg

	
if __name__ == '__main__':
	print(morse_encode('Hello World', CODE))
	print(morse_encode("1 3 3 7", CODE))