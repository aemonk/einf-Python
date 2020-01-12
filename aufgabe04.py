# aufgabe04.py

#
# Bildet die Notenfunktion für die Tests aus der Vorlesung ab.
#
def Note_Tests( Test1, Test2, Test3):
    gesammtpunkte = Test1 + Test2 + Test3
    #print(gesammtpunkte)
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
    #return Note

if __name__ == "__main__":
    # Meine Tests, da stimmt was nicht!
    print( Note_Tests(5,5,5) ) # 5
    print( Note_Tests(40,10,5) ) # 4
    print( Note_Tests(40,30,5) ) # 3
    print( Note_Tests(40,40,5) ) # 2
    print( Note_Tests(40,40,40) ) # 1
