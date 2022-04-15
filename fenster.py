from tkinter import *
from PIL import ImageTk, Image
fenster = Tk()
fenster.title("Schach Projekt")
rahmen=Frame(fenster, relief="ridge", borderwidth=5)
rahmen.pack()
schachbrett_bild = ImageTk.PhotoImage(Image.open("Bilder\Schachbrett.png"))
schachbrett = Label(rahmen, image=schachbrett_bild)
schachbrett.pack(expand=True, padx=30, pady=30)

felder = {1:{"x":50, "y":379,"figure":"turm1_w"},2:{"x":97, "y":379,"figure":"springer1_w"},3:{"x":144, "y":379,"figure":"laeufer1_w"},4:{"x":191, "y":379,"figure":"dame_w"},5:{"x":238, "y":379,"figure":"koenig_w"},6:{"x":285, "y":379,"figure":"laeufer2_w"},7:{"x":332, "y":379,"figure":"springer2_w"},8:{"x":379, "y":379,"figure":"turm2_w"},9:{"x":50, "y":332,"figure":"bauer1_w"},10:{"x":97, "y":332,"figure":"bauer2_w"},11:{"x":144, "y":332,"figure":"bauer3_w"},12:{"x":191, "y":332,"figure":"bauer4_w"},13:{"x":238, "y":332,"figure":"bauer5_w"},14:{"x":285, "y":332,"figure":"bauer6_w"},15:{"x":332, "y":332,"figure":"bauer7_w"},16:{"x":379, "y":332,"figure":"bauer8_w"},17:{"x":50, "y":285,"figure":"none"},18:{"x":97, "y":285,"figure":"none"},19:{"x":144, "y":285,"figure":"none"},20:{"x":191, "y":285,"figure":"none"},21:{"x":238, "y":285,"figure":"none"},22:{"x":285, "y":285,"figure":"none"},23:{"x":332, "y":285,"figure":"none"},24:{"x":379, "y":285,"figure":"none"},25:{"x":50, "y":238,"figure":"none"},26:{"x":97, "y":238,"figure":"none"},27:{"x":144, "y":238,"figure":"none"},28:{"x":191, "y":238,"figure":"none"},29:{"x":238, "y":238,"figure":"none"},30:{"x":285, "y":238,"figure":"none"},31:{"x":332, "y":238,"figure":"none"},32:{"x":379, "y":238,"figure":"none"},33:{"x":50, "y":191,"figure":"none"},34:{"x":97, "y":191,"figure":"none"},35:{"x":144, "y":191,"figure":"none"},36:{"x":191, "y":191,"figure":"none"},37:{"x":238, "y":191,"figure":"none"},38:{"x":285, "y":191,"figure":"none"},39:{"x":332, "y":191,"figure":"none"},40:{"x":379, "y":191,"figure":"none"},41:{"x":50, "y":144,"figure":"none"},42:{"x":97, "y":144,"figure":"none"},43:{"x":144, "y":144,"figure":"none"},44:{"x":191, "y":144,"figure":"none"},45:{"x":238, "y":144,"figure":"none"},46:{"x":285, "y":144,"figure":"none"},47:{"x":332, "y":144,"figure":"none"},48:{"x":379, "y":144,"figure":"none"},49:{"x":50, "y":97,"figure":"bauer1_s"},50:{"x":97, "y":97,"figure":"bauer2_s"},51:{"x":144, "y":97,"figure":"bauer3_s"},52:{"x":191, "y":97,"figure":"bauer4_s"},53:{"x":238, "y":97,"figure":"bauer5_s"},54:{"x":285, "y":97,"figure":"bauer6_s"},55:{"x":332, "y":97,"figure":"bauer7_s"},56:{"x":379, "y":97,"figure":"bauer8_s"},57:{"x":50, "y":50,"figure":"turm1_s"},58:{"x":97, "y":50,"figure":"springer1_s"},59:{"x":144, "y":50,"figure":"laeufer1_s"},60:{"x":191, "y":50,"figure":"dame_s"},61:{"x":238, "y":50,"figure":"koenig_s"},62:{"x":285, "y":50,"figure":"laeufer2_s"},63:{"x":332, "y":50,"figure":"springer2_s"},64:{"x":379, "y":50,"figure":"turm2_s"}}

gruener_punkt_bild = ImageTk.PhotoImage(Image.open("Bilder\Gruener_Punkt.png"))
punkt=Button(rahmen, image=gruener_punkt_bild)
punkt2=Button(rahmen, image=gruener_punkt_bild)
weristdran="weiß"

#Klasse der weißen Bauern wird erstellt
class Bauer_weiß(Button):
    def zeige_bauer_weiß (self, figur): #das passiert, wenn der Bauer gedrückt wird
        def punktBewegtBauerWeiß():
            #das passiert wenn auf den ersten Knopf gedrückt wird
            global weristdran
            felder[figurPlatz]["figure"]="none"
            felder[moeglichesZiel[0]]["figure"]=figur
            self.place(x=xKoordinate[0], y=yKoordinate[0])
            punkt.place_forget()
            punkt2.place_forget()
            weristdran="schwarz"
        def punkt2BewegtBauerWeiß():
            #das passiert, wenn auf den zweiten Knopf gedrückt wird
            global weristdran
            felder[figurPlatz]["figure"]="none"
            felder[moeglichesZiel[1]]["figure"]=figur
            self.place(x=xKoordinate[1], y=yKoordinate[1])
            punkt.place_forget()
            punkt2.place_forget()
            weristdran="schwarz"
        global weristdran
        if weristdran=="weiß": #nur wenn weiß dran ist, passiert was
            figurgefunden=False
            figurPlatz="?"
            for i in felder: #das Dictionary mit den Feldern wird durchsucht
                if felder[i]["figure"] == figur: #wenn die Figur gefunden wurde
                    figurPlatz=i
                    moeglichesZiel=[0,0]
                    xKoordinate=[0,0]
                    yKoordinate=[0,0]
                    moeglichesZiel[0] = figurPlatz+8
                    xKoordinate[0]=felder[moeglichesZiel[0]]["x"]
                    yKoordinate[0]=felder[moeglichesZiel[0]]["y"]
                    if felder[moeglichesZiel[0]]["figure"]=="none": #es wird geprüft, ob auf dem Feld eine Figur steht
                        figurgefunden=True
                        punkt2.place_forget()
                        punkt["command"]=punktBewegtBauerWeiß #ein Punkt wird platziert
                        punkt.place(x=xKoordinate[0], y=yKoordinate[0])
                    else:
                        figurgefunden=False
                        print(moeglichesZiel)
                        break
                    if figurPlatz >= 9 and figurPlatz <=16: #wenn der Bauer auf der zweiten Reihe steht, wird noch ein zweiter Punkt hinzugefügt
                        moeglichesZiel[1] = figurPlatz+16
                        xKoordinate[1]=felder[moeglichesZiel[1]]["x"]
                        yKoordinate[1]=felder[moeglichesZiel[1]]["y"]
                        if felder[moeglichesZiel[1]]["figure"]=="none": #es wird geprüft, ob auf dem Feld eine Figur steht
                            figurgefunden=True
                            punkt2["command"]=punkt2BewegtBauerWeiß
                            punkt2.place(x=xKoordinate[1], y=yKoordinate[1])
                            break
                    else:
                        break
            if figurgefunden:
                print("Die Figur kann nach ",moeglichesZiel,"fahren")
            else:
                print("Nein")

class Bauer_schwarz(Button):
    def zeige_bauer_schwarz (self, figur): #das passiert, wenn der Bauer gedrückt wird
        def punktBewegtBauerSchwarz():
            #das passiert wenn auf den ersten Knopf gedrückt wird
            global weristdran
            felder[figurPlatz]["figure"]="none"
            felder[moeglichesZiel[0]]["figure"]=figur
            self.place(x=xKoordinate[0], y=yKoordinate[0])
            punkt.place_forget()
            punkt2.place_forget()
            weristdran="weiß"
        def punkt2BewegtBauerSchwarz():
            #das passiert, wenn auf den zweiten Knopf gedrückt wird
            global weristdran
            felder[figurPlatz]["figure"]="none"
            felder[moeglichesZiel[1]]["figure"]=figur
            self.place(x=xKoordinate[1], y=yKoordinate[1])
            punkt.place_forget()
            punkt2.place_forget()
            weristdran="weiß"
        global weristdran
        if weristdran=="schwarz": #nur wenn schwarz dran ist, passiert was
            figurgefunden=False
            figurPlatz="?"
            for i in felder: #das Dictionary mit den Feldern wird durchsucht
                if felder[i]["figure"] == figur: #wenn die Figur gefunden wurde
                    figurPlatz=i
                    moeglichesZiel=[0,0]
                    xKoordinate=[0,0]
                    yKoordinate=[0,0]
                    moeglichesZiel[0] = figurPlatz-8
                    xKoordinate[0]=felder[moeglichesZiel[0]]["x"]
                    yKoordinate[0]=felder[moeglichesZiel[0]]["y"]
                    if felder[moeglichesZiel[0]]["figure"]=="none": #es wird geprüft, ob auf dem Feld eine Figur steht
                        figurgefunden=True
                        punkt2.place_forget()
                        punkt["command"]=punktBewegtBauerSchwarz #ein Punkt wird platziert
                        punkt.place(x=xKoordinate[0], y=yKoordinate[0])
                    else:
                        figurgefunden=False
                        print(moeglichesZiel)
                        break
                    if figurPlatz >= 49 and figurPlatz <=56: #wenn der Bauer auf der zweiten Reihe steht, wird noch ein zweiter Punkt hinzugefügt
                        moeglichesZiel[1] = figurPlatz-16
                        xKoordinate[1]=felder[moeglichesZiel[1]]["x"]
                        yKoordinate[1]=felder[moeglichesZiel[1]]["y"]
                        if felder[moeglichesZiel[1]]["figure"]=="none": #es wird geprüft, ob auf dem Feld eine Figur steht
                            figurgefunden=True
                            punkt2["command"]=punkt2BewegtBauerSchwarz
                            punkt2.place(x=xKoordinate[1], y=yKoordinate[1])
                            break
                    else:
                        break
            if figurgefunden:
                print("Die Figur kann nach ",moeglichesZiel,"fahren")
            else:
                print("Nein")

#acht Bauern weiß
bauer_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Bauer_weiß.png"))
bauer1_w = Bauer_weiß(rahmen, image=bauer_w_bild, command=lambda:bauer1_w.zeige_bauer_weiß("bauer1_w"))
bauer1_w.place(y=332, x=50)
bauer2_w = Bauer_weiß(rahmen, image=bauer_w_bild, command=lambda:bauer2_w.zeige_bauer_weiß("bauer2_w"))
bauer2_w.place(y=332, x=97)
bauer3_w = Bauer_weiß(rahmen, image=bauer_w_bild, command=lambda:bauer3_w.zeige_bauer_weiß("bauer3_w"))
bauer3_w.place(y=332, x=144)
bauer4_w = Bauer_weiß(rahmen, image=bauer_w_bild, command=lambda:bauer4_w.zeige_bauer_weiß("bauer4_w"))
bauer4_w.place(y=332, x=191)
bauer5_w = Bauer_weiß(rahmen, image=bauer_w_bild, command=lambda:bauer5_w.zeige_bauer_weiß("bauer5_w"))
bauer5_w.place(y=332, x=238)
bauer6_w = Bauer_weiß(rahmen, image=bauer_w_bild, command=lambda:bauer6_w.zeige_bauer_weiß("bauer6_w"))
bauer6_w.place(y=332, x=285)
bauer7_w = Bauer_weiß(rahmen, image=bauer_w_bild, command=lambda:bauer7_w.zeige_bauer_weiß("bauer7_w"))
bauer7_w.place(y=332, x=332)
bauer8_w = Bauer_weiß(rahmen, image=bauer_w_bild, command=lambda:bauer8_w.zeige_bauer_weiß("bauer8_w"))
bauer8_w.place(y=332, x=379)

#zwei Türme weiß
turm_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Turm_weiß.png"))
turm1_w = Button(rahmen, image=turm_w_bild)
turm1_w.place(y=379, x=50)
turm2_w = Button(rahmen, image=turm_w_bild)
turm2_w.place(y=379, x=379)

#zwei Springen weiß
springer_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Springer_weiß.png"))
springer1_w = Button(rahmen, image=springer_w_bild)
springer1_w.place(y=379, x=97)
springer2_w = Button(rahmen, image=springer_w_bild)
springer2_w.place(y=379, x=332)

#zwei Laeufer weiß
laeufer_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Läufer_weiß.png"))
laeufer1_w = Button(rahmen, image=laeufer_w_bild)
laeufer1_w.place(y=379, x=144)
laeufer2_w = Button(rahmen, image=laeufer_w_bild)
laeufer2_w.place(y=379, x=285)

#Koenig & Dame weiß
koenig_w_bild = ImageTk.PhotoImage(Image.open("Bilder\König_weiß.png"))
koenig_w = Button(rahmen, image=koenig_w_bild)
koenig_w.place(y=379, x=238)
dame_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Dame_weiß.png"))
dame_w = Button(rahmen, image=dame_w_bild)
dame_w.place(y=379, x=191)


#acht Bauern schwarz
bauer_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Bauer_schwarz.png"))
bauer1_s = Bauer_schwarz(rahmen, image=bauer_s_bild, command=lambda: bauer1_s.zeige_bauer_schwarz("bauer1_s"))
bauer1_s.place(y=97, x=50)
bauer2_s = Bauer_schwarz(rahmen, image=bauer_s_bild, command=lambda: bauer2_s.zeige_bauer_schwarz("bauer2_s"))
bauer2_s.place(y=97, x=97)
bauer3_s = Bauer_schwarz(rahmen, image=bauer_s_bild, command=lambda: bauer3_s.zeige_bauer_schwarz("bauer3_s"))
bauer3_s.place(y=97, x=144)
bauer4_s = Bauer_schwarz(rahmen, image=bauer_s_bild, command=lambda: bauer4_s.zeige_bauer_schwarz("bauer4_s"))
bauer4_s.place(y=97, x=191)
bauer5_s = Bauer_schwarz(rahmen, image=bauer_s_bild, command=lambda: bauer5_s.zeige_bauer_schwarz("bauer5_s"))
bauer5_s.place(y=97, x=238)
bauer6_s = Bauer_schwarz(rahmen, image=bauer_s_bild, command=lambda: bauer6_s.zeige_bauer_schwarz("bauer6_s"))
bauer6_s.place(y=97, x=285)
bauer7_s = Bauer_schwarz(rahmen, image=bauer_s_bild, command=lambda: bauer7_s.zeige_bauer_schwarz("bauer7_s"))
bauer7_s.place(y=97, x=332)
bauer8_s = Bauer_schwarz(rahmen, image=bauer_s_bild, command=lambda: bauer8_s.zeige_bauer_schwarz("bauer8_s"))
bauer8_s.place(y=97, x=379)

#zwei Türme schwarz
turm_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Turm_schwarz.png"))
turm1_s = Button(rahmen, image=turm_s_bild)
turm1_s.place(y=50, x=50)
turm2_s = Button(rahmen, image=turm_s_bild)
turm2_s.place(y=50, x=379)

#zwei Springen schwarz
springer_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Springer_schwarz.png"))
springer1_s = Button(rahmen, image=springer_s_bild)
springer1_s.place(y=50, x=97)
springer2_s = Button(rahmen, image=springer_s_bild)
springer2_s.place(y=50, x=332)

#zwei Laeufer schwarz
laeufer_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Läufer_schwarz.png"))
laeufer1_s = Button(rahmen, image=laeufer_s_bild)
laeufer1_s.place(y=50, x=144)
laeufer2_s = Button(rahmen, image=laeufer_s_bild)
laeufer2_s.place(y=50, x=285)

#Koenig & Dame schwarz
koenig_s_bild = ImageTk.PhotoImage(Image.open("Bilder\König_schwarz.png"))
koenig_s = Button(rahmen, image=koenig_s_bild)
koenig_s.place(y=50, x=238)
dame_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Dame_schwarz.png"))
dame_s = Button(rahmen, image=dame_s_bild)
dame_s.place(y=50, x=191)

fenster.mainloop()