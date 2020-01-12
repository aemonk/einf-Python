# aufgabe05.py


def NilakanthaFolge(i):
    try:
        if i > 0:
            ergebnis = ((-1)**(i-1))  *(4/((2*i)*(2*i+1)*(2*i+2)))
            return ergebnis
        elif type(i) == int and i == 0:
            return 3
        else:
            return 0
    except ZeroDivisionError:
        return 0
    except SyntaxError:
        return 0
    except TypeError:
        return 0
    

def NilakanthaReihe(N):
    if type(N) != int or N < 1:
        return 0
  
    else:
        for i in range(N):
            count = 0
            ergebnis = 0
            while count < N:
                a = NilakanthaFolge(count)
                count = count + 1
                ergebnis = ergebnis + a
            return ergebnis

        
if __name__ == '__main__':
    NilakanthaFolge(i)
    NilakanthaFolge(N)
#    print(NilakanthaFolge(False))
#    print(NilakanthaFolge("ASDF"))
#    print(NilakanthaFolge(-123.123))
#    print(NilakanthaFolge(-3))
#    print(NilakanthaFolge(0))
#    print(NilakanthaFolge(1))
#    print(NilakanthaFolge(2))
#    print(NilakanthaFolge(3))
#    print(NilakanthaFolge(4))    
#    print()
    
#    print(NilakanthaReihe(1))
#    print(NilakanthaReihe(2))
#    print(NilakanthaReihe(3))
