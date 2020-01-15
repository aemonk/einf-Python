class PE:
    def __init__(self, initial_probabilities={}): # constructor
        # Soll initial probabilities übernehmen und speichern (achtung keine referenz speichern!)
        self.init_prob = initial_probabilities.copy()

    def add_event(self, event, probability): # method
        # Fügt Ereigniss und Warhscheinlichkeit hinzu, gibt es das Event bereits wird die
        # Wahrscheinlichkeit zur vorigen addiert.
        if event in self.init_prob:
            self.init_prob[event] += probability
        else:
            self.init_prob[event] = probability

    def combine(self, other, how): # method
        #Kombiniere die Wahrschekeiten in einem neuen PE Objekt und gib es zurück
        new_PE = PE()
        for schnitzel in self.init_prob:
            for pommes in other.get_probabilities():
                new_PE.add_event(how(schnitzel, pommes), self.init_prob[schnitzel] * other.get_probabilities()[pommes])
        return new_PE

    def get_probabilities(self): # method
        # Gibt das dict mit den Event/Wahrscheinlichkeiten zurück (keine referenz)
        return self.init_prob

    def __str__(self):
        return "\n".join(["{}: {:%}".format(se, sp) for se, sp in self.get_probabilities().items()])

     
# run program
D6 = PE({
    1:1/6,
    2:1/6,
    3:1/6,
    4:1/6,
    5:1/6,
    6:1/6,
})

import operator
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

franz = operator.add(5,5) # mit how(schnitzel, pommes)
print(franz)