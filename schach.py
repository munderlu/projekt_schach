from tkinter import *
from PIL import ImageTk, Image
fenster = Tk()
fenster.title("Schach Projekt")
rahmen=Frame(fenster, relief="ridge", borderwidth=5)
rahmen.pack()
schachbrett_bild = ImageTk.PhotoImage(Image.open("Bilder\Schachbrett.png"))
schachbrett = Label(rahmen, image=schachbrett_bild)
schachbrett.pack(expand=True, padx=30, pady=30)

class Schachfigur(Button):
    farbe="?"

moegliche_ziele={1:{"platz": "none", "x":"none", "y":"none"}, 2:{"platz": "none", "x":"none", "y":"none"}, 3:{"platz": "none", "x":"none", "y":"none"}, 4:{"platz": "none", "x":"none", "y":"none"}, 5:{"platz": "none", "x":"none", "y":"none"}, 6:{"platz": "none", "x":"none", "y":"none"}, 7:{"platz": "none", "x":"none", "y":"none"}, 8:{"platz": "none", "x":"none", "y":"none"}, 9:{"platz": "none", "x":"none", "y":"none"}, 10:{"platz": "none", "x":"none", "y":"none"}, 11:{"platz": "none", "x":"none", "y":"none"}, 12:{"platz": "none", "x":"none", "y":"none"}, 13:{"platz": "none", "x":"none", "y":"none"}, 14:{"platz": "none", "x":"none", "y":"none"}, 15:{"platz": "none", "x":"none", "y":"none"}, 16:{"platz": "none", "x":"none", "y":"none"}, 17:{"platz": "none", "x":"none", "y":"none"}, 18:{"platz": "none", "x":"none", "y":"none"}, 19:{"platz": "none", "x":"none", "y":"none"}, 20:{"platz": "none", "x":"none", "y":"none"}, 21:{"platz": "none", "x":"none", "y":"none"}, 22:{"platz": "none", "x":"none", "y":"none"}, 23:{"platz": "none", "x":"none", "y":"none"}, 24:{"platz": "none", "x":"none", "y":"none"}, 25:{"platz": "none", "x":"none", "y":"none"}, 26:{"platz": "none", "x":"none", "y":"none"}, 27:{"platz": "none", "x":"none", "y":"none"}}

def setzeZieleAufNull():
    global moegliche_ziele
    moegliche_ziele={1:{"platz": "none", "x":"none", "y":"none"}, 2:{"platz": "none", "x":"none", "y":"none"}, 3:{"platz": "none", "x":"none", "y":"none"}, 4:{"platz": "none", "x":"none", "y":"none"}, 5:{"platz": "none", "x":"none", "y":"none"}, 6:{"platz": "none", "x":"none", "y":"none"}, 7:{"platz": "none", "x":"none", "y":"none"}, 8:{"platz": "none", "x":"none", "y":"none"}, 9:{"platz": "none", "x":"none", "y":"none"}, 10:{"platz": "none", "x":"none", "y":"none"}, 11:{"platz": "none", "x":"none", "y":"none"}, 12:{"platz": "none", "x":"none", "y":"none"}, 13:{"platz": "none", "x":"none", "y":"none"}, 14:{"platz": "none", "x":"none", "y":"none"}, 15:{"platz": "none", "x":"none", "y":"none"}, 16:{"platz": "none", "x":"none", "y":"none"}, 17:{"platz": "none", "x":"none", "y":"none"}, 18:{"platz": "none", "x":"none", "y":"none"}, 19:{"platz": "none", "x":"none", "y":"none"}, 20:{"platz": "none", "x":"none", "y":"none"}, 21:{"platz": "none", "x":"none", "y":"none"}, 22:{"platz": "none", "x":"none", "y":"none"}, 23:{"platz": "none", "x":"none", "y":"none"}, 24:{"platz": "none", "x":"none", "y":"none"}, 25:{"platz": "none", "x":"none", "y":"none"}, 26:{"platz": "none", "x":"none", "y":"none"}, 27:{"platz": "none", "x":"none", "y":"none"}}
    for i in ziele:
        i.place_forget()

weristdran="weiß"

def zuege_bauer_weiß(figur_name):
    def punktBewegtBauerWeiß(punkt_name):
        felder[figurPlatz]["figure"]="none"
        print(moegliche_ziele[punkt_name], punkt_name)
        if felder[moegliche_ziele[punkt_name]["platz"]]["figure"]!="none":
            geschlageneFiguren.append(felder[moegliche_ziele[punkt_name]["platz"]]["figure"])
        felder[moegliche_ziele[punkt_name]["platz"]]["figure"]=figur_name
        plazieren("figuren")
        setzeZieleAufNull()
        global weristdran
        weristdran="schwarz"
    global weristdran
    if weristdran=="weiß": #nur wenn weiß dran ist, passiert was
        setzeZieleAufNull()
        plazieren("ziele")
        figurgefunden=False
        figurPlatz="?"
        for i in felder: #das Dictionary mit den Feldern wird durchsucht
            if felder[i]["figure"] == figur_name: #wenn die Figur gefunden wurde
                figurPlatz=i
                print(figurPlatz)
                moegliche_ziele[1]["platz"] = figurPlatz+8
                if felder[moegliche_ziele[1]["platz"]]["figure"]=="none": #es wird geprüft, ob auf dem Feld eine Figur steht
                    figurgefunden=True
                    moegliche_ziele[1]["x"]=felder[moegliche_ziele[1]["platz"]]["x"]
                    moegliche_ziele[1]["y"]=felder[moegliche_ziele[1]["platz"]]["y"]
                    punkt2.place_forget()
                    punkt3.place_forget()
                    punkt1["command"]=lambda: punktBewegtBauerWeiß(1)#ein Punkt wird platziert
                    plazieren("ziele")
                if figurPlatz >= 9 and figurPlatz <=16: #wenn der Bauer auf der zweiten Reihe steht, wird noch ein zweiter Punkt hinzugefügt
                    moegliche_ziele[2]["platz"] = figurPlatz+16
                    if felder[moegliche_ziele[1]["platz"]]["figure"]=="none": #es wird geprüft, ob auf dem Feld eine Figur steht
                        moegliche_ziele[2]["x"]=felder[moegliche_ziele[2]["platz"]]["x"]
                        moegliche_ziele[2]["y"]=felder[moegliche_ziele[2]["platz"]]["y"]
                        punkt2["command"]=lambda: punktBewegtBauerWeiß(2)
                        plazieren("ziele")
                figurX=felder[figurPlatz]["x"]
                figurY=felder[figurPlatz]["y"]
                for j in felder:
                    if felder[j]["y"]==figurY-47 and felder[j]["x"]==figurX-47:
                        moegliche_ziele[3]["platz"]=j
                        if felder[j]["figure"]!="none":
                            if felder[j]["figure"].farbe=="schwarz":
                                figurgefunden=True
                                moegliche_ziele[3]["x"]=felder[j]["x"]
                                moegliche_ziele[3]["y"]=felder[j]["y"]
                                punkt3["command"]=lambda: punktBewegtBauerWeiß(3)
                                plazieren("ziele")
                for k in felder:
                    if felder[k]["y"]==figurY-47 and felder[k]["x"]==figurX+47:
                        moegliche_ziele[4]["platz"]=k
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe=="schwarz":
                                figurgefunden=True
                                moegliche_ziele[4]["x"]=felder[k]["x"]
                                moegliche_ziele[4]["y"]=felder[k]["y"]
                                punkt4["command"]=lambda: punktBewegtBauerWeiß(4)
                                plazieren("ziele")
                                break
        if figurgefunden:
            print("Die Figur kann fahren")
        else:
            print("Nein")

def zuege_bauer_schwarz(figur_name):
    def punktBewegtBauerSchwarz(punkt_name):
        felder[figurPlatz]["figure"]="none"
        print(moegliche_ziele[punkt_name], punkt_name)
        if felder[moegliche_ziele[punkt_name]["platz"]]["figure"]!="none":
            geschlageneFiguren.append(felder[moegliche_ziele[punkt_name]["platz"]]["figure"])
        felder[moegliche_ziele[punkt_name]["platz"]]["figure"]=figur_name
        plazieren("figuren")
        setzeZieleAufNull()
        global weristdran
        weristdran="weiß"
    global weristdran
    if weristdran=="schwarz": #nur wenn schwarz dran ist, passiert was
        setzeZieleAufNull()
        plazieren("ziele")
        figurgefunden=False
        figurPlatz="?"
        for i in felder: #das Dictionary mit den Feldern wird durchsucht
            if felder[i]["figure"] == figur_name: #wenn die Figur gefunden wurde
                figurPlatz=i
                print(figurPlatz)
                moegliche_ziele[1]["platz"] = figurPlatz-8
                if felder[moegliche_ziele[1]["platz"]]["figure"]=="none": #es wird geprüft, ob auf dem Feld eine Figur steht
                    figurgefunden=True
                    moegliche_ziele[1]["x"]=felder[moegliche_ziele[1]["platz"]]["x"]
                    moegliche_ziele[1]["y"]=felder[moegliche_ziele[1]["platz"]]["y"]
                    punkt2.place_forget()
                    punkt3.place_forget()
                    punkt1["command"]=lambda: punktBewegtBauerSchwarz(1)#ein Punkt wird platziert
                    plazieren("ziele")
                if figurPlatz >= 49 and figurPlatz <=56: #wenn der Bauer auf der zweiten Reihe steht, wird noch ein zweiter Punkt hinzugefügt
                    moegliche_ziele[2]["platz"] = figurPlatz-16
                    if felder[moegliche_ziele[1]["platz"]]["figure"]=="none": #es wird geprüft, ob auf dem Feld eine Figur steht
                        moegliche_ziele[2]["x"]=felder[moegliche_ziele[2]["platz"]]["x"]
                        moegliche_ziele[2]["y"]=felder[moegliche_ziele[2]["platz"]]["y"]
                        punkt2["command"]=lambda: punktBewegtBauerSchwarz(2)
                        plazieren("ziele")
                figurX=felder[figurPlatz]["x"]
                figurY=felder[figurPlatz]["y"]
                for j in felder:
                    if felder[j]["y"]==figurY+47 and felder[j]["x"]==figurX-47:
                        moegliche_ziele[3]["platz"]=j
                        if felder[j]["figure"]!="none":
                            if felder[j]["figure"].farbe=="weiß":
                                figurgefunden=True
                                moegliche_ziele[3]["x"]=felder[j]["x"]
                                moegliche_ziele[3]["y"]=felder[j]["y"]
                                punkt3["command"]=lambda: punktBewegtBauerSchwarz(3)
                                plazieren("ziele")
                for k in felder:
                    if felder[k]["y"]==figurY+47 and felder[k]["x"]==figurX+47:
                        moegliche_ziele[4]["platz"]=k
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe=="weiß":
                                figurgefunden=True
                                moegliche_ziele[4]["x"]=felder[k]["x"]
                                moegliche_ziele[4]["y"]=felder[k]["y"]
                                punkt4["command"]=lambda: punktBewegtBauerSchwarz(4)
                                plazieren("ziele")
                                break
        if figurgefunden:
            print("Die Figur kann fahren")
        else:
            print("Nein")

def zuege_springer_weiß(figur_name):
    def punktBewegtSpringerWeiß(punkt_name):
        felder[figurPlatz]["figure"]="none"
        print(moegliche_ziele[punkt_name], punkt_name)
        if felder[moegliche_ziele[punkt_name]["platz"]]["figure"]!="none":
            geschlageneFiguren.append(felder[moegliche_ziele[punkt_name]["platz"]]["figure"])
        felder[moegliche_ziele[punkt_name]["platz"]]["figure"]=figur_name
        plazieren("figuren")
        setzeZieleAufNull()
        global weristdran
        weristdran="schwarz"
    global weristdran
    if weristdran=="weiß": #nur wenn weiß dran ist, passiert was
        setzeZieleAufNull()
        plazieren("ziele")
        figurgefunden=False
        figurPlatz="?"
        for i in felder: #das Dictionary mit den Feldern wird durchsucht
            if felder[i]["figure"] == figur_name: #wenn die Figur gefunden wurde
                figurPlatz=i
                print(figurPlatz)
                figurX=felder[figurPlatz]["x"]
                figurY=felder[figurPlatz]["y"]
                for j in felder:
                    if felder[j]["y"]==figurY-2*47 and felder[j]["x"]==figurX+47:
                        moegliche_ziele[1]["platz"]=j
                        if felder[j]["figure"]!="none":
                            if felder[j]["figure"].farbe=="schwarz":
                                figurgefunden=True
                                moegliche_ziele[1]["x"]=felder[j]["x"]
                                moegliche_ziele[1]["y"]=felder[j]["y"]
                                punkt1["command"]=lambda: punktBewegtSpringerWeiß(1)
                                plazieren("ziele")
                        else:
                            figurgefunden=True
                            moegliche_ziele[1]["x"]=felder[j]["x"]
                            moegliche_ziele[1]["y"]=felder[j]["y"]
                            punkt1["command"]=lambda: punktBewegtSpringerWeiß(1)
                            plazieren("ziele")
        if figurgefunden:
            print("Die Figur kann fahren")
        else:
            print("Nein")

def zuege_springer_schwarz(figur_name):
    def punktBewegtSpringerSchwarz(punkt_name):
        felder[figurPlatz]["figure"]="none"
        print(moegliche_ziele[punkt_name], punkt_name)
        if felder[moegliche_ziele[punkt_name]["platz"]]["figure"]!="none":
            geschlageneFiguren.append(felder[moegliche_ziele[punkt_name]["platz"]]["figure"])
        felder[moegliche_ziele[punkt_name]["platz"]]["figure"]=figur_name
        plazieren("figuren")
        setzeZieleAufNull()
        global weristdran
        weristdran="weiß"
    global weristdran
    if weristdran=="schwarz": #nur wenn weiß dran ist, passiert was
        setzeZieleAufNull()
        plazieren("ziele")
        figurgefunden=False
        figurPlatz="?"
        for i in felder: #das Dictionary mit den Feldern wird durchsucht
            if felder[i]["figure"] == figur_name: #wenn die Figur gefunden wurde
                figurPlatz=i
                print(figurPlatz)
                figurX=felder[figurPlatz]["x"]
                figurY=felder[figurPlatz]["y"]
                for j in felder:
                    if felder[j]["y"]==figurY+2*47 and felder[j]["x"]==figurX+47:
                        moegliche_ziele[1]["platz"]=j
                        if felder[j]["figure"]!="none":
                            if felder[j]["figure"].farbe=="weiß":
                                figurgefunden=True
                                moegliche_ziele[1]["x"]=felder[j]["x"]
                                moegliche_ziele[1]["y"]=felder[j]["y"]
                                punkt1["command"]=lambda: punktBewegtSpringerSchwarz(1)
                                plazieren("ziele")
                        else:
                            figurgefunden=True
                            moegliche_ziele[1]["x"]=felder[j]["x"]
                            moegliche_ziele[1]["y"]=felder[j]["y"]
                            punkt1["command"]=lambda: punktBewegtSpringerSchwarz(1)
                            plazieren("ziele")
        if figurgefunden:
            print("Die Figur kann fahren")
        else:
            print("Nein")

#acht Bauern weiß
bauer_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Bauer_weiß.png"))
bauer1_w = Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiß(bauer1_w))
bauer1_w.farbe="weiß"
bauer2_w = Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiß(bauer2_w))
bauer2_w.farbe="weiß"
bauer3_w = Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiß(bauer3_w))
bauer3_w.farbe="weiß"
bauer4_w = Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiß(bauer4_w))
bauer4_w.farbe="weiß"
bauer5_w = Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiß(bauer5_w))
bauer5_w.farbe="weiß"
bauer6_w = Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiß(bauer6_w))
bauer6_w.farbe="weiß"
bauer7_w = Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiß(bauer7_w))
bauer7_w.farbe="weiß"
bauer8_w = Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiß(bauer8_w))
bauer8_w.farbe="weiß"

#zwei Türme weiß
turm_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Turm_weiß.png"))
turm1_w = Schachfigur(rahmen, image=turm_w_bild)
turm1_w.farbe="weiß"
turm2_w = Schachfigur(rahmen, image=turm_w_bild)
turm2_w.farbe="weiß"

#zwei Springen weiß
springer_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Springer_weiß.png"))
springer1_w = Schachfigur(rahmen, image=springer_w_bild, command=lambda:zuege_springer_weiß(springer1_w))
springer1_w.farbe="weiß"
springer2_w = Schachfigur(rahmen, image=springer_w_bild, command=lambda:zuege_springer_weiß(springer2_w))
springer2_w.farbe="weiß"

#zwei Laeufer weiß
laeufer_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Läufer_weiß.png"))
laeufer1_w = Schachfigur(rahmen, image=laeufer_w_bild)
laeufer1_w.farbe="weiß"
laeufer2_w = Schachfigur(rahmen, image=laeufer_w_bild)
laeufer2_w.farbe="weiß"

#Koenig & Dame weiß
koenig_w_bild = ImageTk.PhotoImage(Image.open("Bilder\König_weiß.png"))
koenig_w = Schachfigur(rahmen, image=koenig_w_bild)
koenig_w.farbe="weiß"
dame_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Dame_weiß.png"))
dame_w = Schachfigur(rahmen, image=dame_w_bild)
dame_w.farbe="weiß"


#acht Bauern schwarz
bauer_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Bauer_schwarz.png"))
bauer1_s = Schachfigur(rahmen, image=bauer_s_bild, command=lambda: zuege_bauer_schwarz(bauer1_s))
bauer1_s.farbe="schwarz"
bauer2_s = Schachfigur(rahmen, image=bauer_s_bild, command=lambda: zuege_bauer_schwarz(bauer2_s))
bauer2_s.farbe="schwarz"
bauer3_s = Schachfigur(rahmen, image=bauer_s_bild, command=lambda: zuege_bauer_schwarz(bauer3_s))
bauer3_s.farbe="schwarz"
bauer4_s = Schachfigur(rahmen, image=bauer_s_bild, command=lambda: zuege_bauer_schwarz(bauer4_s))
bauer4_s.farbe="schwarz"
bauer5_s = Schachfigur(rahmen, image=bauer_s_bild, command=lambda: zuege_bauer_schwarz(bauer5_s))
bauer5_s.farbe="schwarz"
bauer6_s = Schachfigur(rahmen, image=bauer_s_bild, command=lambda: zuege_bauer_schwarz(bauer6_s))
bauer6_s.farbe="schwarz"
bauer7_s = Schachfigur(rahmen, image=bauer_s_bild, command=lambda: zuege_bauer_schwarz(bauer7_s))
bauer7_s.farbe="schwarz"
bauer8_s = Schachfigur(rahmen, image=bauer_s_bild, command=lambda: zuege_bauer_schwarz(bauer8_s))
bauer8_s.farbe="schwarz"

#zwei Türme schwarz
turm_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Turm_schwarz.png"))
turm1_s = Schachfigur(rahmen, image=turm_s_bild)
turm1_s.farbe="schwarz"
turm2_s = Schachfigur(rahmen, image=turm_s_bild)
turm2_s.farbe="schwarz"

#zwei Springen schwarz
springer_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Springer_schwarz.png"))
springer1_s = Schachfigur(rahmen, image=springer_s_bild, command=lambda:zuege_springer_schwarz(springer1_s))
springer1_s.farbe="schwarz"
springer2_s = Schachfigur(rahmen, image=springer_s_bild, command=lambda:zuege_springer_schwarz(springer2_s))
springer2_s.farbe="schwarz"

#zwei Laeufer schwarz
laeufer_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Läufer_schwarz.png"))
laeufer1_s = Schachfigur(rahmen, image=laeufer_s_bild)
laeufer1_s.farbe="schwarz"
laeufer2_s = Schachfigur(rahmen, image=laeufer_s_bild)
laeufer2_s.farbe="schwarz"

#Koenig & Dame schwarz
koenig_s_bild = ImageTk.PhotoImage(Image.open("Bilder\König_schwarz.png"))
koenig_s = Schachfigur(rahmen, image=koenig_s_bild)
koenig_s.farbe="schwarz"
dame_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Dame_schwarz.png"))
dame_s = Schachfigur(rahmen, image=dame_s_bild)
dame_s.farbe="schwarz"

gruener_punkt_bild = ImageTk.PhotoImage(Image.open("Bilder\Gruener_Punkt.png"))
punkt1=Button(rahmen, image=gruener_punkt_bild)
punkt2=Button(rahmen, image=gruener_punkt_bild)
punkt3=Button(rahmen, image=gruener_punkt_bild)
punkt4=Button(rahmen, image=gruener_punkt_bild)
punkt5=Button(rahmen, image=gruener_punkt_bild)
punkt6=Button(rahmen, image=gruener_punkt_bild)
punkt7=Button(rahmen, image=gruener_punkt_bild)
punkt8=Button(rahmen, image=gruener_punkt_bild)
punkt9=Button(rahmen, image=gruener_punkt_bild)
punkt10=Button(rahmen, image=gruener_punkt_bild)
punkt11=Button(rahmen, image=gruener_punkt_bild)
punkt12=Button(rahmen, image=gruener_punkt_bild)
punkt13=Button(rahmen, image=gruener_punkt_bild)
punkt14=Button(rahmen, image=gruener_punkt_bild)
punkt15=Button(rahmen, image=gruener_punkt_bild)
punkt16=Button(rahmen, image=gruener_punkt_bild)
punkt17=Button(rahmen, image=gruener_punkt_bild)
punkt18=Button(rahmen, image=gruener_punkt_bild)
punkt19=Button(rahmen, image=gruener_punkt_bild)
punkt20=Button(rahmen, image=gruener_punkt_bild)
punkt21=Button(rahmen, image=gruener_punkt_bild)
punkt22=Button(rahmen, image=gruener_punkt_bild)
punkt23=Button(rahmen, image=gruener_punkt_bild)
punkt24=Button(rahmen, image=gruener_punkt_bild)
punkt25=Button(rahmen, image=gruener_punkt_bild)
punkt26=Button(rahmen, image=gruener_punkt_bild)
punkt27=Button(rahmen, image=gruener_punkt_bild)

felder = {1:{"x":50, "y":379,"figure":turm1_w},2:{"x":97, "y":379,"figure":springer1_w},3:{"x":144, "y":379,"figure":laeufer1_w },4:{"x":191, "y":379,"figure":dame_w},5:{"x":238, "y":379,"figure":koenig_w},6:{"x":285, "y":379,"figure":laeufer2_w},7:{"x":332, "y":379,"figure":springer2_w},8:{"x":379, "y":379,"figure":turm2_w},9:{"x":50, "y":332,"figure":bauer1_w},10:{"x":97, "y":332,"figure":bauer2_w},11:{"x":144, "y":332,"figure":bauer3_w},12:{"x":191, "y":332,"figure":bauer4_w},13:{"x":238, "y":332,"figure":bauer5_w},14:{"x":285, "y":332,"figure":bauer6_w},15:{"x":332, "y":332,"figure":bauer7_w},16:{"x":379, "y":332,"figure":bauer8_w},17:{"x":50, "y":285,"figure":"none"},18:{"x":97, "y":285,"figure":"none"},19:{"x":144, "y":285,"figure":"none"},20:{"x":191, "y":285,"figure":"none"},21:{"x":238, "y":285,"figure":"none"},22:{"x":285, "y":285,"figure":"none"},23:{"x":332, "y":285,"figure":"none"},24:{"x":379, "y":285,"figure":"none"},25:{"x":50, "y":238,"figure":"none"},26:{"x":97, "y":238,"figure":"none"},27:{"x":144, "y":238,"figure":"none"},28:{"x":191, "y":238,"figure":"none"},29:{"x":238, "y":238,"figure":"none"},30:{"x":285, "y":238,"figure":"none"},31:{"x":332, "y":238,"figure":"none"},32:{"x":379, "y":238,"figure":"none"},33:{"x":50, "y":191,"figure":"none"},34:{"x":97, "y":191,"figure":"none"},35:{"x":144, "y":191,"figure":"none"},36:{"x":191, "y":191,"figure":"none"},37:{"x":238, "y":191,"figure":"none"},38:{"x":285, "y":191,"figure":"none"},39:{"x":332, "y":191,"figure":"none"},40:{"x":379, "y":191,"figure":"none"},41:{"x":50, "y":144,"figure":"none"},42:{"x":97, "y":144,"figure":"none"},43:{"x":144, "y":144,"figure":"none"},44:{"x":191, "y":144,"figure":"none"},45:{"x":238, "y":144,"figure":"none"},46:{"x":285, "y":144,"figure":"none"},47:{"x":332, "y":144,"figure":"none"},48:{"x":379, "y":144,"figure":"none"},49:{"x":50, "y":97,"figure":bauer1_s},50:{"x":97, "y":97,"figure":bauer2_s},51:{"x":144, "y":97,"figure":bauer3_s},52:{"x":191, "y":97,"figure":bauer4_s},53:{"x":238, "y":97,"figure":bauer5_s},54:{"x":285, "y":97,"figure":bauer6_s},55:{"x":332, "y":97,"figure":bauer7_s},56:{"x":379, "y":97,"figure":bauer8_s},57:{"x":50, "y":50,"figure":turm1_s},58:{"x":97, "y":50,"figure":springer1_s},59:{"x":144, "y":50,"figure":laeufer1_s},60:{"x":191, "y":50,"figure":dame_s},61:{"x":238, "y":50,"figure":koenig_s},62:{"x":285, "y":50,"figure":laeufer2_s},63:{"x":332, "y":50,"figure":springer2_s},64:{"x":379, "y":50,"figure":turm2_s}}
ziele = [punkt1, punkt2, punkt3, punkt4, punkt5, punkt6, punkt7, punkt8, punkt9, punkt10, punkt11, punkt12, punkt13, punkt14, punkt15, punkt16, punkt17, punkt18, punkt19, punkt20, punkt21, punkt22, punkt23, punkt24, punkt25, punkt26, punkt27]
geschlageneFiguren=[]


def plazieren(x):
    if x == "figuren":
        for i in geschlageneFiguren:
            i.place_forget()
        for i in felder:
            if felder[i]["figure"]!="none":
                felder[i]["figure"].place(x=felder[i]["x"], y=felder[i]["y"])
    elif x == "ziele":
        for i in moegliche_ziele:
            if moegliche_ziele[i]["x"]!="none":
                ziele[i-1].place(x=moegliche_ziele[i]["x"], y=moegliche_ziele[i]["y"])

plazieren("figuren")

fenster.mainloop()