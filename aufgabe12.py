# aufgabe12.py


test_list = [[0, 0, 0], 
						[6.888437030500963, 5.159088058806049, -1.5885683833831],
						[2.0667720363602307, 5.384582486178219, -3.4898856343748133],
						[7.742743817055683, 1.4508370077567676, -3.957946551327696],
						[9.410384606156306, 9.613094711663472, -3.864209434979891],
						[5.047141494150383, 14.72917879480795, -1.4968295014732576],
						[0.05726832139919402, 22.924103914172754, 8.158880019279806],
						[6.261613041330982, 30.96742292296441, 4.361831405666459],
						[10.858248006533554, 38.94418868232428, 8.041510043975286],
						[10.30110231558782, 30.958212843691598, 6.724946753050958],
						[12.518841784463852, 39.21843390844956, 16.057074108466132]]
	
short_list = [[0, 0, 0], 
						[6.888437030500963, 5.159088058806049, -1.5885683833831]]

empty_list = []
					
def distanceTravelled(gpstrack):
	'''
	Sie bekommen eine List mit Fake GPS-Koordinaten, jeweils eine x,y und z Koordinate
	in dieser Reihenfolge als Liste (siehe Beispiel). 
	Wir nehmen die folge der Koordinaten beschreibt eine Wanderung. 
	Die Koordinaten sind absolut zu sehen und in Meter gegeben. 
	Es wird alle zwei Sekunden ein Punkt aufgenommen.

	Schreiben Sie eine Funktion die diese Liste als Eingabe bekommen.

	distanceTravelled( gpstrack): Soll die gesamte Strecke die dieser GPS-Track beschreibt berechnen
	und zurückgeben (in Meter). 
	Zwischen den Punkten soll der direkte Weg angenommen werden (Pythagoras).

	Es wird in jedem Fall eine Liste übergeben 
	die allerdings beliebig viele Punkte enthalten kann, auch 0.
	'''
	erg = 0 # ergebnis
	lst = []
	for i in range(len(gpstrack)-1):
		# iterate over every element in the i-th list
		sum_of_values = 0 # x,y,z summed up
		for j in range(len(gpstrack[i])): # iterate over every j in list i
			q = gpstrack[i][j] # take list i value j
			p = gpstrack[i+1][j] # take next list value j
			expon = ((p)-(q))**2 # calculate the exponent of p-q
			sum_of_values += expon # sum all three values up
		lst.append(sum_of_values) # append this value to a list
		
	for i in lst: # for every element in the list
		sqrt = i ** 0.5 # squaroot the value i
		erg += sqrt # sum all values up
	return erg # give back the calculatet value in meter

	

	
if __name__ == '__main__':
	distanceTravelled()
	#print(distanceTravelled(test_list))
	#print(distanceTravelled(short_list))
	#print(distanceTravelled(empty_list))
	
