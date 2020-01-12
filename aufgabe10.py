# aufgabe10.py


def Note_Tests(gesammtpunkte):
	Note = None
	if gesammtpunkte <= 50:
		Note = 5
		return Note
	if gesammtpunkte < 63:
		Note = 4
		return Note
	if gesammtpunkte < 76:
		Note = 3
		return Note
	if gesammtpunkte < 88:
		Note = 2
		return Note
	else:
		Note = 1
		return Note


def potential_top_marks(lst):
	'''potential_top_marks.
	Bekommt eine Liste mit Punkten der ersten Teilprüfung, ein Eintrag pro Teilnehmer. Angenommen auf allen
	weiteren Tests erhält jeder Teilnehmer die vollen Punkte: Wieviel % der Teilnehmer würden dann am Ende noch
	ein “Sehr Gut” bekommen können? Der Rückgabewert soll sein die Prozent im mathematischen Sinne, also
	zwischen 0 und 1.'''
	
	try:
		sehr_gut = 0  # wie viele Sehr Gut gibt es?
		kein_sehr_gut = 0  # wie viele keine Sehr Gut gibt es?
		prozent_sehr_gut = float()
	
		for punkte in lst:
			if punkte + 80 >= 88:
				sehr_gut += 1
			else:
				kein_sehr_gut += 1
			
		gesamtanzahl = sehr_gut + kein_sehr_gut
		prozent_sehr_gut = sehr_gut / gesamtanzahl

		return prozent_sehr_gut

	except Exception:
		n = 0
		return n
		
	
def no_improvement(lst):
	'''no_improvements. 
	Bekommt eine Liste mit Punkten der ersten Teilprüfung, ein Eintrag pro Teilnehmer. Angenommen keiner der
	Teilnehmer verbessert oder verschlechtert sich. Ge- benSie eine Liste mit Noten der jeweiligen Teilnehmer
	zurück, und zwar so das die i-te Note dem Teilnehmer mit den i-ten Punkten entspricht.'''
	
	marks = []  # leere liste für die Finalen no_improvement Noten
	try:
		for punkte in lst:
			endnote = punkte * 3
			try:
				ges_note = Note_Tests(endnote)
				marks.append(ges_note)
			except:
				pass

		return marks
		
	except Exception:
		pass


if __name__ == '__main__':
	potential_top_marks()
	no_improvement()
