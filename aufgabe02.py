
# aufgabe 2

# warenwert = 137

def verzollen(warenwert):
    steuer = 0
    zoll = 0
    if warenwert > 22:
        steuer = warenwert * 0.2
    if warenwert >= 150:
        zoll = warenwert * 0.17

    ergebnis = warenwert + steuer + zoll

    return ergebnis

if __name__ == '__main__':
    verzollen(warenwert)
