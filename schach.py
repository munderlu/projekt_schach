from tkinter import *
from PIL import ImageTk, Image
fenster = Tk()
fenster.title("Schach Projekt")
rahmen=Frame(fenster, relief="ridge", borderwidth=5)
rahmen.pack()
schachbrett_bild = ImageTk.PhotoImage(Image.open("Bilder\Schachbrett.png"))
schachbrett = Label(rahmen, image=schachbrett_bild)
schachbrett.pack(expand=True, padx=30, pady=30)
weristdran="weiß"
aktuelle_figur="none"

class Schachfigur(Button):
    farbe="?"

moegliche_ziele={1:{"button_Nr": "none", "x":"none", "y":"none"}, 2:{"button_Nr": "none", "x":"none", "y":"none"}, 3:{"button_Nr": "none", "x":"none", "y":"none"}, 4:{"button_Nr": "none", "x":"none", "y":"none"}, 5:{"button_Nr": "none", "x":"none", "y":"none"}, 6:{"button_Nr": "none", "x":"none", "y":"none"}, 7:{"button_Nr": "none", "x":"none", "y":"none"}, 8:{"button_Nr": "none", "x":"none", "y":"none"}, 9:{"button_Nr": "none", "x":"none", "y":"none"}, 10:{"button_Nr": "none", "x":"none", "y":"none"}, 11:{"button_Nr": "none", "x":"none", "y":"none"}, 12:{"button_Nr": "none", "x":"none", "y":"none"}, 13:{"button_Nr": "none", "x":"none", "y":"none"}, 14:{"button_Nr": "none", "x":"none", "y":"none"}, 15:{"button_Nr": "none", "x":"none", "y":"none"}, 16:{"button_Nr": "none", "x":"none", "y":"none"}, 17:{"button_Nr": "none", "x":"none", "y":"none"}, 18:{"button_Nr": "none", "x":"none", "y":"none"}, 19:{"button_Nr": "none", "x":"none", "y":"none"}, 20:{"button_Nr": "none", "x":"none", "y":"none"}, 21:{"button_Nr": "none", "x":"none", "y":"none"}, 22:{"button_Nr": "none", "x":"none", "y":"none"}, 23:{"button_Nr": "none", "x":"none", "y":"none"}, 24:{"button_Nr": "none", "x":"none", "y":"none"}, 25:{"button_Nr": "none", "x":"none", "y":"none"}, 26:{"button_Nr": "none", "x":"none", "y":"none"}, 27:{"button_Nr": "none", "x":"none", "y":"none"}}
def setzeZieleAufNull():
    global moegliche_ziele
    moegliche_ziele={1:{"button_Nr": "none", "x":"none", "y":"none"}, 2:{"button_Nr": "none", "x":"none", "y":"none"}, 3:{"button_Nr": "none", "x":"none", "y":"none"}, 4:{"button_Nr": "none", "x":"none", "y":"none"}, 5:{"button_Nr": "none", "x":"none", "y":"none"}, 6:{"button_Nr": "none", "x":"none", "y":"none"}, 7:{"button_Nr": "none", "x":"none", "y":"none"}, 8:{"button_Nr": "none", "x":"none", "y":"none"}, 9:{"button_Nr": "none", "x":"none", "y":"none"}, 10:{"button_Nr": "none", "x":"none", "y":"none"}, 11:{"button_Nr": "none", "x":"none", "y":"none"}, 12:{"button_Nr": "none", "x":"none", "y":"none"}, 13:{"button_Nr": "none", "x":"none", "y":"none"}, 14:{"button_Nr": "none", "x":"none", "y":"none"}, 15:{"button_Nr": "none", "x":"none", "y":"none"}, 16:{"button_Nr": "none", "x":"none", "y":"none"}, 17:{"button_Nr": "none", "x":"none", "y":"none"}, 18:{"button_Nr": "none", "x":"none", "y":"none"}, 19:{"button_Nr": "none", "x":"none", "y":"none"}, 20:{"button_Nr": "none", "x":"none", "y":"none"}, 21:{"button_Nr": "none", "x":"none", "y":"none"}, 22:{"button_Nr": "none", "x":"none", "y":"none"}, 23:{"button_Nr": "none", "x":"none", "y":"none"}, 24:{"button_Nr": "none", "x":"none", "y":"none"}, 25:{"button_Nr": "none", "x":"none", "y":"none"}, 26:{"button_Nr": "none", "x":"none", "y":"none"}, 27:{"button_Nr": "none", "x":"none", "y":"none"}}
    for i in punkte:
        i.place_forget

def punkte_auswählen():
    for i in moegliche_ziele:
        if moegliche_ziele[i]["x"]!="none":
            rechenvariable1=moegliche_ziele[i]["x"]
            rechenvariable2=moegliche_ziele[i]["y"]
            rechenvariable3=(rechenvariable1-3)/47
            rechenvariable4=(rechenvariable2-3)/47       
            ergebniss=(rechenvariable3+((rechenvariable4-1)*8)-1)
            moegliche_ziele[i]["button_Nr"]=int(ergebniss)

def punkte_plazieren():
    for i in moegliche_ziele:
        if moegliche_ziele[i]["button_Nr"]!="none":
            punkte[int(moegliche_ziele[i]["button_Nr"])].place(x=moegliche_ziele[i]["x"], y=moegliche_ziele[i]["y"])

def zuege_bauer_weiß(figur):
    setzeZieleAufNull()
    global weristdran
    if weristdran=="weiß":
        for i in felder:
            if felder[i]["figure"]==figur:
                global aktuelle_figur
                aktuelle_figur=figur
                if felder[i+8]["figure"]=="none":
                    moegliche_ziele[1]["x"]=felder[i]["x"]
                    moegliche_ziele[1]["y"]=felder[i]["y"]-47
                if felder[i]["y"]==332 and felder[i+8]["figure"]=="none" and felder[i+16]["figure"]=="none":
                    moegliche_ziele[2]["x"]=felder[i]["x"]
                    moegliche_ziele[2]["y"]=238
                if felder[i]["x"]!=379:
                    if felder[i+9]["figure"]!="none"and felder[i+9]["figure"].farbe=="schwarz":
                        moegliche_ziele[3]["x"]=felder[i]["x"]+47
                        moegliche_ziele[3]["y"]=felder[i]["y"]-47
                if felder[i]["x"]!=50:
                    if felder[i+7]["figure"]!="none"and felder[i+7]["figure"].farbe=="schwarz":
                        moegliche_ziele[4]["x"]=felder[i]["x"]-47
                        moegliche_ziele[4]["y"]=felder[i]["y"]-47
        punkte_auswählen()             
        punkte_plazieren() 
        print(moegliche_ziele)
        
def zuege_bauer_schwarz(figur):
    setzeZieleAufNull()
    global weristdran
    if weristdran=="schwarz":
        for i in felder:
            if felder[i]["figure"]==figur:
                global aktuelle_figur
                aktuelle_figur=figur
                if felder[i-8]["figure"]=="none":
                    moegliche_ziele[1]["x"]=felder[i]["x"]
                    moegliche_ziele[1]["y"]=felder[i]["y"]+47
                if felder[i]["y"]==97 and felder[i-8]["figure"]=="none" and felder[i-16]["figure"]=="none":
                    moegliche_ziele[2]["x"]=felder[i]["x"]
                    moegliche_ziele[2]["y"]=191
                if felder[i]["x"]!=50:
                    if felder[i-9]["figure"]!="none"and felder[i-9]["figure"].farbe=="weiß":
                        moegliche_ziele[3]["x"]=felder[i]["x"]-47
                        moegliche_ziele[3]["y"]=felder[i]["y"]+47
                if felder[i]["x"]!=379:
                    if felder[i-7]["figure"]!="none"and felder[i-7]["figure"].farbe=="weiß":
                        moegliche_ziele[4]["x"]=felder[i]["x"]+47
                        moegliche_ziele[4]["y"]=felder[i]["y"]+47
        punkte_auswählen()             
        punkte_plazieren() 
        
def zuege_turm_weiß(aktuelle_figur):
    print("coming soon")
def zuege_turm_schwarz(aktuelle_figur):
    print("coming soon")
def zuege_springer_weiß(figur):
    setzeZieleAufNull()
    global weristdran
    if weristdran=="weiß":
        for i in felder:
            if felder[i]["figure"]==figur:
                global aktuelle_figur
                aktuelle_figur=figur
                figurX=felder[i]["x"]
                figurY=felder[i]["y"]
                for j in felder:
                    if felder[j]["y"]==figurY-2*47 and felder[j]["x"]==figurX+47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            moegliche_ziele[1]["x"]=felder[j]["x"]
                            moegliche_ziele[1]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY-2*47 and felder[j]["x"]==figurX-47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            moegliche_ziele[2]["x"]=felder[j]["x"]
                            moegliche_ziele[2]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY-47 and felder[j]["x"]==figurX+2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            moegliche_ziele[3]["x"]=felder[j]["x"]
                            moegliche_ziele[3]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+47 and felder[j]["x"]==figurX+2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            moegliche_ziele[4]["x"]=felder[j]["x"]
                            moegliche_ziele[4]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+2*47 and felder[j]["x"]==figurX+47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            moegliche_ziele[5]["x"]=felder[j]["x"]
                            moegliche_ziele[5]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+2*47 and felder[j]["x"]==figurX-47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            moegliche_ziele[6]["x"]=felder[j]["x"]
                            moegliche_ziele[6]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+47 and felder[j]["x"]==figurX-2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            moegliche_ziele[7]["x"]=felder[j]["x"]
                            moegliche_ziele[7]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY-47 and felder[j]["x"]==figurX-2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            moegliche_ziele[8]["x"]=felder[j]["x"]
                            moegliche_ziele[8]["y"]=felder[j]["y"]
            print(moegliche_ziele)
            punkte_auswählen()
            punkte_plazieren()
            
def zuege_springer_schwarz(figur):
    setzeZieleAufNull()
    global weristdran
    if weristdran=="schwarz":
        for i in felder:
            if felder[i]["figure"]==figur:
                global aktuelle_figur
                aktuelle_figur=figur
                figurX=felder[i]["x"]
                figurY=felder[i]["y"]
                for j in felder:
                    if felder[j]["y"]==figurY-2*47 and felder[j]["x"]==figurX+47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiß":
                            moegliche_ziele[1]["x"]=felder[j]["x"]
                            moegliche_ziele[1]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY-2*47 and felder[j]["x"]==figurX-47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiß":
                            moegliche_ziele[2]["x"]=felder[j]["x"]
                            moegliche_ziele[2]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY-47 and felder[j]["x"]==figurX+2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiß":
                            moegliche_ziele[3]["x"]=felder[j]["x"]
                            moegliche_ziele[3]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+47 and felder[j]["x"]==figurX+2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiß":
                            moegliche_ziele[4]["x"]=felder[j]["x"]
                            moegliche_ziele[4]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+2*47 and felder[j]["x"]==figurX+47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiß":
                            moegliche_ziele[5]["x"]=felder[j]["x"]
                            moegliche_ziele[5]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+2*47 and felder[j]["x"]==figurX-47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiß":
                            moegliche_ziele[6]["x"]=felder[j]["x"]
                            moegliche_ziele[6]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+47 and felder[j]["x"]==figurX-2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiß":
                            moegliche_ziele[7]["x"]=felder[j]["x"]
                            moegliche_ziele[7]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY-47 and felder[j]["x"]==figurX-2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiß":
                            moegliche_ziele[8]["x"]=felder[j]["x"]
                            moegliche_ziele[8]["y"]=felder[j]["y"]
            print(moegliche_ziele)
            punkte_auswählen()
            punkte_plazieren()
def zuege_laeufer_weiß(aktuelle_figur):
    print("coming soon")
def zuege_laeufer_schwarz(aktuelle_figur):
    print("coming soon")
def zuege_koenig_weiß(aktuelle_figur):
    print("coming soon")
def zuege_koenig_schwarz(aktuelle_figur):
    print("coming soon")
def zuege_dame_weiß(aktuelle_figur):
    print("coming soon")
def zuege_dame_schwarz(aktuelle_figur):
    print("coming soon")

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
turm1_w = Schachfigur(rahmen, image=turm_w_bild, command=lambda:zuege_turm_weiß(turm1_w))
turm1_w.farbe="weiß"
turm2_w = Schachfigur(rahmen, image=turm_w_bild, command=lambda:zuege_turm_weiß(turm2_w))
turm2_w.farbe="weiß"

#zwei Springen weiß
springer_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Springer_weiß.png"))
springer1_w = Schachfigur(rahmen, image=springer_w_bild, command=lambda:zuege_springer_weiß(springer1_w))
springer1_w.farbe="weiß"
springer2_w = Schachfigur(rahmen, image=springer_w_bild, command=lambda:zuege_springer_weiß(springer2_w))
springer2_w.farbe="weiß"

#zwei Laeufer weiß
laeufer_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Läufer_weiß.png"))
laeufer1_w = Schachfigur(rahmen, image=laeufer_w_bild, command=lambda:zuege_laeufer_weiß(laeufer1_w))
laeufer1_w.farbe="weiß"
laeufer2_w = Schachfigur(rahmen, image=laeufer_w_bild, command=lambda:zuege_laeufer_weiß(laeufer2_w))
laeufer2_w.farbe="weiß"

#Koenig & Dame weiß
koenig_w_bild = ImageTk.PhotoImage(Image.open("Bilder\König_weiß.png"))
koenig_w = Schachfigur(rahmen, image=koenig_w_bild, command=lambda:zuege_koenig_weiß(koenig_w))
koenig_w.farbe="weiß"
dame_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Dame_weiß.png"))
dame_w = Schachfigur(rahmen, image=dame_w_bild, command=lambda:zuege_dame_weiß(dame_w))
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
turm1_s = Schachfigur(rahmen, image=turm_s_bild, command=lambda:zuege_turm_schwarz(turm1_s))
turm1_s.farbe="schwarz"
turm2_s = Schachfigur(rahmen, image=turm_s_bild, command=lambda:zuege_turm_schwarz(turm2_s))
turm2_s.farbe="schwarz"

#zwei Springer schwarz
springer_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Springer_schwarz.png"))
springer1_s = Schachfigur(rahmen, image=springer_s_bild, command=lambda:zuege_springer_schwarz(springer1_s))
springer1_s.farbe="schwarz"
springer2_s = Schachfigur(rahmen, image=springer_s_bild, command=lambda:zuege_springer_schwarz(springer2_s))
springer2_s.farbe="schwarz"

#zwei Laeufer schwarz
laeufer_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Läufer_schwarz.png"))
laeufer1_s = Schachfigur(rahmen, image=laeufer_s_bild, command=lambda:zuege_laeufer_schwarz(laeufer1_s))
laeufer1_s.farbe="schwarz"
laeufer2_s = Schachfigur(rahmen, image=laeufer_s_bild, command=lambda:zuege_laeufer_schwarz(laeufer2_s))
laeufer2_s.farbe="schwarz"

#Koenig & Dame schwarz
koenig_s_bild = ImageTk.PhotoImage(Image.open("Bilder\König_schwarz.png"))
koenig_s = Schachfigur(rahmen, image=koenig_s_bild, command=lambda:zuege_koenig_schwarz(koenig_s))
koenig_s.farbe="schwarz"
dame_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Dame_schwarz.png"))
dame_s = Schachfigur(rahmen, image=dame_s_bild, command=lambda:zuege_dame_schwarz(dame_s))
dame_s.farbe="schwarz"

def figur_ziehen(xpos, ypos):
    for i in range(0, 64, 1):
        punkte[i].place_forget()
    global felder
    global weristdran
    for i in felder:
        if felder[i]["figure"]==aktuelle_figur:
            felder[i]["figure"]="none"
    for i in felder:
        if felder[i]["x"]==xpos and felder[i]["y"]==ypos:
            if felder[i]["figure"]!="none":
                felder[i]["figure"].place_forget()
            felder[i]["figure"]=aktuelle_figur
            felder[i]["figure"].place(x=felder[i]["x"], y=felder[i]["y"])
    if weristdran=="schwarz":
        weristdran="weiß"
    else:
        weristdran="schwarz"
       
gruener_punkt_bild = ImageTk.PhotoImage(Image.open("Bilder\Gruener_Punkt.png"))
punkt1= Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(50, 50))
punkt2= Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(97, 50))
punkt3= Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(144, 50))
punkt4= Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(191, 50))
punkt5= Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(238, 50))
punkt6= Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(285, 50))
punkt7= Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(332, 50))
punkt8= Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(379, 50))
punkt9= Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(50, 97))
punkt10=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(97, 97))
punkt11=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(144, 97))
punkt12=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(191, 97))
punkt13=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(238, 97))
punkt14=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(285, 97))
punkt15=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(332, 97))
punkt16=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(379, 97))
punkt17=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(50, 144))
punkt18=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(97, 144))
punkt19=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(144, 144))
punkt20=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(191, 144))
punkt21=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(238, 144))
punkt22=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(285, 144))
punkt23=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(332, 144))
punkt24=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(379, 144))
punkt25=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(50, 191))
punkt26=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(97, 191))
punkt27=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(144, 191))
punkt28=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(191, 191))
punkt29=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(238, 191))
punkt30=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(285, 191))
punkt31=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(332, 191))
punkt32=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(379, 191))
punkt33=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(50, 238))
punkt34=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(97, 238))
punkt35=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(144, 238))
punkt36=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(191, 238))
punkt37=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(238, 238))
punkt38=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(285, 238))
punkt39=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(332, 238))
punkt40=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(379, 238))
punkt41=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(50, 285))
punkt42=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(97, 285))
punkt43=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(144, 285))
punkt44=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(191, 285))
punkt45=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(238, 285))
punkt46=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(285, 285))
punkt47=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(332, 285))
punkt48=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(379, 285))
punkt49=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(50, 332))
punkt50=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(97, 332))
punkt51=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(144, 332))
punkt52=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(191, 332))
punkt53=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(238, 332))
punkt54=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(285, 332))
punkt55=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(332, 332))
punkt56=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(379, 332))
punkt57=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(50, 379))
punkt58=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(97, 379))
punkt59=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(144, 379))
punkt60=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(191, 379))
punkt61=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(238, 379))
punkt62=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(285, 379))
punkt63=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(332, 379))
punkt64=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(379, 379))

felder = {1:{"x":50, "y":379,"figure":turm1_w},2:{"x":97, "y":379,"figure":springer1_w},3:{"x":144, "y":379,"figure":laeufer1_w },4:{"x":191, "y":379,"figure":dame_w},5:{"x":238, "y":379,"figure":koenig_w},6:{"x":285, "y":379,"figure":laeufer2_w},7:{"x":332, "y":379,"figure":springer2_w},8:{"x":379, "y":379,"figure":turm2_w},9:{"x":50, "y":332,"figure":bauer1_w},10:{"x":97, "y":332,"figure":bauer2_w},11:{"x":144, "y":332,"figure":bauer3_w},12:{"x":191, "y":332,"figure":bauer4_w},13:{"x":238, "y":332,"figure":bauer5_w},14:{"x":285, "y":332,"figure":bauer6_w},15:{"x":332, "y":332,"figure":bauer7_w},16:{"x":379, "y":332,"figure":bauer8_w},17:{"x":50, "y":285,"figure":"none"},18:{"x":97, "y":285,"figure":"none"},19:{"x":144, "y":285,"figure":"none"},20:{"x":191, "y":285,"figure":"none"},21:{"x":238, "y":285,"figure":"none"},22:{"x":285, "y":285,"figure":"none"},23:{"x":332, "y":285,"figure":"none"},24:{"x":379, "y":285,"figure":"none"},25:{"x":50, "y":238,"figure":"none"},26:{"x":97, "y":238,"figure":"none"},27:{"x":144, "y":238,"figure":"none"},28:{"x":191, "y":238,"figure":"none"},29:{"x":238, "y":238,"figure":"none"},30:{"x":285, "y":238,"figure":"none"},31:{"x":332, "y":238,"figure":"none"},32:{"x":379, "y":238,"figure":"none"},33:{"x":50, "y":191,"figure":"none"},34:{"x":97, "y":191,"figure":"none"},35:{"x":144, "y":191,"figure":"none"},36:{"x":191, "y":191,"figure":"none"},37:{"x":238, "y":191,"figure":"none"},38:{"x":285, "y":191,"figure":"none"},39:{"x":332, "y":191,"figure":"none"},40:{"x":379, "y":191,"figure":"none"},41:{"x":50, "y":144,"figure":"none"},42:{"x":97, "y":144,"figure":"none"},43:{"x":144, "y":144,"figure":"none"},44:{"x":191, "y":144,"figure":"none"},45:{"x":238, "y":144,"figure":"none"},46:{"x":285, "y":144,"figure":"none"},47:{"x":332, "y":144,"figure":"none"},48:{"x":379, "y":144,"figure":"none"},49:{"x":50, "y":97,"figure":bauer1_s},50:{"x":97, "y":97,"figure":bauer2_s},51:{"x":144, "y":97,"figure":bauer3_s},52:{"x":191, "y":97,"figure":bauer4_s},53:{"x":238, "y":97,"figure":bauer5_s},54:{"x":285, "y":97,"figure":bauer6_s},55:{"x":332, "y":97,"figure":bauer7_s},56:{"x":379, "y":97,"figure":bauer8_s},57:{"x":50, "y":50,"figure":turm1_s},58:{"x":97, "y":50,"figure":springer1_s},59:{"x":144, "y":50,"figure":laeufer1_s},60:{"x":191, "y":50,"figure":dame_s},61:{"x":238, "y":50,"figure":koenig_s},62:{"x":285, "y":50,"figure":laeufer2_s},63:{"x":332, "y":50,"figure":springer2_s},64:{"x":379, "y":50,"figure":turm2_s}}
punkte = [punkt1, punkt2, punkt3, punkt4, punkt5, punkt6, punkt7, punkt8, punkt9, punkt10, punkt11, punkt12, punkt13, punkt14, punkt15, punkt16, punkt17, punkt18, punkt19, punkt20, punkt21, punkt22, punkt23, punkt24, punkt25, punkt26, punkt27, punkt28, punkt29, punkt30, punkt31, punkt32, punkt33, punkt34, punkt35, punkt36, punkt37, punkt38, punkt39, punkt40, punkt41, punkt42, punkt43, punkt44, punkt45, punkt46, punkt47, punkt48, punkt49, punkt50, punkt51, punkt52, punkt53, punkt54, punkt55, punkt56, punkt57, punkt58, punkt59, punkt60, punkt61, punkt62, punkt63, punkt64]
alle_figuren=[bauer1_w, bauer2_w, bauer3_w, bauer4_w, bauer5_w, bauer6_w, bauer7_w, bauer8_w, turm1_w, turm2_w, springer1_w, springer2_w, laeufer1_w, laeufer2_w, koenig_w, dame_w, bauer1_s, bauer2_s, bauer3_s, bauer4_s, bauer5_s, bauer6_s, bauer7_s, bauer8_s, turm1_s, turm2_s, springer1_s, springer2_s, laeufer1_s, laeufer2_s, koenig_s, dame_s]

def figuren_plazieren():
    for i in felder:
        if felder[i]["figure"]!="none":
            felder[i]["figure"].place(x=felder[i]["x"], y=felder[i]["y"])

figuren_plazieren()
fenster.mainloop()