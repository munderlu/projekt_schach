from tkinter import *
from PIL import ImageTk, Image
import copy
fenster=Tk()
fenster.title("Schach Projekt")
rahmen=Frame(fenster, relief="ridge", borderwidth=5)
rahmen.pack()
schachbrett_bild=ImageTk.PhotoImage(Image.open("Bilder\Schachbrett.png"))
schachbrett=Label(rahmen, image=schachbrett_bild)
schachbrett.pack(expand=True, padx=30, pady=30)
weristdran="weiß"
aktuelle_figur="none"
schachWeiß=False
schachSchwarz=False
moegliche_züge=[]
rochade={"turm1_w_gezogen": False, "turm2_w_gezogen": False, "koenig_w_gezogen":False, "turm1_s_gezogen": False, "turm2_s_gezogen": False, "koenig_s_gezogen": False}

class Schachfigur(Button):
    farbe="?"
    art="?"

dame2_s=Schachfigur(rahmen)
dame3_s=Schachfigur(rahmen)
dame4_s=Schachfigur(rahmen)
dame5_s=Schachfigur(rahmen)
dame6_s=Schachfigur(rahmen)
dame7_s=Schachfigur(rahmen)
dame8_s=Schachfigur(rahmen)
dame9_s=Schachfigur(rahmen)
dame2_w=Schachfigur(rahmen)
dame3_w=Schachfigur(rahmen)
dame4_w=Schachfigur(rahmen)
dame5_w=Schachfigur(rahmen)
dame6_w=Schachfigur(rahmen)
dame7_w=Schachfigur(rahmen)
dame8_w=Schachfigur(rahmen)
dame9_w=Schachfigur(rahmen)
turm3_s=Schachfigur(rahmen)
turm4_s=Schachfigur(rahmen)
turm5_s=Schachfigur(rahmen)
turm6_s=Schachfigur(rahmen)
turm7_s=Schachfigur(rahmen)
turm8_s=Schachfigur(rahmen)
turm9_s=Schachfigur(rahmen)
turm10_s=Schachfigur(rahmen)
turm3_w=Schachfigur(rahmen)
turm4_w=Schachfigur(rahmen)
turm5_w=Schachfigur(rahmen)
turm6_w=Schachfigur(rahmen)
turm7_w=Schachfigur(rahmen)
turm8_w=Schachfigur(rahmen)
turm9_w=Schachfigur(rahmen)
turm10_w=Schachfigur(rahmen)
laeufer3_s=Schachfigur(rahmen)
laeufer4_s=Schachfigur(rahmen)
laeufer5_s=Schachfigur(rahmen)
laeufer6_s=Schachfigur(rahmen)
laeufer7_s=Schachfigur(rahmen)
laeufer8_s=Schachfigur(rahmen)
laeufer9_s=Schachfigur(rahmen)
laeufer10_s=Schachfigur(rahmen)
laeufer3_w=Schachfigur(rahmen)
laeufer4_w=Schachfigur(rahmen)
laeufer5_w=Schachfigur(rahmen)
laeufer6_w=Schachfigur(rahmen)
laeufer7_w=Schachfigur(rahmen)
laeufer8_w=Schachfigur(rahmen)
laeufer9_w=Schachfigur(rahmen)
laeufer10_w=Schachfigur(rahmen)
springer3_s=Schachfigur(rahmen)
springer4_s=Schachfigur(rahmen)
springer5_s=Schachfigur(rahmen)
springer6_s=Schachfigur(rahmen)
springer7_s=Schachfigur(rahmen)
springer8_s=Schachfigur(rahmen)
springer9_s=Schachfigur(rahmen)
springer10_s=Schachfigur(rahmen)
springer3_w=Schachfigur(rahmen)
springer4_w=Schachfigur(rahmen)
springer5_w=Schachfigur(rahmen)
springer6_w=Schachfigur(rahmen)
springer7_w=Schachfigur(rahmen)
springer8_w=Schachfigur(rahmen)
springer9_w=Schachfigur(rahmen)
springer10_w=Schachfigur(rahmen)
verwandelte_figuren={"damen_schwarz":[dame2_s, dame3_s, dame4_s, dame5_s, dame6_s, dame7_s, dame8_s, dame9_s], "damen_weiß":[dame2_w, dame3_w, dame4_w, dame5_w, dame6_w, dame7_w, dame8_w, dame9_w], "tuerme_schwarz":[turm3_s, turm4_s, turm5_s, turm6_s, turm7_s, turm8_s, turm9_s, turm10_s], "tuerme_weiß":[turm3_w, turm4_w, turm5_w, turm6_w, turm7_w, turm8_w, turm9_w, turm10_w], "laeufer_schwarz":[laeufer3_s, laeufer4_s, laeufer5_s, laeufer6_s, laeufer7_s, laeufer8_s, laeufer9_s, laeufer10_s], "laeufer_schwarz":[laeufer3_w, laeufer4_w, laeufer5_w, laeufer6_w, laeufer7_w, laeufer8_w, laeufer9_w, laeufer10_w], "springer_schwarz":[springer3_s, springer4_s, springer5_s, springer6_s, springer7_s, springer8_s, springer9_s, springer10_s], "springer_weiß":[springer3_w, springer4_w, springer5_w, springer6_w, springer7_w, springer8_w, springer9_w, springer10_w]}
for i in verwandelte_figuren:
    for k in verwandelte_figuren[i]:
        if i=="damen_schwarz":
            k.art="dame"
            k.farbe="schwarz"
        if i=="damen_weiß":
            k.art="dame"
            k.farbe="weiß"
        if i=="tuerme_schwarz":
            k.art="turm"
            k.farbe="schwarz"
        if i=="tuerme_weiß":
            k.art="turm"
            k.farbe="weiß"
        if i=="laeufer_schwarz":
            k.art="laeufer"
            k.farbe="schwarz"
        if i=="laeufer_weiß":
            k.art="laeufer"
            k.farbe="weiß"
        if i=="springer_schwarz":
            k.art="springer"
            k.farbe="schwarz"
        if i=="springer_weiß":
            k.art="springer"
            k.farbe="weiß"

moegliche_ziele={1:{"button_Nr": "none", "x":"none", "y":"none"}, 2:{"button_Nr": "none", "x":"none", "y":"none"}, 3:{"button_Nr": "none", "x":"none", "y":"none"}, 4:{"button_Nr": "none", "x":"none", "y":"none"}, 5:{"button_Nr": "none", "x":"none", "y":"none"}, 6:{"button_Nr": "none", "x":"none", "y":"none"}, 7:{"button_Nr": "none", "x":"none", "y":"none"}, 8:{"button_Nr": "none", "x":"none", "y":"none"}, 9:{"button_Nr": "none", "x":"none", "y":"none"}, 10:{"button_Nr": "none", "x":"none", "y":"none"}, 11:{"button_Nr": "none", "x":"none", "y":"none"}, 12:{"button_Nr": "none", "x":"none", "y":"none"}, 13:{"button_Nr": "none", "x":"none", "y":"none"}, 14:{"button_Nr": "none", "x":"none", "y":"none"}, 15:{"button_Nr": "none", "x":"none", "y":"none"}, 16:{"button_Nr": "none", "x":"none", "y":"none"}, 17:{"button_Nr": "none", "x":"none", "y":"none"}, 18:{"button_Nr": "none", "x":"none", "y":"none"}, 19:{"button_Nr": "none", "x":"none", "y":"none"}, 20:{"button_Nr": "none", "x":"none", "y":"none"}, 21:{"button_Nr": "none", "x":"none", "y":"none"}, 22:{"button_Nr": "none", "x":"none", "y":"none"}, 23:{"button_Nr": "none", "x":"none", "y":"none"}, 24:{"button_Nr": "none", "x":"none", "y":"none"}, 25:{"button_Nr": "none", "x":"none", "y":"none"}, 26:{"button_Nr": "none", "x":"none", "y":"none"}, 27:{"button_Nr": "none", "x":"none", "y":"none"}}

def alleZügeBerechnenWeiß(felder_kopie):
    global moegliche_züge
    for figur in alle_figuren:
        if(figur.farbe=="weiß"):
            if(figur.art=="bauer"):
                for i in felder_kopie:
                    if felder_kopie[i]["figure"]==figur:
                        if felder_kopie[i+8]["figure"]=="none":
                            moegliche_züge.append({"x": felder_kopie[i]["x"], "y": felder_kopie[i]["y"]-47})
                        if felder_kopie[i]["y"]==332 and felder_kopie[i+8]["figure"]=="none" and felder_kopie[i+16]["figure"]=="none":
                            moegliche_züge.append({"x": felder_kopie[i]["x"], "y": 238})
                        if felder_kopie[i]["x"]!=379:
                            if felder_kopie[i+9]["figure"]!="none"and felder_kopie[i+9]["figure"].farbe=="schwarz":
                                moegliche_züge.append({"x": felder_kopie[i]["x"]+47, "y": felder_kopie[i]["y"]-47})
                        if felder_kopie[i]["x"]!=50:
                            if felder_kopie[i+7]["figure"]!="none"and felder_kopie[i+7]["figure"].farbe=="schwarz":
                                moegliche_züge.append({"x": felder_kopie[i]["x"]-47, "y": felder_kopie[i]["y"]-47})
            if(figur.art=="turm"):
                for i in felder_kopie:
                    if felder_kopie[i]["figure"]==figur:
                        figurPlatz=i
                        figurX=felder_kopie[figurPlatz]["x"]
                        figurY=felder_kopie[figurPlatz]["y"]
                        zählvariable=1
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX and felder_kopie[k]["y"]==figurY-j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="schwarz":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX and felder_kopie[k]["y"]==figurY+j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="schwarz":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+j*47 and felder_kopie[k]["y"]==figurY:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="schwarz":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-j*47 and felder_kopie[k]["y"]==figurY:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="schwarz":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
            if(figur.art=="springer"):
                for i in felder_kopie:
                    if felder_kopie[i]["figure"]==figur:
                        figurX=felder_kopie[i]["x"]
                        figurY=felder_kopie[i]["y"]
                        for j in felder_kopie:
                            if felder_kopie[j]["y"]==figurY-2*47 and felder_kopie[j]["x"]==figurX+47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="schwarz":
                                    moegliche_züge.append({"x": felder_kopie[j]["x"], "y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY-2*47 and felder_kopie[j]["x"]==figurX-47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="schwarz":
                                    moegliche_züge.append({"x": felder_kopie[j]["x"], "y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY-47 and felder_kopie[j]["x"]==figurX+2*47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="schwarz":
                                    moegliche_züge.append({"x": felder_kopie[j]["x"], "y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY+47 and felder_kopie[j]["x"]==figurX+2*47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="schwarz":
                                    moegliche_züge.append({"x": felder_kopie[j]["x"], "y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY+2*47 and felder_kopie[j]["x"]==figurX+47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="schwarz":
                                    moegliche_züge.append({"x": felder_kopie[j]["x"], "y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY+2*47 and felder_kopie[j]["x"]==figurX-47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="schwarz":
                                    moegliche_züge.append({"x": felder_kopie[j]["x"], "y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY+47 and felder_kopie[j]["x"]==figurX-2*47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="schwarz":
                                    moegliche_züge.append({"x": felder_kopie[j]["x"], "y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY-47 and felder_kopie[j]["x"]==figurX-2*47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="schwarz":
                                    moegliche_züge.append({"x": felder_kopie[j]["x"], "y": felder_kopie[j]["y"]})
            if(figur.art=="laeufer"):
                for i in felder_kopie:
                    if felder_kopie[i]["figure"]==figur:
                        figurPlatz=i
                        figurX=felder_kopie[figurPlatz]["x"]
                        figurY=felder_kopie[figurPlatz]["y"]
                        zählvariable=1
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-j*47 and felder_kopie[k]["y"]==figurY-j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="schwarz":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-j*47 and felder_kopie[k]["y"]==figurY+j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="schwarz":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+j*47 and felder_kopie[k]["y"]==figurY-j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="schwarz":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+j*47 and felder_kopie[k]["y"]==figurY+j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="schwarz":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
            if(figur.art=="koenig"):
                for i in felder_kopie:
                    if felder_kopie[i]["figure"]==figur:
                        figurPlatz=i
                        figurX=felder_kopie[figurPlatz]["x"]
                        figurY=felder_kopie[figurPlatz]["y"]
                        zählvariable=1
                        for k in felder_kopie:
                            if felder_kopie[k]["x"]==figurX and felder_kopie[k]["y"]==figurY-47:
                                if felder_kopie[k]["figure"]!="none":
                                    if felder_kopie[k]["figure"].farbe!="schwarz":
                                        break
                                moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                zählvariable+=1
                                break
                        for k in felder_kopie:
                            if felder_kopie[k]["x"]==figurX and felder_kopie[k]["y"]==figurY+47:
                                if felder_kopie[k]["figure"]!="none":
                                    if felder_kopie[k]["figure"].farbe!="schwarz":
                                        break
                                moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                zählvariable+=1
                                break
                        for k in felder_kopie:
                            if felder_kopie[k]["x"]==figurX+47 and felder_kopie[k]["y"]==figurY:
                                if felder_kopie[k]["figure"]!="none":
                                    if felder_kopie[k]["figure"].farbe!="schwarz":
                                        break
                                moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                zählvariable+=1
                                break
                        for k in felder_kopie:
                            if felder_kopie[k]["x"]==figurX-47 and felder_kopie[k]["y"]==figurY:
                                if felder_kopie[k]["figure"]!="none":
                                    if felder_kopie[k]["figure"].farbe!="schwarz":
                                        break
                                moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                zählvariable+=1
                                break
                        for k in felder_kopie:
                            if felder_kopie[k]["x"]==figurX-47 and felder_kopie[k]["y"]==figurY-47:
                                if felder_kopie[k]["figure"]!="none":
                                    if felder_kopie[k]["figure"].farbe!="schwarz":
                                        break
                                moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                zählvariable+=1
                                break
                        for k in felder_kopie:
                            if felder_kopie[k]["x"]==figurX-47 and felder_kopie[k]["y"]==figurY+47:
                                if felder_kopie[k]["figure"]!="none":
                                    if felder_kopie[k]["figure"].farbe!="schwarz":
                                        break
                                moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                zählvariable+=1
                                break
                        for k in felder_kopie:
                            if felder_kopie[k]["x"]==figurX+47 and felder_kopie[k]["y"]==figurY-47:
                                if felder_kopie[k]["figure"]!="none":
                                    if felder_kopie[k]["figure"].farbe!="schwarz":
                                        break
                                moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                zählvariable+=1
                                break
                        for k in felder_kopie:
                            if felder_kopie[k]["x"]==figurX+47 and felder_kopie[k]["y"]==figurY+47:
                                if felder_kopie[k]["figure"]!="none":
                                    if felder_kopie[k]["figure"].farbe!="schwarz":
                                        break
                                moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                zählvariable+=1
                                break
            if(figur.art=="dame"):
                for i in felder_kopie:
                    if felder_kopie[i]["figure"]==figur:
                        figurPlatz=i
                        figurX=felder_kopie[figurPlatz]["x"]
                        figurY=felder_kopie[figurPlatz]["y"]
                        zählvariable=1
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX and felder_kopie[k]["y"]==figurY-j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="schwarz":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX and felder_kopie[k]["y"]==figurY+j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="schwarz":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+j*47 and felder_kopie[k]["y"]==figurY:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="schwarz":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-j*47 and felder_kopie[k]["y"]==figurY:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="schwarz":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-j*47 and felder_kopie[k]["y"]==figurY-j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="schwarz":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-j*47 and felder_kopie[k]["y"]==figurY+j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="schwarz":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+j*47 and felder_kopie[k]["y"]==figurY-j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="schwarz":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+j*47 and felder_kopie[k]["y"]==figurY+j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="schwarz":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break

def alleZügeBerechnenSchwarz(felder_kopie):
    global moegliche_züge
    for figur in alle_figuren:
        if(figur.farbe=="schwarz"):
            if(figur.art=="bauer"):
                for i in felder_kopie:
                    if felder_kopie[i]["figure"]==figur:
                        if felder_kopie[i-8]["figure"]=="none":
                            moegliche_züge.append({"x": felder_kopie[i]["x"], "y": felder_kopie[i]["y"]+47})
                        if felder_kopie[i]["y"]==97 and felder_kopie[i-8]["figure"]=="none" and felder_kopie[i-16]["figure"]=="none":
                            moegliche_züge.append({"x": felder_kopie[i]["x"], "y": 191})
                        if felder_kopie[i]["x"]!=50:
                            if felder_kopie[i-9]["figure"]!="none"and felder_kopie[i-9]["figure"].farbe=="weiß":
                                moegliche_züge.append({"x": felder_kopie[i]["x"]-47, "y": felder_kopie[i]["y"]+47})
                        if felder_kopie[i]["x"]!=379:
                            if felder_kopie[i-7]["figure"]!="none"and felder_kopie[i-7]["figure"].farbe=="weiß":
                                moegliche_züge.append({"x": felder_kopie[i]["x"]+47, "y": felder_kopie[i]["x"]+47})
            if(figur.art=="turm"):
                for i in felder_kopie:
                    if felder_kopie[i]["figure"]==figur:
                        figurPlatz=i
                        figurX=felder_kopie[figurPlatz]["x"]
                        figurY=felder_kopie[figurPlatz]["y"]
                        zählvariable=1
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX and felder_kopie[k]["y"]==figurY-j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX and felder_kopie[k]["y"]==figurY+j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+j*47 and felder_kopie[k]["y"]==figurY:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-j*47 and felder_kopie[k]["y"]==figurY:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
            if(figur.art=="springer"):
                for i in felder_kopie:
                    if felder_kopie[i]["figure"]==figur:
                        figurX=felder_kopie[i]["x"]
                        figurY=felder_kopie[i]["y"]
                        for j in felder_kopie:
                            if felder_kopie[j]["y"]==figurY-2*47 and felder_kopie[j]["x"]==figurX+47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="weiß":
                                    moegliche_züge.append({"x": felder_kopie[j]["x"],"y": felder_kopie[j]["y"]})    
                            if felder_kopie[j]["y"]==figurY-2*47 and felder_kopie[j]["x"]==figurX-47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="weiß":
                                    moegliche_züge.append({"x": felder_kopie[j]["x"],"y": felder_kopie[j]["y"]})   
                            if felder_kopie[j]["y"]==figurY-47 and felder_kopie[j]["x"]==figurX+2*47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="weiß":
                                    moegliche_züge.append({"x": felder_kopie[j]["x"],"y": felder_kopie[j]["y"]})    
                            if felder_kopie[j]["y"]==figurY+47 and felder_kopie[j]["x"]==figurX+2*47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="weiß":
                                    moegliche_züge.append({"x": felder_kopie[j]["x"],"y": felder_kopie[j]["y"]})    
                            if felder_kopie[j]["y"]==figurY+2*47 and felder_kopie[j]["x"]==figurX+47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="weiß":
                                    moegliche_züge.append({"x": felder_kopie[j]["x"],"y": felder_kopie[j]["y"]})       
                            if felder_kopie[j]["y"]==figurY+2*47 and felder_kopie[j]["x"]==figurX-47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="weiß":
                                    moegliche_züge.append({"x": felder_kopie[j]["x"],"y": felder_kopie[j]["y"]})       
                            if felder_kopie[j]["y"]==figurY+47 and felder_kopie[j]["x"]==figurX-2*47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="weiß":
                                    moegliche_züge.append({"x": felder_kopie[j]["x"],"y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY-47 and felder_kopie[j]["x"]==figurX-2*47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="weiß":
                                    moegliche_züge.append({"x": felder_kopie[j]["x"],"y": felder_kopie[j]["y"]})
            if(figur.art=="laeufer"):
                for i in felder_kopie:
                    if felder_kopie[i]["figure"]==figur:
                        figurPlatz=i
                        figurX=felder_kopie[figurPlatz]["x"]
                        figurY=felder_kopie[figurPlatz]["y"]
                        zählvariable=1
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-j*47 and felder_kopie[k]["y"]==figurY-j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-j*47 and felder_kopie[k]["y"]==figurY+j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+j*47 and felder_kopie[k]["y"]==figurY-j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+j*47 and felder_kopie[k]["y"]==figurY+j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
            if(figur.art=="koenig"):
                for i in felder_kopie:
                        if felder_kopie[i]["figure"]==figur:
                            figurPlatz=i
                            figurX=felder_kopie[figurPlatz]["x"]
                            figurY=felder_kopie[figurPlatz]["y"]
                            zählvariable=1
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX and felder_kopie[k]["y"]==figurY-47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX and felder_kopie[k]["y"]==figurY+47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+47 and felder_kopie[k]["y"]==figurY:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-47 and felder_kopie[k]["y"]==figurY:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-47 and felder_kopie[k]["y"]==figurY-47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-47 and felder_kopie[k]["y"]==figurY+47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+47 and felder_kopie[k]["y"]==figurY-47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+47 and felder_kopie[k]["y"]==figurY+47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
            if(figur.art=="dame"):
                for i in felder_kopie:
                    if felder_kopie[i]["figure"]==figur:
                        figurPlatz=i
                        figurX=felder_kopie[figurPlatz]["x"]
                        figurY=felder_kopie[figurPlatz]["y"]
                        zählvariable=1
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX and felder_kopie[k]["y"]==figurY-j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX and felder_kopie[k]["y"]==figurY+j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+j*47 and felder_kopie[k]["y"]==figurY:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-j*47 and felder_kopie[k]["y"]==figurY:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-j*47 and felder_kopie[k]["y"]==figurY-j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-j*47 and felder_kopie[k]["y"]==figurY+j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+j*47 and felder_kopie[k]["y"]==figurY-j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+j*47 and felder_kopie[k]["y"]==figurY+j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiß":
                                            break
                                    moegliche_züge.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break

def schachWeißeFigurBerechnen(felder_kopie):
    global schachWeiß
    global moegliche_züge
    schachWeiß=False
    moegliche_züge=[]
    alleZügeBerechnenSchwarz(felder_kopie)
    for figur in alle_figuren:
        if figur.farbe=="weiß" and figur.art=="koenig":
            for i in felder_kopie:
                if felder_kopie[i]["figure"]==figur:
                    XKönig=felder_kopie[i]["x"]
                    YKönig=felder_kopie[i]["y"]
    for i in moegliche_züge:
        if i["x"]==XKönig and i["y"]==YKönig:
            schachWeiß=True

def schachSchwarzFigurBerechnen(felder_kopie):
    global schachSchwarz
    global moegliche_züge
    schachSchwarz=False
    moegliche_züge=[]
    alleZügeBerechnenWeiß(felder_kopie)
    for figur in alle_figuren:
        if figur.farbe=="schwarz" and figur.art=="koenig":
            for i in felder_kopie:
                if felder_kopie[i]["figure"]==figur:
                    XKönig=felder_kopie[i]["x"]
                    YKönig=felder_kopie[i]["y"]
    for i in moegliche_züge:
        if i["x"]==XKönig and i["y"]==YKönig:
            schachSchwarz=True

def schachWeißBerechnen():
    punkt_rot.place_forget()
    global schachWeiß
    global moegliche_züge
    schachMatt=True
    alleZügeBerechnenSchwarz(felder)
    for figur in alle_figuren:
        if figur.farbe=="weiß" and figur.art=="koenig":
            for i in felder:
                if felder[i]["figure"]==figur:
                    XKönig=felder[i]["x"]
                    YKönig=felder[i]["y"]
    for i in moegliche_züge:
        if i["x"]==XKönig and i["y"]==YKönig:
            schachWeiß=True
            punkt_rot.place(x=XKönig, y=YKönig)
    for figur in alle_figuren:
        if figur.farbe=="weiß":
            if figur.art=="bauer":
                zuege_bauer_weiß(figur)
                for i in moegliche_ziele:
                    if moegliche_ziele[i]["x"]!="none":
                        schachMatt=False
                        break
            if figur.art=="turm":
                zuege_turm_weiß(figur)
                for i in moegliche_ziele:
                    if moegliche_ziele[i]["x"]!="none":
                        schachMatt=False
                        break
            if figur.art=="laeufer":
                zuege_laeufer_weiß(figur)
                for i in moegliche_ziele:
                    if moegliche_ziele[i]["x"]!="none":
                        schachMatt=False
                        break
            if figur.art=="dame":
                zuege_dame_weiß(figur)
                for i in moegliche_ziele:
                    if moegliche_ziele[i]["x"]!="none":
                        schachMatt=False
                        break
            if figur.art=="koenig":
                zuege_koenig_weiß(figur)
                for i in moegliche_ziele:
                    if moegliche_ziele[i]["x"]!="none":
                        schachMatt=False
                        break
            if figur.art=="springer":
                zuege_springer_weiß(figur)
                for i in moegliche_ziele:
                    if moegliche_ziele[i]["x"]!="none":
                        schachMatt=False
                        break
    for punkt in punkte:
        punkt.place_forget()
    if schachMatt:
        schrift=Label(text="Schach Matt:\nschwarz gewinnt", font="Arial, 30")
        schrift.place(x=100, y=200)

def schachSchwarzBerechnen():
    punkt_rot.place_forget()
    global schachSchwarz
    global moegliche_züge
    schachMatt=True
    alleZügeBerechnenWeiß(felder)
    for figur in alle_figuren:
        if figur.farbe=="schwarz" and figur.art=="koenig":
            for i in felder:
                if felder[i]["figure"]==figur:
                    XKönig=felder[i]["x"]
                    YKönig=felder[i]["y"]
    for i in moegliche_züge:
        if i["x"]==XKönig and i["y"]==YKönig:
            schachSchwarz=True
            punkt_rot.place(x=XKönig, y=YKönig)
    for figur in alle_figuren:
        if figur.farbe=="schwarz":
            if figur.art=="bauer":
                zuege_bauer_schwarz(figur)
                for i in moegliche_ziele:
                    if moegliche_ziele[i]["x"]!="none":
                        schachMatt=False
                        break
            if figur.art=="turm":
                zuege_turm_schwarz(figur)
                for i in moegliche_ziele:
                    if moegliche_ziele[i]["x"]!="none":
                        schachMatt=False
                        break
            if figur.art=="laeufer":
                zuege_laeufer_schwarz(figur)
                for i in moegliche_ziele:
                    if moegliche_ziele[i]["x"]!="none":
                        schachMatt=False
                        break
            if figur.art=="dame":
                zuege_dame_schwarz(figur)
                for i in moegliche_ziele:
                    if moegliche_ziele[i]["x"]!="none":
                        schachMatt=False
                        break
            if figur.art=="koenig":
                zuege_koenig_schwarz(figur)
                for i in moegliche_ziele:
                    if moegliche_ziele[i]["x"]!="none":
                        schachMatt=False
                        break
            if figur.art=="springer":
                zuege_springer_schwarz(figur)
                for i in moegliche_ziele:
                    if moegliche_ziele[i]["x"]!="none":
                        schachMatt=False
                        break
    for punkt in punkte:
        punkt.place_forget()
    if schachMatt:
        schrift=Label(text="Schach Matt:\nweiß gewinnt", font="Arial, 30")
        schrift.place(x=100, y=200)

def setzeZieleAufNull():
    global moegliche_ziele
    moegliche_ziele={1:{"button_Nr": "none", "x":"none", "y":"none"}, 2:{"button_Nr": "none", "x":"none", "y":"none"}, 3:{"button_Nr": "none", "x":"none", "y":"none"}, 4:{"button_Nr": "none", "x":"none", "y":"none"}, 5:{"button_Nr": "none", "x":"none", "y":"none"}, 6:{"button_Nr": "none", "x":"none", "y":"none"}, 7:{"button_Nr": "none", "x":"none", "y":"none"}, 8:{"button_Nr": "none", "x":"none", "y":"none"}, 9:{"button_Nr": "none", "x":"none", "y":"none"}, 10:{"button_Nr": "none", "x":"none", "y":"none"}, 11:{"button_Nr": "none", "x":"none", "y":"none"}, 12:{"button_Nr": "none", "x":"none", "y":"none"}, 13:{"button_Nr": "none", "x":"none", "y":"none"}, 14:{"button_Nr": "none", "x":"none", "y":"none"}, 15:{"button_Nr": "none", "x":"none", "y":"none"}, 16:{"button_Nr": "none", "x":"none", "y":"none"}, 17:{"button_Nr": "none", "x":"none", "y":"none"}, 18:{"button_Nr": "none", "x":"none", "y":"none"}, 19:{"button_Nr": "none", "x":"none", "y":"none"}, 20:{"button_Nr": "none", "x":"none", "y":"none"}, 21:{"button_Nr": "none", "x":"none", "y":"none"}, 22:{"button_Nr": "none", "x":"none", "y":"none"}, 23:{"button_Nr": "none", "x":"none", "y":"none"}, 24:{"button_Nr": "none", "x":"none", "y":"none"}, 25:{"button_Nr": "none", "x":"none", "y":"none"}, 26:{"button_Nr": "none", "x":"none", "y":"none"}, 27:{"button_Nr": "none", "x":"none", "y":"none"}}
    for i in punkte:
        i.place_forget()

def felder_kopie_ausgeben():
    tkinterObjekte=[]
    for i in felder:
        if str(felder[i]["figure"])[:7]==".!frame":
            tkinterObjekte.append(felder[i]["figure"])
            felder[i]["figure"]="tkinter"
    felder_kopie=copy.deepcopy(felder)
    for i in felder:
        if felder[i]["figure"]=="tkinter":
            felder[i]["figure"]=tkinterObjekte[0]
            felder_kopie[i]["figure"]=tkinterObjekte[0]
            tkinterObjekte.pop(0)
    return felder_kopie

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
                    felder_kopie=felder_kopie_ausgeben()
                    felder_kopie[i]["figure"]="none"
                    felder_kopie[i+8]["figure"]=figur
                    schachWeißeFigurBerechnen(felder_kopie)
                    if schachWeiß==False:
                        moegliche_ziele[1]["x"]=felder[i]["x"]
                        moegliche_ziele[1]["y"]=felder[i]["y"]-47
                if felder[i]["y"]==332 and felder[i+8]["figure"]=="none" and felder[i+16]["figure"]=="none":
                    felder_kopie=felder_kopie_ausgeben()
                    felder_kopie[i]["figure"]="none"
                    felder_kopie[i+16]["figure"]=figur
                    schachWeißeFigurBerechnen(felder_kopie)
                    if schachWeiß==False:
                        moegliche_ziele[2]["x"]=felder[i]["x"]
                        moegliche_ziele[2]["y"]=238
                if felder[i]["x"]!=379:
                    if felder[i+9]["figure"]!="none"and felder[i+9]["figure"].farbe=="schwarz":
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[i+9]["figure"]=figur
                        schachWeißeFigurBerechnen(felder_kopie)
                        if schachWeiß==False:
                            moegliche_ziele[3]["x"]=felder[i]["x"]+47
                            moegliche_ziele[3]["y"]=felder[i]["y"]-47
                if felder[i]["x"]!=50:
                    if felder[i+7]["figure"]!="none"and felder[i+7]["figure"].farbe=="schwarz":
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[i+7]["figure"]=figur
                        schachWeißeFigurBerechnen(felder_kopie)
                        if schachWeiß==False:
                            moegliche_ziele[4]["x"]=felder[i]["x"]-47
                            moegliche_ziele[4]["y"]=felder[i]["y"]-47
        punkte_auswählen()
        punkte_plazieren()

def zuege_bauer_schwarz(figur):
    setzeZieleAufNull()
    global weristdran
    if weristdran=="schwarz":
        for i in felder:
            if felder[i]["figure"]==figur:
                global aktuelle_figur
                aktuelle_figur=figur
                if felder[i-8]["figure"]=="none":
                    felder_kopie=felder_kopie_ausgeben()
                    felder_kopie[i]["figure"]="none"
                    felder_kopie[i-8]["figure"]=figur
                    schachSchwarzFigurBerechnen(felder_kopie)
                    if schachSchwarz==False:
                        moegliche_ziele[1]["x"]=felder[i]["x"]
                        moegliche_ziele[1]["y"]=felder[i]["y"]+47
                if felder[i]["y"]==97 and felder[i-8]["figure"]=="none" and felder[i-16]["figure"]=="none":
                    felder_kopie=felder_kopie_ausgeben()
                    felder_kopie[i]["figure"]="none"
                    felder_kopie[i-16]["figure"]=figur
                    schachSchwarzFigurBerechnen(felder_kopie)
                    if schachSchwarz==False:
                        moegliche_ziele[2]["x"]=felder[i]["x"]
                        moegliche_ziele[2]["y"]=191
                if felder[i]["x"]!=50:
                    if felder[i-9]["figure"]!="none"and felder[i-9]["figure"].farbe=="weiß":
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[i-9]["figure"]=figur
                        schachSchwarzFigurBerechnen(felder_kopie)
                        if schachSchwarz==False:
                            moegliche_ziele[3]["x"]=felder[i]["x"]-47
                            moegliche_ziele[3]["y"]=felder[i]["y"]+47
                if felder[i]["x"]!=379:
                    if felder[i-7]["figure"]!="none"and felder[i-7]["figure"].farbe=="weiß":
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[i-7]["figure"]=figur
                        schachSchwarzFigurBerechnen(felder_kopie)
                        if schachSchwarz==False:
                            moegliche_ziele[4]["x"]=felder[i]["x"]+47
                            moegliche_ziele[4]["y"]=felder[i]["y"]+47
        punkte_auswählen()
        punkte_plazieren() 

def zuege_turm_weiß(figur):
    global weristdran
    if weristdran=="weiß":
        setzeZieleAufNull()
        figurPlatz="?"
        for i in felder:
            if felder[i]["figure"]==figur:
                global aktuelle_figur
                aktuelle_figur=figur
                figurPlatz=i
                figurX=felder[figurPlatz]["x"]
                figurY=felder[figurPlatz]["y"]
                zählvariable=1
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX and felder[k]["y"]==figurY-j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="schwarz":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX and felder[k]["y"]==figurY+j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="schwarz":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX+j*47 and felder[k]["y"]==figurY:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="schwarz":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX-j*47 and felder[k]["y"]==figurY:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="schwarz":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
        punkte_auswählen()
        punkte_plazieren()

def zuege_turm_schwarz(figur):
    global weristdran
    if weristdran=="schwarz":
        setzeZieleAufNull()
        figurPlatz="?"
        for i in felder:
            if felder[i]["figure"]==figur:
                global aktuelle_figur
                aktuelle_figur=figur
                figurPlatz=i
                figurX=felder[figurPlatz]["x"]
                figurY=felder[figurPlatz]["y"]
                zählvariable=1
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX and felder[k]["y"]==figurY-j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="weiß":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX and felder[k]["y"]==figurY+j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="weiß":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX+j*47 and felder[k]["y"]==figurY:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="weiß":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX-j*47 and felder[k]["y"]==figurY:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="weiß":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
        punkte_auswählen()
        punkte_plazieren()

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
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[1]["x"]=felder[j]["x"]
                                moegliche_ziele[1]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY-2*47 and felder[j]["x"]==figurX-47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[2]["x"]=felder[j]["x"]
                                moegliche_ziele[2]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY-47 and felder[j]["x"]==figurX+2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[3]["x"]=felder[j]["x"]
                                moegliche_ziele[3]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+47 and felder[j]["x"]==figurX+2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[4]["x"]=felder[j]["x"]
                                moegliche_ziele[4]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+2*47 and felder[j]["x"]==figurX+47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[5]["x"]=felder[j]["x"]
                                moegliche_ziele[5]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+2*47 and felder[j]["x"]==figurX-47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[6]["x"]=felder[j]["x"]
                                moegliche_ziele[6]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+47 and felder[j]["x"]==figurX-2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[7]["x"]=felder[j]["x"]
                                moegliche_ziele[7]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY-47 and felder[j]["x"]==figurX-2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[8]["x"]=felder[j]["x"]
                                moegliche_ziele[8]["y"]=felder[j]["y"]
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
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[1]["x"]=felder[j]["x"]
                                moegliche_ziele[1]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY-2*47 and felder[j]["x"]==figurX-47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiß":
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[2]["x"]=felder[j]["x"]
                                moegliche_ziele[2]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY-47 and felder[j]["x"]==figurX+2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiß":
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[3]["x"]=felder[j]["x"]
                                moegliche_ziele[3]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+47 and felder[j]["x"]==figurX+2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiß":
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[4]["x"]=felder[j]["x"]
                                moegliche_ziele[4]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+2*47 and felder[j]["x"]==figurX+47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiß":
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[5]["x"]=felder[j]["x"]
                                moegliche_ziele[5]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+2*47 and felder[j]["x"]==figurX-47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiß":
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[6]["x"]=felder[j]["x"]
                                moegliche_ziele[6]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+47 and felder[j]["x"]==figurX-2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiß":
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[7]["x"]=felder[j]["x"]
                                moegliche_ziele[7]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY-47 and felder[j]["x"]==figurX-2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiß":
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[8]["x"]=felder[j]["x"]
                                moegliche_ziele[8]["y"]=felder[j]["y"]
            punkte_auswählen()
            punkte_plazieren()

def zuege_laeufer_weiß(figur):
    global weristdran
    if weristdran=="weiß":
        setzeZieleAufNull()
        figurPlatz="?"
        for i in felder:
            if felder[i]["figure"]==figur:
                global aktuelle_figur
                aktuelle_figur=figur
                figurPlatz=i
                figurX=felder[figurPlatz]["x"]
                figurY=felder[figurPlatz]["y"]
                zählvariable=1
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX-j*47 and felder[k]["y"]==figurY-j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="schwarz":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX-j*47 and felder[k]["y"]==figurY+j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="schwarz":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX+j*47 and felder[k]["y"]==figurY-j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="schwarz":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX+j*47 and felder[k]["y"]==figurY+j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="schwarz":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
        punkte_auswählen()
        punkte_plazieren()

def zuege_laeufer_schwarz(figur):
    global weristdran
    if weristdran=="schwarz":
        setzeZieleAufNull()
        figurPlatz="?"
        for i in felder:
            if felder[i]["figure"]==figur:
                global aktuelle_figur
                aktuelle_figur=figur
                figurPlatz=i
                figurX=felder[figurPlatz]["x"]
                figurY=felder[figurPlatz]["y"]
                zählvariable=1
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX-j*47 and felder[k]["y"]==figurY-j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="weiß":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX-j*47 and felder[k]["y"]==figurY+j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="weiß":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX+j*47 and felder[k]["y"]==figurY-j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="weiß":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX+j*47 and felder[k]["y"]==figurY+j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="weiß":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
        punkte_auswählen()
        punkte_plazieren()

def zuege_koenig_weiß(figur):
    global weristdran
    if weristdran=="weiß":
        setzeZieleAufNull()
        figurPlatz="?"
        for i in felder:
            if felder[i]["figure"]==figur:
                global aktuelle_figur
                aktuelle_figur=figur
                figurPlatz=i
                figurX=felder[figurPlatz]["x"]
                figurY=felder[figurPlatz]["y"]
                zählvariable=1
                for k in felder:
                    if felder[k]["x"]==figurX and felder[k]["y"]==figurY-47:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="schwarz":
                                break
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachWeißeFigurBerechnen(felder_kopie)
                        if schachWeiß==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX and felder[k]["y"]==figurY+47:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="schwarz":
                                break
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachWeißeFigurBerechnen(felder_kopie)
                        if schachWeiß==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX+47 and felder[k]["y"]==figurY:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="schwarz":
                                break
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachWeißeFigurBerechnen(felder_kopie)
                        if schachWeiß==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX-47 and felder[k]["y"]==figurY:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="schwarz":
                                break
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachWeißeFigurBerechnen(felder_kopie)
                        if schachWeiß==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX-47 and felder[k]["y"]==figurY-47:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="schwarz":
                                break
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachWeißeFigurBerechnen(felder_kopie)
                        if schachWeiß==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX-47 and felder[k]["y"]==figurY+47:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="schwarz":
                                break
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachWeißeFigurBerechnen(felder_kopie)
                        if schachWeiß==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX+47 and felder[k]["y"]==figurY-47:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="schwarz":
                                break
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachWeißeFigurBerechnen(felder_kopie)
                        if schachWeiß==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX+47 and felder[k]["y"]==figurY+47:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="schwarz":
                                break
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachWeißeFigurBerechnen(felder_kopie)
                        if schachWeiß==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                if rochade["koenig_w_gezogen"]==False and rochade["turm1_w_gezogen"]==False:
                    rochadeGehtNicht=False
                    if felder[2]["figure"]!="none":
                        rochadeGehtNicht=True
                    if felder[3]["figure"]!="none":
                        rochadeGehtNicht=True
                    if felder[4]["figure"]!="none":
                        rochadeGehtNicht=True
                    schachWeißeFigurBerechnen(felder)
                    if schachWeiß==True:
                        rochadeGehtNicht=True
                    felder_kopie=felder_kopie_ausgeben()
                    felder_kopie[5]["figure"]="none"
                    felder_kopie[4]["figure"]=koenig_w
                    schachWeißeFigurBerechnen(felder_kopie)
                    if schachWeiß==True:
                        rochadeGehtNicht=True
                    felder_kopie[4]["figure"]="none"
                    felder_kopie[3]["figure"]=koenig_w
                    schachWeißeFigurBerechnen(felder_kopie)
                    if schachWeiß==True:
                        rochadeGehtNicht=True
                    if rochadeGehtNicht==False:
                        punkt_lange_rochade_weiß.place(x=144, y=379)
                if rochade["koenig_w_gezogen"]==False and rochade["turm2_w_gezogen"]==False:
                    rochadeGehtNicht=False
                    if felder[7]["figure"]!="none":
                        rochadeGehtNicht=True
                    if felder[6]["figure"]!="none":
                        rochadeGehtNicht=True
                    schachWeißeFigurBerechnen(felder)
                    if schachWeiß==True:
                        rochadeGehtNicht=True
                    felder_kopie=felder_kopie_ausgeben()
                    felder_kopie[5]["figure"]="none"
                    felder_kopie[6]["figure"]=koenig_w
                    schachWeißeFigurBerechnen(felder_kopie)
                    if schachWeiß==True:
                        rochadeGehtNicht=True
                    felder_kopie[6]["figure"]="none"
                    felder_kopie[7]["figure"]=koenig_w
                    schachWeißeFigurBerechnen(felder_kopie)
                    if schachWeiß==True:
                        rochadeGehtNicht=True
                    if rochadeGehtNicht==False:
                        punkt_kurze_rochade_weiß.place(x=332, y=379)
        punkte_auswählen()
        punkte_plazieren()

def zuege_koenig_schwarz(figur):
    global weristdran
    if weristdran=="schwarz":
        setzeZieleAufNull()
        figurPlatz="?"
        for i in felder:
            if felder[i]["figure"]==figur:
                global aktuelle_figur
                aktuelle_figur=figur
                figurPlatz=i
                figurX=felder[figurPlatz]["x"]
                figurY=felder[figurPlatz]["y"]
                zählvariable=1
                for k in felder:
                    if felder[k]["x"]==figurX and felder[k]["y"]==figurY-47:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="weiß":
                                break
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachSchwarzFigurBerechnen(felder_kopie)
                        if schachSchwarz==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX and felder[k]["y"]==figurY+47:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="weiß":
                                break
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachSchwarzFigurBerechnen(felder_kopie)
                        if schachSchwarz==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX+47 and felder[k]["y"]==figurY:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="weiß":
                                break
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachSchwarzFigurBerechnen(felder_kopie)
                        if schachSchwarz==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX-47 and felder[k]["y"]==figurY:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="weiß":
                                break
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachSchwarzFigurBerechnen(felder_kopie)
                        if schachSchwarz==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX-47 and felder[k]["y"]==figurY-47:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="weiß":
                                break
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachSchwarzFigurBerechnen(felder_kopie)
                        if schachSchwarz==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX-47 and felder[k]["y"]==figurY+47:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="weiß":
                                break
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachSchwarzFigurBerechnen(felder_kopie)
                        if schachSchwarz==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX+47 and felder[k]["y"]==figurY-47:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="weiß":
                                break
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachSchwarzFigurBerechnen(felder_kopie)
                        if schachSchwarz==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX+47 and felder[k]["y"]==figurY+47:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="weiß":
                                break
                        felder_kopie=felder_kopie_ausgeben()
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachSchwarzFigurBerechnen(felder_kopie)
                        if schachSchwarz==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                if rochade["koenig_s_gezogen"]==False and rochade["turm1_s_gezogen"]==False:
                    rochadeGehtNicht=False
                    if felder[58]["figure"]!="none":
                        rochadeGehtNicht=True
                    if felder[59]["figure"]!="none":
                        rochadeGehtNicht=True
                    if felder[60]["figure"]!="none":
                        rochadeGehtNicht=True
                    schachSchwarzFigurBerechnen(felder)
                    if schachSchwarz==True:
                        rochadeGehtNicht=True
                    felder_kopie=felder_kopie_ausgeben()
                    felder_kopie[61]["figure"]="none"
                    felder_kopie[60]["figure"]=koenig_s
                    schachSchwarzFigurBerechnen(felder_kopie)
                    if schachSchwarz==True:
                        rochadeGehtNicht=True
                    felder_kopie[60]["figure"]="none"
                    felder_kopie[59]["figure"]=koenig_s
                    schachSchwarzFigurBerechnen(felder_kopie)
                    if schachSchwarz==True:
                        rochadeGehtNicht=True
                    if rochadeGehtNicht==False:
                        punkt_lange_rochade_schwarz.place(x=144, y=50)
                if rochade["koenig_s_gezogen"]==False and rochade["turm2_s_gezogen"]==False:
                    rochadeGehtNicht=False
                    if felder[63]["figure"]!="none":
                        rochadeGehtNicht=True
                    if felder[62]["figure"]!="none":
                        rochadeGehtNicht=True
                    schachSchwarzFigurBerechnen(felder)
                    if schachSchwarz==True:
                        rochadeGehtNicht=True
                    felder_kopie=felder_kopie_ausgeben()
                    felder_kopie[61]["figure"]="none"
                    felder_kopie[62]["figure"]=koenig_s
                    schachSchwarzFigurBerechnen(felder_kopie)
                    if schachSchwarz==True:
                        rochadeGehtNicht=True
                    felder_kopie[62]["figure"]="none"
                    felder_kopie[63]["figure"]=koenig_s
                    schachSchwarzFigurBerechnen(felder_kopie)
                    if schachSchwarz==True:
                        rochadeGehtNicht=True
                    if rochadeGehtNicht==False:
                        punkt_kurze_rochade_schwarz.place(x=332, y=50)
        punkte_auswählen()
        punkte_plazieren()

def zuege_dame_weiß(figur):
    global weristdran
    if weristdran=="weiß":
        setzeZieleAufNull()
        figurPlatz="?"
        for i in felder:
            if felder[i]["figure"]==figur:
                global aktuelle_figur
                aktuelle_figur=figur
                figurPlatz=i
                figurX=felder[figurPlatz]["x"]
                figurY=felder[figurPlatz]["y"]
                zählvariable=1
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX and felder[k]["y"]==figurY-j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="schwarz":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX and felder[k]["y"]==figurY+j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="schwarz":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX+j*47 and felder[k]["y"]==figurY:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="schwarz":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX-j*47 and felder[k]["y"]==figurY:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="schwarz":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX-j*47 and felder[k]["y"]==figurY-j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="schwarz":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX-j*47 and felder[k]["y"]==figurY+j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="schwarz":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX+j*47 and felder[k]["y"]==figurY-j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="schwarz":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX+j*47 and felder[k]["y"]==figurY+j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="schwarz":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeißeFigurBerechnen(felder_kopie)
                            if schachWeiß==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
        punkte_auswählen()
        punkte_plazieren()

def zuege_dame_schwarz(figur):
    global weristdran
    if weristdran=="schwarz":
        setzeZieleAufNull()
        figurPlatz="?"
        for i in felder:
            if felder[i]["figure"]==figur:
                global aktuelle_figur
                aktuelle_figur=figur
                figurPlatz=i
                figurX=felder[figurPlatz]["x"]
                figurY=felder[figurPlatz]["y"]
                zählvariable=1
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX and felder[k]["y"]==figurY-j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="weiß":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX and felder[k]["y"]==figurY+j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="weiß":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX+j*47 and felder[k]["y"]==figurY:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="weiß":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX-j*47 and felder[k]["y"]==figurY:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="weiß":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX-j*47 and felder[k]["y"]==figurY-j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="weiß":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX-j*47 and felder[k]["y"]==figurY+j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="weiß":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX+j*47 and felder[k]["y"]==figurY-j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="weiß":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
                for j in range (1, 8):
                    for k in felder:
                        if felder[k]["x"]==figurX+j*47 and felder[k]["y"]==figurY+j*47:
                            if felder[k]["figure"]!="none":
                                if felder[k]["figure"].farbe!="weiß":
                                    break
                            felder_kopie=felder_kopie_ausgeben()
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                                moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                            zählvariable+=1
                            break
                    if felder[k]["figure"]!="none":
                        break
        punkte_auswählen()
        punkte_plazieren()

def lange_rochade_machen_weiß():
    global felder
    global weristdran
    weristdran="schwarz"
    felder[5]["figure"]="none"
    felder[4]["figure"]=turm1_w
    felder[1]["figure"]="none"
    felder[3]["figure"]=koenig_w
    rochade["koenig_w_gezogen"]=True
    figuren_plazieren()
    for punkt in punkte:
        punkt.place_forget()

def kurze_rochade_machen_weiß():
    global felder
    global weristdran
    weristdran="schwarz"
    felder[5]["figure"]="none"
    felder[6]["figure"]=turm2_w
    felder[8]["figure"]="none"
    felder[7]["figure"]=koenig_w
    rochade["koenig_w_gezogen"]=True
    figuren_plazieren()
    for punkt in punkte:
        punkt.place_forget()

def lange_rochade_machen_schwarz():
    global felder
    global weristdran
    weristdran="weiß"
    felder[61]["figure"]="none"
    felder[60]["figure"]=turm1_s
    felder[57]["figure"]="none"
    felder[59]["figure"]=koenig_s
    rochade["koenig_s_gezogen"]=True
    figuren_plazieren()
    for punkt in punkte:
        punkt.place_forget()

def kurze_rochade_machen_schwarz():
    global felder
    global weristdran
    weristdran="weiß"
    felder[61]["figure"]="none"
    felder[62]["figure"]=turm2_s
    felder[64]["figure"]="none"
    felder[63]["figure"]=koenig_s
    rochade["koenig_s_gezogen"]=True
    figuren_plazieren()
    for punkt in punkte:
        punkt.place_forget()

def bauer_verwandeln_schwarz(aktuelle_figur, verwandel_figur, xpos, ypos):
    global felder
    global verwandelte_figuren
    if verwandel_figur=="dame":
        verwandelte_figuren["damen_schwarz"][0]["image"]=dame_s_bild
        figur=verwandelte_figuren["damen_schwarz"][0]
        verwandelte_figuren["damen_schwarz"][0]["command"]=lambda:zuege_dame_schwarz(figur)
        verwandelte_figuren["damen_schwarz"][0].place(x=xpos, y=ypos)
        aktuelle_figur.place_forget()
        alle_figuren.append(verwandelte_figuren["damen_schwarz"][0])
        for i in felder:
            if felder[i]["x"]==xpos and felder[i]["y"]==ypos:
                felder[i]["figure"]=verwandelte_figuren["damen_schwarz"][0]
        verwandelte_figuren["damen_schwarz"].pop(0)
    if verwandel_figur=="turm":
        verwandelte_figuren["tuerme_schwarz"][0]["image"]=turm_s_bild
        figur=verwandelte_figuren["tuerme_schwarz"][0]
        verwandelte_figuren["tuerme_schwarz"][0]["command"]=lambda:zuege_turm_schwarz(figur)
        verwandelte_figuren["tuerme_schwarz"][0].place(x=xpos, y=ypos)
        aktuelle_figur.place_forget()
        alle_figuren.append(verwandelte_figuren["tuerme_schwarz"][0])
        for i in felder:
            if felder[i]["x"]==xpos and felder[i]["y"]==ypos:
                felder[i]["figure"]=verwandelte_figuren["tuerme_schwarz"][0]
        verwandelte_figuren["tuerme_schwarz"].pop(0)
    if verwandel_figur=="springer":
        verwandelte_figuren["springer_schwarz"][0]["image"]=springer_s_bild
        figur=verwandelte_figuren["springer_schwarz"][0]
        verwandelte_figuren["springer_schwarz"][0]["command"]=lambda:zuege_springer_schwarz(figur)
        verwandelte_figuren["springer_schwarz"][0].place(x=xpos, y=ypos)
        aktuelle_figur.place_forget()
        alle_figuren.append(verwandelte_figuren["springer_schwarz"][0])
        for i in felder:
            if felder[i]["x"]==xpos and felder[i]["y"]==ypos:
                felder[i]["figure"]=verwandelte_figuren["springer_schwarz"][0]
        verwandelte_figuren["springer_schwarz"].pop(0)
    if verwandel_figur=="laeufer":
        verwandelte_figuren["laeufer_schwarz"][0]["image"]=laeufer_s_bild
        figur=verwandelte_figuren["laeufer_schwarz"][0]
        verwandelte_figuren["laeufer_schwarz"][0]["command"]=lambda:zuege_laeufer_schwarz(figur)
        verwandelte_figuren["laeufer_schwarz"][0].place(x=xpos, y=ypos)
        aktuelle_figur.place_forget()
        alle_figuren.append(verwandelte_figuren["laeufer_schwarz"][0])
        for i in felder:
            if felder[i]["x"]==xpos and felder[i]["y"]==ypos:
                felder[i]["figure"]=verwandelte_figuren["laeufer_schwarz"][0]
        verwandelte_figuren["laeufer_schwarz"].pop(0)
    
def bauer_verwandeln_weiß(aktuelle_figur, verwandel_figur, xpos, ypos):
    global felder
    global verwandelte_figuren
    if verwandel_figur=="dame":
        verwandelte_figuren["damen_weiß"][0]["image"]=dame_w_bild
        figur=verwandelte_figuren["damen_weiß"][0]
        verwandelte_figuren["damen_weiß"][0]["command"]=lambda:zuege_dame_weiß(figur)
        verwandelte_figuren["damen_weiß"][0].place(x=xpos, y=ypos)
        aktuelle_figur.place_forget()
        alle_figuren.append(verwandelte_figuren["damen_weiß"][0])
        for i in felder:
            if felder[i]["x"]==xpos and felder[i]["y"]==ypos:
                felder[i]["figure"]=verwandelte_figuren["damen_weiß"][0]
                print(felder[i]["figure"])
        verwandelte_figuren["damen_weiß"].pop(0)
    if verwandel_figur=="turm":
        verwandelte_figuren["tuerme_weiß"][0]["image"]=turm_w_bild
        figur=verwandelte_figuren["tuerme_weiß"][0]
        verwandelte_figuren["tuerme_weiß"][0]["command"]=lambda:zuege_turm_weiß(figur)
        verwandelte_figuren["tuerme_weiß"][0].place(x=xpos, y=ypos)
        aktuelle_figur.place_forget()
        alle_figuren.append(verwandelte_figuren["tuerme_weiß"][0])
        for i in felder:
            if felder[i]["x"]==xpos and felder[i]["y"]==ypos:
                felder[i]["figure"]=verwandelte_figuren["tuerme_weiß"][0]
        verwandelte_figuren["tuerme_weiß"].pop(0)
    if verwandel_figur=="springer":
        verwandelte_figuren["springer_weiß"][0]["image"]=springer_w_bild
        figur=verwandelte_figuren["springer_weiß"][0]
        verwandelte_figuren["springer_weiß"][0]["command"]=lambda:zuege_springer_weiß(figur)
        verwandelte_figuren["springer_weiß"][0].place(x=xpos, y=ypos)
        aktuelle_figur.place_forget()
        alle_figuren.append(verwandelte_figuren["springer_weiß"][0])
        for i in felder:
            if felder[i]["x"]==xpos and felder[i]["y"]==ypos:
                felder[i]["figure"]=verwandelte_figuren["springer_weiß"][0]
        verwandelte_figuren["springer_weiß"].pop(0)
    if verwandel_figur=="laeufer":
        verwandelte_figuren["laeufer_weiß"][0]["image"]=laeufer_w_bild
        figur=verwandelte_figuren["laeufer_weiß"][0]
        verwandelte_figuren["laeufer_weiß"][0]["command"]=lambda:zuege_laeufer_weiß(figur)
        verwandelte_figuren["laeufer_weiß"][0].place(x=xpos, y=ypos)
        aktuelle_figur.place_forget()
        alle_figuren.append(verwandelte_figuren["laeufer_weiß"][0])
        for i in felder:
            if felder[i]["x"]==xpos and felder[i]["y"]==ypos:
                felder[i]["figure"]=verwandelte_figuren["laeufer_weiß"][0]
        verwandelte_figuren["laeufer_weiß"].pop(0)
           
#acht Bauern weiß
bauer_w_bild=ImageTk.PhotoImage(Image.open("Bilder\Bauer_weiß.png"))
bauer1_w=Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiß(bauer1_w))
bauer1_w.farbe="weiß"
bauer1_w.art="bauer"
bauer2_w=Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiß(bauer2_w))
bauer2_w.farbe="weiß"
bauer2_w.art="bauer"
bauer3_w=Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiß(bauer3_w))
bauer3_w.farbe="weiß"
bauer3_w.art="bauer"
bauer4_w=Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiß(bauer4_w))
bauer4_w.farbe="weiß"
bauer4_w.art="bauer"
bauer5_w=Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiß(bauer5_w))
bauer5_w.farbe="weiß"
bauer5_w.art="bauer"
bauer6_w=Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiß(bauer6_w))
bauer6_w.farbe="weiß"
bauer6_w.art="bauer"
bauer7_w=Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiß(bauer7_w))
bauer7_w.farbe="weiß"
bauer7_w.art="bauer"
bauer8_w=Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiß(bauer8_w))
bauer8_w.farbe="weiß"
bauer8_w.art="bauer"

#zwei Türme weiß
turm_w_bild=ImageTk.PhotoImage(Image.open("Bilder\Turm_weiß.png"))
turm1_w=Schachfigur(rahmen, image=turm_w_bild, command=lambda:zuege_turm_weiß(turm1_w))
turm1_w.farbe="weiß"
turm1_w.art="turm"
turm2_w=Schachfigur(rahmen, image=turm_w_bild, command=lambda:zuege_turm_weiß(turm2_w))
turm2_w.farbe="weiß"
turm2_w.art="turm"

#zwei Springen weiß
springer_w_bild=ImageTk.PhotoImage(Image.open("Bilder\Springer_weiß.png"))
springer1_w=Schachfigur(rahmen, image=springer_w_bild, command=lambda:zuege_springer_weiß(springer1_w))
springer1_w.farbe="weiß"
springer1_w.art="springer"
springer2_w=Schachfigur(rahmen, image=springer_w_bild, command=lambda:zuege_springer_weiß(springer2_w))
springer2_w.farbe="weiß"
springer2_w.art="springer"

#zwei Laeufer weiß
laeufer_w_bild=ImageTk.PhotoImage(Image.open("Bilder\Läufer_weiß.png"))
laeufer1_w=Schachfigur(rahmen, image=laeufer_w_bild, command=lambda:zuege_laeufer_weiß(laeufer1_w))
laeufer1_w.farbe="weiß"
laeufer1_w.art="laeufer"
laeufer2_w=Schachfigur(rahmen, image=laeufer_w_bild, command=lambda:zuege_laeufer_weiß(laeufer2_w))
laeufer2_w.farbe="weiß"
laeufer2_w.art="laeufer"

#Koenig & Dame weiß
koenig_w_bild=ImageTk.PhotoImage(Image.open("Bilder\König_weiß.png"))
koenig_w=Schachfigur(rahmen, image=koenig_w_bild, command=lambda:zuege_koenig_weiß(koenig_w))
koenig_w.farbe="weiß"
koenig_w.art="koenig"
dame_w_bild=ImageTk.PhotoImage(Image.open("Bilder\Dame_weiß.png"))
dame_w=Schachfigur(rahmen, image=dame_w_bild, command=lambda:zuege_dame_weiß(dame_w))
dame_w.farbe="weiß"
dame_w.art="dame"


#acht Bauern schwarz
bauer_s_bild=ImageTk.PhotoImage(Image.open("Bilder\Bauer_schwarz.png"))
bauer1_s=Schachfigur(rahmen, image=bauer_s_bild, command=lambda: zuege_bauer_schwarz(bauer1_s))
bauer1_s.farbe="schwarz"
bauer1_s.art="bauer"
bauer2_s=Schachfigur(rahmen, image=bauer_s_bild, command=lambda: zuege_bauer_schwarz(bauer2_s))
bauer2_s.farbe="schwarz"
bauer2_s.art="bauer"
bauer3_s=Schachfigur(rahmen, image=bauer_s_bild, command=lambda: zuege_bauer_schwarz(bauer3_s))
bauer3_s.farbe="schwarz"
bauer3_s.art="bauer"
bauer4_s=Schachfigur(rahmen, image=bauer_s_bild, command=lambda: zuege_bauer_schwarz(bauer4_s))
bauer4_s.farbe="schwarz"
bauer4_s.art="bauer"
bauer5_s=Schachfigur(rahmen, image=bauer_s_bild, command=lambda: zuege_bauer_schwarz(bauer5_s))
bauer5_s.farbe="schwarz"
bauer5_s.art="bauer"
bauer6_s=Schachfigur(rahmen, image=bauer_s_bild, command=lambda: zuege_bauer_schwarz(bauer6_s))
bauer6_s.farbe="schwarz"
bauer6_s.art="bauer"
bauer7_s=Schachfigur(rahmen, image=bauer_s_bild, command=lambda: zuege_bauer_schwarz(bauer7_s))
bauer7_s.farbe="schwarz"
bauer7_s.art="bauer"
bauer8_s=Schachfigur(rahmen, image=bauer_s_bild, command=lambda: zuege_bauer_schwarz(bauer8_s))
bauer8_s.farbe="schwarz"
bauer8_s.art="bauer"

#zwei Türme schwarz
turm_s_bild=ImageTk.PhotoImage(Image.open("Bilder\Turm_schwarz.png"))
turm1_s=Schachfigur(rahmen, image=turm_s_bild, command=lambda:zuege_turm_schwarz(turm1_s))
turm1_s.farbe="schwarz"
turm1_s.art="turm"
turm2_s=Schachfigur(rahmen, image=turm_s_bild, command=lambda:zuege_turm_schwarz(turm2_s))
turm2_s.farbe="schwarz"
turm2_s.art="turm"

#zwei Springer schwarz
springer_s_bild=ImageTk.PhotoImage(Image.open("Bilder\Springer_schwarz.png"))
springer1_s=Schachfigur(rahmen, image=springer_s_bild, command=lambda:zuege_springer_schwarz(springer1_s))
springer1_s.farbe="schwarz"
springer1_s.art="springer"
springer2_s=Schachfigur(rahmen, image=springer_s_bild, command=lambda:zuege_springer_schwarz(springer2_s))
springer2_s.farbe="schwarz"
springer2_s.art="springer"

#zwei Laeufer schwarz
laeufer_s_bild=ImageTk.PhotoImage(Image.open("Bilder\Läufer_schwarz.png"))
laeufer1_s=Schachfigur(rahmen, image=laeufer_s_bild, command=lambda:zuege_laeufer_schwarz(laeufer1_s))
laeufer1_s.farbe="schwarz"
laeufer1_s.art="laeufer"
laeufer2_s=Schachfigur(rahmen, image=laeufer_s_bild, command=lambda:zuege_laeufer_schwarz(laeufer2_s))
laeufer2_s.farbe="schwarz"
laeufer2_s.art="laeufer"

#Koenig & Dame schwarz
koenig_s_bild=ImageTk.PhotoImage(Image.open("Bilder\König_schwarz.png"))
koenig_s=Schachfigur(rahmen, image=koenig_s_bild, command=lambda:zuege_koenig_schwarz(koenig_s))
koenig_s.farbe="schwarz"
koenig_s.art="koenig"
dame_s_bild=ImageTk.PhotoImage(Image.open("Bilder\Dame_schwarz.png"))
dame_s=Schachfigur(rahmen, image=dame_s_bild, command=lambda:zuege_dame_schwarz(dame_s))
dame_s.farbe="schwarz"
dame_s.art="dame"

def figur_ziehen(xpos, ypos):
    for i in range(0, 64, 1):
        punkte[i].place_forget()
    global felder
    global weristdran
    global rochade
    for i in felder:
        if felder[i]["figure"]==aktuelle_figur:
            felder[i]["figure"]="none"
    for i in felder:
        if felder[i]["x"]==xpos and felder[i]["y"]==ypos:
            if felder[i]["figure"]!="none":
                felder[i]["figure"].place_forget()
            felder[i]["figure"]=aktuelle_figur
            felder[i]["figure"].place(x=felder[i]["x"], y=felder[i]["y"])
    if aktuelle_figur==turm1_w:
        rochade["turm1_w_gezogen"]=True
    if aktuelle_figur==turm2_w:
        rochade["turm2_w_gezogen"]=True
    if aktuelle_figur==turm1_s:
        rochade["turm1_s_gezogen"]=True
    if aktuelle_figur==turm2_s:
        rochade["turm2_s_gezogen"]=True
    if aktuelle_figur==koenig_w:
        rochade["koenig_w_gezogen"]=True
    if aktuelle_figur==koenig_s:
        rochade["koenig_s_gezogen"]=True
    if aktuelle_figur.art=="bauer" and ypos==379:
        auswaehlfenster=Tk()
        auswaehlfenster.title("Auswählen")
        auswahlDame=Button(auswaehlfenster, image=dame_s_bild, command=lambda:bauer_verwandeln_schwarz(aktuelle_figur, "dame", xpos, ypos))
        auswahlTurm=Button(auswaehlfenster, image=turm_s_bild, command=lambda:bauer_verwandeln_schwarz(aktuelle_figur, "turm", xpos, ypos))
        auswahlLaeufer=Button(auswaehlfenster, image=laeufer_s_bild, command=lambda:bauer_verwandeln_schwarz(aktuelle_figur, "laeufer", xpos, ypos))
        auswahlSpringer=Button(auswaehlfenster, image=springer_s_bild, command=lambda:bauer_verwandeln_schwarz(aktuelle_figur, "springer", xpos, ypos))
        auswahlDame.pack()
        auswahlTurm.pack()
        auswahlLaeufer.pack()
        auswahlSpringer.pack()
        auswaehlfenster.mainloop()
    if aktuelle_figur.art=="bauer" and ypos==50:
        auswaehlfenster=Tk()
        auswaehlfenster.title("Auswählen")
        auswahlDame=Button(auswaehlfenster, image=dame_w_bild, command=lambda:bauer_verwandeln_weiß(aktuelle_figur, "dame", xpos, ypos))
        auswahlTurm=Button(auswaehlfenster, image=turm_w_bild, command=lambda:bauer_verwandeln_weiß(aktuelle_figur, "turm", xpos, ypos))
        auswahlLaeufer=Button(auswaehlfenster, image=laeufer_w_bild, command=lambda:bauer_verwandeln_weiß(aktuelle_figur, "laeufer", xpos, ypos))
        auswahlSpringer=Button(auswaehlfenster, image=springer_w_bild, command=lambda:bauer_verwandeln_weiß(aktuelle_figur, "springer", xpos, ypos))
        auswahlDame.pack()
        auswahlTurm.pack()
        auswahlLaeufer.pack()
        auswahlSpringer.pack()
        auswaehlfenster.mainloop()
    if weristdran=="schwarz":
        weristdran="weiß"
        schachWeißBerechnen()
    else:
        weristdran="schwarz"
        schachSchwarzBerechnen()

gruener_punkt_bild=ImageTk.PhotoImage(Image.open("Bilder\Gruener_Punkt.png"))
punkt1=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(50, 50))
punkt2=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(97, 50))
punkt3=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(144, 50))
punkt4=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(191, 50))
punkt5=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(238, 50))
punkt6=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(285, 50))
punkt7=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(332, 50))
punkt8=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(379, 50))
punkt9=Button(rahmen, image=gruener_punkt_bild, command=lambda:figur_ziehen(50, 97))
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
punkt_lange_rochade_weiß=Button(rahmen, image=gruener_punkt_bild, command=lambda:lange_rochade_machen_weiß())
punkt_kurze_rochade_weiß=Button(rahmen, image=gruener_punkt_bild, command=lambda:kurze_rochade_machen_weiß())
punkt_lange_rochade_schwarz=Button(rahmen, image=gruener_punkt_bild, command=lambda:lange_rochade_machen_schwarz())
punkt_kurze_rochade_schwarz=Button(rahmen, image=gruener_punkt_bild, command=lambda:kurze_rochade_machen_schwarz())

roter_punkt_bild=ImageTk.PhotoImage(Image.open("Bilder\Roter_Punkt.png"))
punkt_rot=Button(rahmen, image=roter_punkt_bild)

felder={1:{"x":50, "y":379,"figure":turm1_w},2:{"x":97, "y":379,"figure":springer1_w},3:{"x":144, "y":379,"figure":laeufer1_w },4:{"x":191, "y":379,"figure":dame_w},5:{"x":238, "y":379,"figure":koenig_w},6:{"x":285, "y":379,"figure":laeufer2_w},7:{"x":332, "y":379,"figure":springer2_w},8:{"x":379, "y":379,"figure":turm2_w},9:{"x":50, "y":332,"figure":bauer1_w},10:{"x":97, "y":332,"figure":bauer2_w},11:{"x":144, "y":332,"figure":bauer3_w},12:{"x":191, "y":332,"figure":bauer4_w},13:{"x":238, "y":332,"figure":bauer5_w},14:{"x":285, "y":332,"figure":bauer6_w},15:{"x":332, "y":332,"figure":bauer7_w},16:{"x":379, "y":332,"figure":bauer8_w},17:{"x":50, "y":285,"figure":"none"},18:{"x":97, "y":285,"figure":"none"},19:{"x":144, "y":285,"figure":"none"},20:{"x":191, "y":285,"figure":"none"},21:{"x":238, "y":285,"figure":"none"},22:{"x":285, "y":285,"figure":"none"},23:{"x":332, "y":285,"figure":"none"},24:{"x":379, "y":285,"figure":"none"},25:{"x":50, "y":238,"figure":"none"},26:{"x":97, "y":238,"figure":"none"},27:{"x":144, "y":238,"figure":"none"},28:{"x":191, "y":238,"figure":"none"},29:{"x":238, "y":238,"figure":"none"},30:{"x":285, "y":238,"figure":"none"},31:{"x":332, "y":238,"figure":"none"},32:{"x":379, "y":238,"figure":"none"},33:{"x":50, "y":191,"figure":"none"},34:{"x":97, "y":191,"figure":"none"},35:{"x":144, "y":191,"figure":"none"},36:{"x":191, "y":191,"figure":"none"},37:{"x":238, "y":191,"figure":"none"},38:{"x":285, "y":191,"figure":"none"},39:{"x":332, "y":191,"figure":"none"},40:{"x":379, "y":191,"figure":"none"},41:{"x":50, "y":144,"figure":"none"},42:{"x":97, "y":144,"figure":"none"},43:{"x":144, "y":144,"figure":"none"},44:{"x":191, "y":144,"figure":"none"},45:{"x":238, "y":144,"figure":"none"},46:{"x":285, "y":144,"figure":"none"},47:{"x":332, "y":144,"figure":"none"},48:{"x":379, "y":144,"figure":"none"},49:{"x":50, "y":97,"figure":bauer1_s},50:{"x":97, "y":97,"figure":bauer2_s},51:{"x":144, "y":97,"figure":bauer3_s},52:{"x":191, "y":97,"figure":bauer4_s},53:{"x":238, "y":97,"figure":bauer5_s},54:{"x":285, "y":97,"figure":bauer6_s},55:{"x":332, "y":97,"figure":bauer7_s},56:{"x":379, "y":97,"figure":bauer8_s},57:{"x":50, "y":50,"figure":turm1_s},58:{"x":97, "y":50,"figure":springer1_s},59:{"x":144, "y":50,"figure":laeufer1_s},60:{"x":191, "y":50,"figure":dame_s},61:{"x":238, "y":50,"figure":koenig_s},62:{"x":285, "y":50,"figure":laeufer2_s},63:{"x":332, "y":50,"figure":springer2_s},64:{"x":379, "y":50,"figure":turm2_s}}
punkte=[punkt1, punkt2, punkt3, punkt4, punkt5, punkt6, punkt7, punkt8, punkt9, punkt10, punkt11, punkt12, punkt13, punkt14, punkt15, punkt16, punkt17, punkt18, punkt19, punkt20, punkt21, punkt22, punkt23, punkt24, punkt25, punkt26, punkt27, punkt28, punkt29, punkt30, punkt31, punkt32, punkt33, punkt34, punkt35, punkt36, punkt37, punkt38, punkt39, punkt40, punkt41, punkt42, punkt43, punkt44, punkt45, punkt46, punkt47, punkt48, punkt49, punkt50, punkt51, punkt52, punkt53, punkt54, punkt55, punkt56, punkt57, punkt58, punkt59, punkt60, punkt61, punkt62, punkt63, punkt64, punkt_lange_rochade_weiß, punkt_kurze_rochade_weiß, punkt_kurze_rochade_schwarz, punkt_lange_rochade_schwarz]
alle_figuren=[bauer1_w, bauer2_w, bauer3_w, bauer4_w, bauer5_w, bauer6_w, bauer7_w, bauer8_w, turm1_w, turm2_w, springer1_w, springer2_w, laeufer1_w, laeufer2_w, koenig_w, dame_w, bauer1_s, bauer2_s, bauer3_s, bauer4_s, bauer5_s, bauer6_s, bauer7_s, bauer8_s, turm1_s, turm2_s, springer1_s, springer2_s, laeufer1_s, laeufer2_s, koenig_s, dame_s]

def figuren_plazieren():
    for i in felder:
        if felder[i]["figure"]!="none":
            felder[i]["figure"].place(x=felder[i]["x"], y=felder[i]["y"])

figuren_plazieren()
fenster.mainloop()