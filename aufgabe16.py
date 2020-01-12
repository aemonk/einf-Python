# aufgabe16.py

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
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

CODE1 = {'W': '.......-', 'O': '.....-', 'E': '..-', 'R': '......-', 'L': '....-', 'H': '...-', ' ': '--', 'D': '.-'}
# test = ".... . .-.. .-.. --- .-- --- .-. .-.. -.."

def morse_decode(text, code_table):
	new_table = dict(map(reversed, code_table.items()))
	text = text.split(" ")
	lst = []
	for i in text:
		if i in new_table:
			lst.append(new_table[i])
	
	return "".join(lst)

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
	print(morse_decode(morse_encode("Hello World", CODE), CODE))
