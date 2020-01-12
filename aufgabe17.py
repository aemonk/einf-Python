def morse_encode(text, code_table):
	return " ".join([code_table[character.upper()] for character in text if character.upper() in code_table])
