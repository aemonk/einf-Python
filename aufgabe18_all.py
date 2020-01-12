# aufgabe18.py
'''
Hint: combine is really just two loop and add_event.

Schreiben Sie eine Klasse die Wahrscheinlichkeiten (probabilities) und Ereignisse (events) ver- waltet.
Verwenden Sie dazu ein dict mit Ereignis als key und der Wahrscheinlichkeit als Eintrag.
Keine Fehlerbehandlung nötig, Ereignisse sind immer immutables und Wahrscheinlichkeiten sind zahlen (float).
Das meiste ist unten erklärt, aber combine(self, other, how) ist etwas komplizierter.
how ist hier eine Funktion die zwei Ereignisse übernimmt, daraus eine neues macht, und dieses zurückgibt.
Zur korrekten Kombination von zwei Ereignisräumen muss man alle Ereignisse des einen (self) mit allen Ereignissen
des anderen (other) kombinieren, die Wahrscheinlichkeit der kombinierten Ereignisses ist die Multiplikation der beiden Wahrscheinlichkeiten.

Beispiel: Die Wahrscheinlichkeit das ich 1 würfle mit einem Würfel ist 1/6,
die Wahrscheinlich- keit das ich mit zwei Würfeln einen 1-er Pasch würfle ist 1/6*1/6.

Achtung: Es kann durch die Kombination von verschiedenen Events ein gleiches Event entstehen,
die Wahrscheinlichkeiten werden dann einfach addiert (siehe add_event).

Beispiel: Die Wahrscheinlichkeit mit zwei würfeln in Summe 3 zu würfeln ist die
Kombination von (1,2) und (2,1) mit je 1/6*1/6, also hat 3 die Wahrscheinlichkeit 1/36 + 1/36 = 5.55%.
'''

class PE:
    def __init__(self, initial_probabilities={}):
        # Soll initial probabilities übernehmen und speichern (achtung keine referenz speichern!)
        # Shall tak the initial_probabilities and store them
        pass

    def add_event(self, event, probability):
        # Fügt Ereigniss und Warhscheinlichkeit hinzu, gibt es das Event bereits wird die
        # Wahrscheinlichkeit zur vorigen addiert.
        # Add an event and probability, if the event exists sum up the probabilities
        pass

    def combine(self, other, how):
        #Kombiniere die Wahrschekeiten in einem neuen PE Objekt und gib es zurück
        #Combine the probabilities in a new PE object and return that
        pass
        #return ...

    def get_probabilities(self):
        # Gibt das dict mit den Event/Wahrscheinlichkeiten zurück (keine referenz)
        pass
        # return ...

    def __str__(self):
        return "\n".join(["{}: {:%}".format(se, sp) for se, sp in self.get_probabilities.items()])


# run the program
import operator

D6 = PE({
    1:1/6,
    2:1/6,
    3:1/6,
    4:1/6,
    5:1/6,
    6:1/6,
})

print("Roll one die")
print(D6)

print()
print("Roll two dice")
zwei = D6.combine(D6, operator.add)
print(zwei)

print()
print("Probability of the second die rolling higher than the first")
shtf = D6.combine(D6, lambda a, b: b > a)
print(shtf)



# OUTPUT
'''
Roll one die
1: 16.666667%
2: 16.666667%
3: 16.666667%
4: 16.666667%
5: 16.666667%
6: 16.666667%

Roll two dice
2: 2.777778%
3: 5.555556%
4: 8.333333%
5: 11.111111%
6: 13.888889%
7: 16.666667%
8: 13.888889%
9: 11.111111%
10: 8.333333%
11: 5.555556%
12: 2.777778%

Probability of the second die rolling higher than the first
False: 58.333333%
True: 41.666667%
'''
