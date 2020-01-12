# aufgabe14.py

'''
horizontale = distanceTravelled ohne der Z Koordinate, range um 1 verringern
aufstieg = startpunkt kleiner als endpunkt
abstieg = startpunkt größer als endpunkt
zeit = 

Wie lange dauert die Tour in Stunden?
'''

'''
Entfernung pro Stunde:
300 Meter im Aufstieg.
500 Meter im Abstieg.
4 Kilometer Horizontalentfernung.

Die tatsächliche Gehzeit einer Strecke lässt sich errechnen, indem von den für Horizontal- und Vertikalentfernung errechneten Zeiten der kleinere Wert halbiert und zum größeren addiert wird.

Beispiel: Höhenunterschied: 900m — 900m/300m → 3 h Horizontalentfernung: 8 km — 8 km/4 km → 2 h

Ansatz: 2,0 h x 0,5 + 3,0 h = 4,0 h

Ergebnis: Die Gehzeit beträgt somit 4 h.

Beispiel 2: Wie Beispiel 1 aber mit Rückweg: 900m im Aufstieg (3h) und Abstieg (~1h 45m (1.8h)): 4h 45m 16km Horizontal: 4h

Ergebnis: 4h × 0.5 + 4h 45m = 6h 45m (Für uns 6.8h)
'''

points = [[0, 0, 0], 
				(344.42185152504817, 257.95440294030243, -31.77136766766199),
				(103.33860181801151, 269.22912430891097, -69.79771268749627),
				(387.1371908527841, 72.5418503878384, -79.15893102655394),
				(470.5192303078153, 480.65473558317353, -77.28418869959785),
				(252.35707470751913, 736.4589397403975, -29.936590029465208),
				(2.863416069959669, 1146.2051957086376, 163.177600385596),
				(313.0806520665492, 1548.3711461482203, 87.23662811332906),
				(542.9124003266779, 1947.2094341162137, 160.83020087950558),
				(515.0551157793913, 1547.9106421845795, 134.4989350610191),
				(625.9420892231929, 1960.9216954224776, 321.14148216932267)]


def sqrt_list(track):
	erg = 0
	for i in track: # for every element in the list
		sqrt = i ** 0.5 # squaroot the value i
		erg += sqrt # sum all values up
	return erg # give back the calculatet value in meter
	
	
def distanceTravelled(gpstrack): # horizontale
	lst = []
	try:
		for i in range(len(gpstrack)-1): # -1 = ohne z Werte
			# iterate over every element in the i-th list
			sum_of_values = 0 # x,y,z summed up
			for j in range(len(gpstrack[i])-1): # iterate over every j in list i
				q = gpstrack[i][j] # take list i value j
				p = gpstrack[i+1][j] # take next list value j
				expon = ((p)-(q))**2 # calculate the exponent of p-q
				sum_of_values += expon # sum all three values up
			lst.append(sum_of_values) # append this value to a list
		return sqrt_list(lst)
	except Exception:
		return 0
		
def heightAscended(gpstrack): #auf-/abstieg
	# Wie viele Meter der Strecke wurde im Aufstieg verbracht, in Meter
	# Ascent: 25.1286325643 m
	lst_aufstieg = []
	lst_abstieg = []
	try:
		for i in range(len(gpstrack)-1):
			# iterate over every element in the i-th list
			sum_aufstieg = 0
			sum_abstieg = 0
			for j in range(1): # iterate over every j in list i
				q = gpstrack[i][2] # take list i value j
				p = gpstrack[i+1][2] # take next list value j
				if q < p: #aufstieg 300m
					aufstieg = ((p)-(q))**2 # calculate the exponent of p-q
					# calculate
					sum_aufstieg += aufstieg # sum all three values up
				elif q > p: #abstieg 500m
					abstieg = ((p)-(q))**2 # calculate the exponent of p-q
					# 
					sum_abstieg += abstieg # sum all three values up
				else:
					continue
			#lst.append(sum_of_values) # append this value to a list
			lst_aufstieg.append(sum_aufstieg)
			lst_abstieg.append(sum_abstieg)
		meter_aufstieg = sqrt_list(lst_aufstieg)
		meter_abstieg = sqrt_list(lst_abstieg)
		aufstieg_abstieg = (meter_aufstieg, meter_abstieg)
		
		return aufstieg_abstieg
	except Exception:
		return 0

def plan(gpstrack):
	# time: 2.5437994087243254 h
	#for i in gpstrack:
	#	print(i)
	# aufstieg_abstieg tuple
	# aufstieg = 300m
	# abstieg = 500m
	# horizontal = 4000m
	vertikal_meter = heightAscended(gpstrack)
	horizontal_meter = distanceTravelled(gpstrack)
	vertikal = (vertikal_meter[0] / 300) + (vertikal_meter[1] / 500)
	horizontal = horizontal_meter / 4000
	if horizontal < vertikal:
		time = (horizontal * 0.5) + vertikal
		return time
	else:
		time = (vertikal * 0.5) + horizontal
		return time
	
	
	
if __name__ == '__main__':
	#plan(points)
	#print(distanceTravelled(points))
	#print(heightAscended(points))
	#leer = []
	#print(plan(points))
	#print(plan(leer))
	plan()
