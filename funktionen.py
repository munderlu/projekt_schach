felder = {1:"none", 2:"none", 3:"none", 4:"none", 5:"none", 6:"none", 7:"none", 8:"none", 9:"bauer1_w", 10:"bauer2_w", 11:"bauer3_w", 12:"bauer4_w", 13:"bauer5_w", 14:"bauer6_w", 15:"bauer7_w", 16:"bauer8_w", 17:"none", 18:"none", 19:"none", 20:"none", 21:"none", 22:"none", 23:"none", 24:"none", 25:"none", 26:"none", 27:"none", 28:"none", 29:"none", 30:"none", 31:"none", 32:"none", 33:"none", 34:"none", 35:"none", 36:"none", 37:"none", 38:"none", 39:"none", 40:"none", 41:"none", 42:"none", 43:"none", 44:"none", 45:"none", 46:"none", 47:"none", 48:"none", 49:"none", 50:"none", 51:"none", 52:"none", 53:"none", 54:"none", 55:"none", 56:"none", 57:"none", 58:"none", 59:"none", 60:"none", 61:"none", 62:"none", 63:"none", 64:"none"}

#Funktionen der acht weißen Bauern
def zeige_bauer (figur):
    figurgefunden=False
    figurPlatz="?"
    for i in felder:
        if felder[i][0:] == figur:
            figurPlatz=i
            figurgefunden=True
            break
    if figurgefunden:
        print("Die Figur kann nach ",figurPlatz+8,"fahren")
    else:
        print("Nein")