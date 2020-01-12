# aufgabe08.py
def fancy(was="Rechts", minlen=20, align="rechts", underline=False):
	
	# align all: links, mitte, default: rechts
	# strip whitespace and make lowercase string
	align = align.strip().lower()

	# format variables
	links_ = "{0:<{w}}\n".format(was, w=minlen)
	mitte_ = "{0:^{w}}\n".format(was, w=minlen)
	rechts_ = "{0:>{w}}\n".format(was, w=minlen)
	
	if align == "links":
		ergebnis = links_
		
	elif align == "mitte":
		ergebnis = mitte_
	
	else:
		ergebnis = rechts_
	
	if underline == True:
		# make underline
		x = ""
		for i in range(len(ergebnis)-1):
			x = x + "="
	
		# format the "=" string
		under_ = "{}\n".format(x)
		
		if align == "mitte":
			ergebnis = mitte_ + under_
		
		elif align == "links":
			ergebnis = links_ + under_
				
		else:
			ergebnis = rechts_ + under_
				
	return ergebnis
		
print(fancy("HRpXN", 20, "lInkS", True))
print(fancy("NlQpj", 25, "ReChtS ", True))
#print(fancy("h3Pz7", 14, " miTTe", True))
#print(fancy("9bSEO", 10, "LINkS", True))
#print(fancy("QQMFXPE", 3, "LINks", True))
#print(fancy("OPAmV", 4, "wAs?", True))
