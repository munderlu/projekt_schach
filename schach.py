from tkinter import *
from PIL import ImageTk, Image
import copy
fenster=Tk()
fenster.title("Schach Projekt")
rahmen=Frame(fenster, relief="ridge", borderwidth=5)
rahmen.pack(fill="both", expand=1)
fenster.geometry("500x500")

feld_style=35
pixelVirtual=PhotoImage(width=1, height=1)
feld1=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(50,50))
feld2=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(97,50))
feld3=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(144,50))
feld4=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(191,50))
feld5=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(238,50))
feld6=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(285,50))
feld7=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(332,50))
feld8=Button(rahmen, bg="#8b4531", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(379,50))
feld9=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(50,97))
feld10=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(97,97))
feld11=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(144,97))
feld12=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(191,97))
feld13=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(238,97))
feld14=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(285,97))
feld15=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(332,97))
feld16=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(379,97))
feld17=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(50,144))
feld18=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(97,144))
feld19=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(144,144))
feld20=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(191,144))
feld21=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(238,144))
feld22=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(285,144))
feld23=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(332,144))
feld24=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(379,144))
feld25=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(50,191))
feld26=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(97,191))
feld27=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(144,191))
feld28=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(191,191))
feld29=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(238,191))
feld30=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(285,191))
feld31=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(332,191))
feld32=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(379,191))
feld33=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(50,238))
feld34=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(97,238))
feld35=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(144,238))
feld36=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(191,238))
feld37=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(238,238))
feld38=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(285,238))
feld39=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(332,238))
feld40=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(379,238))
feld41=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(50,285))
feld42=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(97,285))
feld43=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(144,285))
feld44=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(191,285))
feld45=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(238,285))
feld46=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(285,285))
feld47=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(332,285))
feld48=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(379,285))
feld49=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(50,332))
feld50=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(97,332))
feld51=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(144,332))
feld52=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(191,332))
feld53=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(238,332))
feld54=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(285,332))
feld55=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(332,332))
feld56=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(379,332))
feld57=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(50,379))
feld58=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(97,379))
feld59=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(144,379))
feld60=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(191,379))
feld61=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(238,379))
feld62=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(285,379))
feld63=Button(rahmen, bg="#8b4513", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(332,379))
feld64=Button(rahmen, bg="#FFFFFF", image=pixelVirtual, border=5, height=feld_style, width=feld_style, compound="center", command=lambda:figur_ziehen(379,379))
feld1.place(x=40, y=40)
feld2.place(x=40+47*1, y=40)
feld3.place(x=40+47*2, y=40)
feld4.place(x=40+47*3, y=40)
feld5.place(x=40+47*4, y=40)
feld6.place(x=40+47*5, y=40)
feld7.place(x=40+47*6, y=40)
feld8.place(x=40+47*7, y=40)
feld9.place(x=40, y=40+47)
feld10.place(x=40+47*1, y=40+47)
feld11.place(x=40+47*2, y=40+47)
feld12.place(x=40+47*3, y=40+47)
feld13.place(x=40+47*4, y=40+47)
feld14.place(x=40+47*5, y=40+47)
feld15.place(x=40+47*6, y=40+47)
feld16.place(x=40+47*7, y=40+47)
feld17.place(x=40, y=40+2*47)
feld18.place(x=40+47*1, y=40+2*47)
feld19.place(x=40+47*2, y=40+2*47)
feld20.place(x=40+47*3, y=40+2*47)
feld21.place(x=40+47*4, y=40+2*47)
feld22.place(x=40+47*5, y=40+2*47)
feld23.place(x=40+47*6, y=40+2*47)
feld24.place(x=40+47*7, y=40+2*47)
feld25.place(x=40, y=40+3*47)
feld26.place(x=40+47*1, y=40+3*47)
feld27.place(x=40+47*2, y=40+3*47)
feld28.place(x=40+47*3, y=40+3*47)
feld29.place(x=40+47*4, y=40+3*47)
feld30.place(x=40+47*5, y=40+3*47)
feld31.place(x=40+47*6, y=40+3*47)
feld32.place(x=40+47*7, y=40+3*47)
feld33.place(x=40, y=40+4*47)
feld34.place(x=40+47*1, y=40+4*47)
feld35.place(x=40+47*2, y=40+4*47)
feld36.place(x=40+47*3, y=40+4*47)
feld37.place(x=40+47*4, y=40+4*47)
feld38.place(x=40+47*5, y=40+4*47)
feld39.place(x=40+47*6, y=40+4*47)
feld40.place(x=40+47*7, y=40+4*47)
feld41.place(x=40, y=40+5*47)
feld42.place(x=40+47*1, y=40+5*47)
feld43.place(x=40+47*2, y=40+5*47)
feld44.place(x=40+47*3, y=40+5*47)
feld45.place(x=40+47*4, y=40+5*47)
feld46.place(x=40+47*5, y=40+5*47)
feld47.place(x=40+47*6, y=40+5*47)
feld48.place(x=40+47*7, y=40+5*47)
feld49.place(x=40, y=40+6*47)
feld50.place(x=40+47*1, y=40+6*47)
feld51.place(x=40+47*2, y=40+6*47)
feld52.place(x=40+47*3, y=40+6*47)
feld53.place(x=40+47*4, y=40+6*47)
feld54.place(x=40+47*5, y=40+6*47)
feld55.place(x=40+47*6, y=40+6*47)
feld56.place(x=40+47*7, y=40+6*47)
feld57.place(x=40, y=40+7*47)
feld58.place(x=40+47*1, y=40+7*47)
feld59.place(x=40+47*2, y=40+7*47)
feld60.place(x=40+47*3, y=40+7*47)
feld61.place(x=40+47*4, y=40+7*47)
feld62.place(x=40+47*5, y=40+7*47)
feld63.place(x=40+47*6, y=40+7*47)
feld64.place(x=40+47*7, y=40+7*47)

felder_buttons=[feld1, feld2, feld3, feld4, feld5, feld6, feld7, feld8, feld9, feld10, feld11, feld12, feld13, feld14, feld15, feld16, feld17, feld18, feld19, feld20, feld21, feld22, feld23, feld24, feld25, feld26, feld27, feld28, feld29, feld30, feld31, feld32, feld33, feld34, feld35, feld36, feld37, feld38, feld39, feld40, feld41, feld42, feld43, feld44, feld45, feld46, feld47, feld48, feld49, feld50, feld51, feld52, feld53, feld54, feld55, feld56, feld57, feld58, feld59, feld60, feld61, feld62, feld63, feld64]

aktuelle_figur="none"
weristdran="weiss"
aktuelle_figur="none"
schachWeiss=False
schachSchwarz=False
moegliche_zuege=[]
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
verwandelte_figuren={"damen_schwarz":[dame2_s, dame3_s, dame4_s, dame5_s, dame6_s, dame7_s, dame8_s, dame9_s], "damen_weiss":[dame2_w, dame3_w, dame4_w, dame5_w, dame6_w, dame7_w, dame8_w, dame9_w], "tuerme_schwarz":[turm3_s, turm4_s, turm5_s, turm6_s, turm7_s, turm8_s, turm9_s, turm10_s], "tuerme_weiss":[turm3_w, turm4_w, turm5_w, turm6_w, turm7_w, turm8_w, turm9_w, turm10_w], "laeufer_schwarz":[laeufer3_s, laeufer4_s, laeufer5_s, laeufer6_s, laeufer7_s, laeufer8_s, laeufer9_s, laeufer10_s], "laeufer_weiss":[laeufer3_w, laeufer4_w, laeufer5_w, laeufer6_w, laeufer7_w, laeufer8_w, laeufer9_w, laeufer10_w], "springer_schwarz":[springer3_s, springer4_s, springer5_s, springer6_s, springer7_s, springer8_s, springer9_s, springer10_s], "springer_weiss":[springer3_w, springer4_w, springer5_w, springer6_w, springer7_w, springer8_w, springer9_w, springer10_w]}
for i in verwandelte_figuren:
    for k in verwandelte_figuren[i]:
        if i=="damen_schwarz":
            k.art="dame"
            k.farbe="schwarz"
        if i=="damen_weiss":
            k.art="dame"
            k.farbe="weiss"
        if i=="tuerme_schwarz":
            k.art="turm"
            k.farbe="schwarz"
        if i=="tuerme_weiss":
            k.art="turm"
            k.farbe="weiss"
        if i=="laeufer_schwarz":
            k.art="laeufer"
            k.farbe="schwarz"
        if i=="laeufer_weiss":
            k.art="laeufer"
            k.farbe="weiss"
        if i=="springer_schwarz":
            k.art="springer"
            k.farbe="schwarz"
        if i=="springer_weiss":
            k.art="springer"
            k.farbe="weiss"

moegliche_ziele={1:{"Feld_Nr": "none", "x":"none", "y":"none"}, 2:{"Feld_Nr": "none", "x":"none", "y":"none"}, 3:{"Feld_Nr": "none", "x":"none", "y":"none"}, 4:{"Feld_Nr": "none", "x":"none", "y":"none"}, 5:{"Feld_Nr": "none", "x":"none", "y":"none"}, 6:{"Feld_Nr": "none", "x":"none", "y":"none"}, 7:{"Feld_Nr": "none", "x":"none", "y":"none"}, 8:{"Feld_Nr": "none", "x":"none", "y":"none"}, 9:{"Feld_Nr": "none", "x":"none", "y":"none"}, 10:{"Feld_Nr": "none", "x":"none", "y":"none"}, 11:{"Feld_Nr": "none", "x":"none", "y":"none"}, 12:{"Feld_Nr": "none", "x":"none", "y":"none"}, 13:{"Feld_Nr": "none", "x":"none", "y":"none"}, 14:{"Feld_Nr": "none", "x":"none", "y":"none"}, 15:{"Feld_Nr": "none", "x":"none", "y":"none"}, 16:{"Feld_Nr": "none", "x":"none", "y":"none"}, 17:{"Feld_Nr": "none", "x":"none", "y":"none"}, 18:{"Feld_Nr": "none", "x":"none", "y":"none"}, 19:{"Feld_Nr": "none", "x":"none", "y":"none"}, 20:{"Feld_Nr": "none", "x":"none", "y":"none"}, 21:{"Feld_Nr": "none", "x":"none", "y":"none"}, 22:{"Feld_Nr": "none", "x":"none", "y":"none"}, 23:{"Feld_Nr": "none", "x":"none", "y":"none"}, 24:{"Feld_Nr": "none", "x":"none", "y":"none"}, 25:{"Feld_Nr": "none", "x":"none", "y":"none"}, 26:{"Feld_Nr": "none", "x":"none", "y":"none"}, 27:{"Feld_Nr": "none", "x":"none", "y":"none"}}

def alleZuegeBerechnenWeiss(felder_kopie):
    global moegliche_zuege
    for figur in alle_figuren:
        if(figur.farbe=="weiss"):
            if(figur.art=="bauer"):
                for i in felder_kopie:
                    if felder_kopie[i]["figure"]==figur:
                        if felder_kopie[i+8]["figure"]=="none":
                            moegliche_zuege.append({"x": felder_kopie[i]["x"], "y": felder_kopie[i]["y"]-47})
                        if felder_kopie[i]["y"]==332 and felder_kopie[i+8]["figure"]=="none" and felder_kopie[i+16]["figure"]=="none":
                            moegliche_zuege.append({"x": felder_kopie[i]["x"], "y": 238})
                        if felder_kopie[i]["x"]!=379:
                            if felder_kopie[i+9]["figure"]!="none"and felder_kopie[i+9]["figure"].farbe=="schwarz":
                                moegliche_zuege.append({"x": felder_kopie[i]["x"]+47, "y": felder_kopie[i]["y"]-47})
                        if felder_kopie[i]["x"]!=50:
                            if felder_kopie[i+7]["figure"]!="none"and felder_kopie[i+7]["figure"].farbe=="schwarz":
                                moegliche_zuege.append({"x": felder_kopie[i]["x"]-47, "y": felder_kopie[i]["y"]-47})
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
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
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
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
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
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
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
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
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
                                    moegliche_zuege.append({"x": felder_kopie[j]["x"], "y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY-2*47 and felder_kopie[j]["x"]==figurX-47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="schwarz":
                                    moegliche_zuege.append({"x": felder_kopie[j]["x"], "y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY-47 and felder_kopie[j]["x"]==figurX+2*47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="schwarz":
                                    moegliche_zuege.append({"x": felder_kopie[j]["x"], "y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY+47 and felder_kopie[j]["x"]==figurX+2*47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="schwarz":
                                    moegliche_zuege.append({"x": felder_kopie[j]["x"], "y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY+2*47 and felder_kopie[j]["x"]==figurX+47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="schwarz":
                                    moegliche_zuege.append({"x": felder_kopie[j]["x"], "y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY+2*47 and felder_kopie[j]["x"]==figurX-47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="schwarz":
                                    moegliche_zuege.append({"x": felder_kopie[j]["x"], "y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY+47 and felder_kopie[j]["x"]==figurX-2*47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="schwarz":
                                    moegliche_zuege.append({"x": felder_kopie[j]["x"], "y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY-47 and felder_kopie[j]["x"]==figurX-2*47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="schwarz":
                                    moegliche_zuege.append({"x": felder_kopie[j]["x"], "y": felder_kopie[j]["y"]})
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
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
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
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
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
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
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
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
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
                                moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                zählvariable+=1
                                break
                        for k in felder_kopie:
                            if felder_kopie[k]["x"]==figurX and felder_kopie[k]["y"]==figurY+47:
                                if felder_kopie[k]["figure"]!="none":
                                    if felder_kopie[k]["figure"].farbe!="schwarz":
                                        break
                                moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                zählvariable+=1
                                break
                        for k in felder_kopie:
                            if felder_kopie[k]["x"]==figurX+47 and felder_kopie[k]["y"]==figurY:
                                if felder_kopie[k]["figure"]!="none":
                                    if felder_kopie[k]["figure"].farbe!="schwarz":
                                        break
                                moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                zählvariable+=1
                                break
                        for k in felder_kopie:
                            if felder_kopie[k]["x"]==figurX-47 and felder_kopie[k]["y"]==figurY:
                                if felder_kopie[k]["figure"]!="none":
                                    if felder_kopie[k]["figure"].farbe!="schwarz":
                                        break
                                moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                zählvariable+=1
                                break
                        for k in felder_kopie:
                            if felder_kopie[k]["x"]==figurX-47 and felder_kopie[k]["y"]==figurY-47:
                                if felder_kopie[k]["figure"]!="none":
                                    if felder_kopie[k]["figure"].farbe!="schwarz":
                                        break
                                moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                zählvariable+=1
                                break
                        for k in felder_kopie:
                            if felder_kopie[k]["x"]==figurX-47 and felder_kopie[k]["y"]==figurY+47:
                                if felder_kopie[k]["figure"]!="none":
                                    if felder_kopie[k]["figure"].farbe!="schwarz":
                                        break
                                moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                zählvariable+=1
                                break
                        for k in felder_kopie:
                            if felder_kopie[k]["x"]==figurX+47 and felder_kopie[k]["y"]==figurY-47:
                                if felder_kopie[k]["figure"]!="none":
                                    if felder_kopie[k]["figure"].farbe!="schwarz":
                                        break
                                moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                zählvariable+=1
                                break
                        for k in felder_kopie:
                            if felder_kopie[k]["x"]==figurX+47 and felder_kopie[k]["y"]==figurY+47:
                                if felder_kopie[k]["figure"]!="none":
                                    if felder_kopie[k]["figure"].farbe!="schwarz":
                                        break
                                moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
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
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
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
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
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
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
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
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
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
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
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
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
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
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
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
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break

def alleZuegeBerechnenSchwarz(felder_kopie):
    global moegliche_zuege
    for figur in alle_figuren:
        if(figur.farbe=="schwarz"):
            if(figur.art=="bauer"):
                for i in felder_kopie:
                    if felder_kopie[i]["figure"]==figur:
                        if felder_kopie[i-8]["figure"]=="none":
                            moegliche_zuege.append({"x": felder_kopie[i]["x"], "y": felder_kopie[i]["y"]+47})
                        if felder_kopie[i]["y"]==97 and felder_kopie[i-8]["figure"]=="none" and felder_kopie[i-16]["figure"]=="none":
                            moegliche_zuege.append({"x": felder_kopie[i]["x"], "y": 191})
                        if felder_kopie[i]["x"]!=50:
                            if felder_kopie[i-9]["figure"]!="none"and felder_kopie[i-9]["figure"].farbe=="weiss":
                                moegliche_zuege.append({"x": felder_kopie[i]["x"]-47, "y": felder_kopie[i]["y"]+47})
                        if felder_kopie[i]["x"]!=379:
                            if felder_kopie[i-7]["figure"]!="none"and felder_kopie[i-7]["figure"].farbe=="weiss":
                                moegliche_zuege.append({"x": felder_kopie[i]["x"]+47, "y": felder_kopie[i]["y"]+47})
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
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX and felder_kopie[k]["y"]==figurY+j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+j*47 and felder_kopie[k]["y"]==figurY:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-j*47 and felder_kopie[k]["y"]==figurY:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
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
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="weiss":
                                    moegliche_zuege.append({"x": felder_kopie[j]["x"],"y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY-2*47 and felder_kopie[j]["x"]==figurX-47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="weiss":
                                    moegliche_zuege.append({"x": felder_kopie[j]["x"],"y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY-47 and felder_kopie[j]["x"]==figurX+2*47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="weiss":
                                    moegliche_zuege.append({"x": felder_kopie[j]["x"],"y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY+47 and felder_kopie[j]["x"]==figurX+2*47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="weiss":
                                    moegliche_zuege.append({"x": felder_kopie[j]["x"],"y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY+2*47 and felder_kopie[j]["x"]==figurX+47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="weiss":
                                    moegliche_zuege.append({"x": felder_kopie[j]["x"],"y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY+2*47 and felder_kopie[j]["x"]==figurX-47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="weiss":
                                    moegliche_zuege.append({"x": felder_kopie[j]["x"],"y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY+47 and felder_kopie[j]["x"]==figurX-2*47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="weiss":
                                    moegliche_zuege.append({"x": felder_kopie[j]["x"],"y": felder_kopie[j]["y"]})
                            if felder_kopie[j]["y"]==figurY-47 and felder_kopie[j]["x"]==figurX-2*47:
                                if felder_kopie[j]["figure"]=="none"or felder_kopie[j]["figure"].farbe=="weiss":
                                    moegliche_zuege.append({"x": felder_kopie[j]["x"],"y": felder_kopie[j]["y"]})
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
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-j*47 and felder_kopie[k]["y"]==figurY+j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+j*47 and felder_kopie[k]["y"]==figurY-j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+j*47 and felder_kopie[k]["y"]==figurY+j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"], "y": felder_kopie[k]["y"]})
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
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX and felder_kopie[k]["y"]==figurY+47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+47 and felder_kopie[k]["y"]==figurY:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-47 and felder_kopie[k]["y"]==figurY:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-47 and felder_kopie[k]["y"]==figurY-47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-47 and felder_kopie[k]["y"]==figurY+47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+47 and felder_kopie[k]["y"]==figurY-47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+47 and felder_kopie[k]["y"]==figurY+47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
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
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX and felder_kopie[k]["y"]==figurY+j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+j*47 and felder_kopie[k]["y"]==figurY:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-j*47 and felder_kopie[k]["y"]==figurY:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-j*47 and felder_kopie[k]["y"]==figurY-j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX-j*47 and felder_kopie[k]["y"]==figurY+j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+j*47 and felder_kopie[k]["y"]==figurY-j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break
                        for j in range (1, 8):
                            for k in felder_kopie:
                                if felder_kopie[k]["x"]==figurX+j*47 and felder_kopie[k]["y"]==figurY+j*47:
                                    if felder_kopie[k]["figure"]!="none":
                                        if felder_kopie[k]["figure"].farbe!="weiss":
                                            break
                                    moegliche_zuege.append({"x": felder_kopie[k]["x"],"y": felder_kopie[k]["y"]})
                                    zählvariable+=1
                                    break
                            if felder_kopie[k]["figure"]!="none":
                                break

def schachWeisseFigurBerechnen(felder_kopie):
    global schachWeiss
    global moegliche_zuege
    schachWeiss=False
    moegliche_zuege=[]
    alleZuegeBerechnenSchwarz(felder_kopie)
    for figur in alle_figuren:
        if figur.farbe=="weiss" and figur.art=="koenig":
            for i in felder_kopie:
                if felder_kopie[i]["figure"]==figur:
                    XKönig=felder_kopie[i]["x"]
                    YKönig=felder_kopie[i]["y"]
    for i in moegliche_zuege:
        if i["x"]==XKönig and i["y"]==YKönig:
            schachWeiss=True

def schachSchwarzFigurBerechnen(felder_kopie):
    global schachSchwarz
    global moegliche_zuege
    schachSchwarz=False
    moegliche_zuege=[]
    alleZuegeBerechnenWeiss(felder_kopie)
    for figur in alle_figuren:
        if figur.farbe=="schwarz" and figur.art=="koenig":
            for i in felder_kopie:
                if felder_kopie[i]["figure"]==figur:
                    XKönig=felder_kopie[i]["x"]
                    YKönig=felder_kopie[i]["y"]
    for i in moegliche_zuege:
        if i["x"]==XKönig and i["y"]==YKönig:
            schachSchwarz=True

def schachWeissBerechnen():
    setzeZieleAufNull()
    NeuesSchachWeiß=False
    schachWeiss=False
    global moegliche_zuege
    schachMatt=True
    alleZuegeBerechnenSchwarz(felder)
    for figur in alle_figuren:
        if figur.farbe=="weiss" and figur.art=="koenig":
            for i in felder:
                if felder[i]["figure"]==figur:
                    XKönig=felder[i]["x"]
                    YKönig=felder[i]["y"]
    for i in moegliche_zuege:
        if i["x"]==XKönig and i["y"]==YKönig:
            NeuesSchachWeiss=True
            rechenvariable1=XKönig
            rechenvariable2=YKönig
            rechenvariable3=(rechenvariable1-3)/47
            rechenvariable4=(rechenvariable2-3)/47
            ergebniss=(rechenvariable3+((rechenvariable4-1)*8)-1)
            feld_Nr=int(ergebniss)
            felder_buttons[feld_Nr]["bg"]="#FF0000"
            print("Schach Weiß")
    for figur in alle_figuren:
        if figur.farbe=="weiss":
            if figur.art=="bauer":
                zuege_bauer_weiss(figur)
                for i in moegliche_ziele:
                    if moegliche_ziele[i]["x"]!="none":
                        schachMatt=False
                        break
            if figur.art=="turm":
                zuege_turm_weiss(figur)
                for i in moegliche_ziele:
                    if moegliche_ziele[i]["x"]!="none":
                        schachMatt=False
                        break
            if figur.art=="laeufer":
                zuege_laeufer_weiss(figur)
                for i in moegliche_ziele:
                    if moegliche_ziele[i]["x"]!="none":
                        schachMatt=False
                        break
            if figur.art=="dame":
                zuege_dame_weiss(figur)
                for i in moegliche_ziele:
                    if moegliche_ziele[i]["x"]!="none":
                        schachMatt=False
                        break
            if figur.art=="koenig":
                zuege_koenig_weiss(figur)
                for i in moegliche_ziele:
                    if moegliche_ziele[i]["x"]!="none":
                        schachMatt=False
                        break
            if figur.art=="springer":
                zuege_springer_weiss(figur)
                for i in moegliche_ziele:
                    if moegliche_ziele[i]["x"]!="none":
                        schachMatt=False
                        break
    setzeZieleAufNull()
    if schachMatt==True and NeuesSchachWeiss==False:
        schrift=Label(text="Patt:\nunentschieden", font="Arial, 30")
        schrift.place(x=100, y=200)
    elif schachMatt==True and NeuesSchachWeiss==True:
        schrift=Label(text="Schach Matt:\nschwarz gewinnt", font="Arial, 30")
        schrift.place(x=100, y=200)

def schachSchwarzBerechnen():
    setzeZieleAufNull()
    NeuesSchachSchwarz=False
    global moegliche_zuege
    schachMatt=True
    alleZuegeBerechnenWeiss(felder)
    for figur in alle_figuren:
        if figur.farbe=="schwarz" and figur.art=="koenig":
            for i in felder:
                if felder[i]["figure"]==figur:
                    XKönig=felder[i]["x"]
                    YKönig=felder[i]["y"]
    for i in moegliche_zuege:
        if i["x"]==XKönig and i["y"]==YKönig:
            NeuesSchachSchwarz=True
            rechenvariable1=XKönig
            rechenvariable2=YKönig
            rechenvariable3=(rechenvariable1-3)/47
            rechenvariable4=(rechenvariable2-3)/47
            ergebniss=(rechenvariable3+((rechenvariable4-1)*8)-1)
            feld_Nr=int(ergebniss)
            felder_buttons[feld_Nr]["bg"]="#FF0000"
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
    setzeZieleAufNull()
    if schachMatt==True and NeuesSchachSchwarz==False:
        schrift=Label(text="Patt:\nunentschieden", font="Arial, 30")
        schrift.place(x=100, y=200)
    elif schachMatt==True and NeuesSchachSchwarz==True:
        schrift=Label(text="Schach Matt:\nweiss gewinnt", font="Arial, 30")
        schrift.place(x=100, y=200)

def setzeZieleAufNull():
    global moegliche_ziele
    moegliche_ziele={1:{"Feld_Nr": "none", "x":"none", "y":"none"}, 2:{"Feld_Nr": "none", "x":"none", "y":"none"}, 3:{"Feld_Nr": "none", "x":"none", "y":"none"}, 4:{"Feld_Nr": "none", "x":"none", "y":"none"}, 5:{"Feld_Nr": "none", "x":"none", "y":"none"}, 6:{"Feld_Nr": "none", "x":"none", "y":"none"}, 7:{"Feld_Nr": "none", "x":"none", "y":"none"}, 8:{"Feld_Nr": "none", "x":"none", "y":"none"}, 9:{"Feld_Nr": "none", "x":"none", "y":"none"}, 10:{"Feld_Nr": "none", "x":"none", "y":"none"}, 11:{"Feld_Nr": "none", "x":"none", "y":"none"}, 12:{"Feld_Nr": "none", "x":"none", "y":"none"}, 13:{"Feld_Nr": "none", "x":"none", "y":"none"}, 14:{"Feld_Nr": "none", "x":"none", "y":"none"}, 15:{"Feld_Nr": "none", "x":"none", "y":"none"}, 16:{"Feld_Nr": "none", "x":"none", "y":"none"}, 17:{"Feld_Nr": "none", "x":"none", "y":"none"}, 18:{"Feld_Nr": "none", "x":"none", "y":"none"}, 19:{"Feld_Nr": "none", "x":"none", "y":"none"}, 20:{"Feld_Nr": "none", "x":"none", "y":"none"}, 21:{"Feld_Nr": "none", "x":"none", "y":"none"}, 22:{"Feld_Nr": "none", "x":"none", "y":"none"}, 23:{"Feld_Nr": "none", "x":"none", "y":"none"}, 24:{"Feld_Nr": "none", "x":"none", "y":"none"}, 25:{"Feld_Nr": "none", "x":"none", "y":"none"}, 26:{"Feld_Nr": "none", "x":"none", "y":"none"}, 27:{"Feld_Nr": "none", "x":"none", "y":"none"}}
    aktuelle_figur="none"
    feld4["command"]=lambda:figur_ziehen(191,50)
    feld7["command"]=lambda:figur_ziehen(332,50)
    feld59["command"]=lambda:figur_ziehen(144,379)
    feld63["command"]=lambda:figur_ziehen(332,379)
 
def farbenZurücksetzen():
    for something in range(0, 49, 16):
        for i in range(0, 7, 2):
            if felder_buttons[i+something]["bg"]!="#FF0000":
                felder_buttons[i+something]["bg"]="#FFFFFF"
        for i in range(1, 8, 2):
            if felder_buttons[i+something]["bg"]!="#FF0000":
                felder_buttons[i+something]["bg"]="#8b4513"
        for i in range(0, 7, 2):
            if felder_buttons[i+something]["bg"]!="#FF0000":
                felder_buttons[i+something+8]["bg"]="#8b4513"
        for i in range(1, 8, 2):
            if felder_buttons[i+something]["bg"]!="#FF0000":
                felder_buttons[i+something+8]["bg"]="#FFFFFF"

def kopie_ausgeben(felder):
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
            moegliche_ziele[i]["Feld_Nr"]=int(ergebniss)

def punkte_plazieren():
    for i in moegliche_ziele:
        print(felder_buttons[moegliche_ziele[i]["Feld_Nr"]]["bg"])
        if moegliche_ziele[i]["Feld_Nr"]!="none" and felder_buttons[moegliche_ziele[i]["Feld_Nr"]]["bg"]!="#FF0000":
            felder_buttons[moegliche_ziele[i]["Feld_Nr"]]["bg"]="#00FF00"

def zuege_bauer_weiss(figur):
    setzeZieleAufNull()
    farbenZurücksetzen()
    global weristdran
    global en_passant
    if weristdran=="weiss":
        for i in felder:
            if felder[i]["figure"]==figur:
                global aktuelle_figur
                aktuelle_figur=figur
                if felder[i+8]["figure"]=="none":
                    felder_kopie=kopie_ausgeben(felder)
                    felder_kopie[i]["figure"]="none"
                    felder_kopie[i+8]["figure"]=figur
                    schachWeisseFigurBerechnen(felder_kopie)
                    if schachWeiss==False:
                        moegliche_ziele[1]["x"]=felder[i]["x"]
                        moegliche_ziele[1]["y"]=felder[i]["y"]-47
                if felder[i]["y"]==332 and felder[i+8]["figure"]=="none" and felder[i+16]["figure"]=="none":
                    felder_kopie=kopie_ausgeben(felder)
                    felder_kopie[i]["figure"]="none"
                    felder_kopie[i+16]["figure"]=figur
                    schachWeisseFigurBerechnen(felder_kopie)
                    if schachWeiss==False:
                        moegliche_ziele[2]["x"]=felder[i]["x"]
                        moegliche_ziele[2]["y"]=238
                if felder[i]["x"]!=379:
                    if felder[i+9]["figure"]!="none"and felder[i+9]["figure"].farbe=="schwarz":
                        felder_kopie=kopie_ausgeben(felder)
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[i+9]["figure"]=figur
                        schachWeisseFigurBerechnen(felder_kopie)
                        if schachWeiss==False:
                            moegliche_ziele[3]["x"]=felder[i]["x"]+47
                            moegliche_ziele[3]["y"]=felder[i]["y"]-47
                if felder[i]["x"]!=50:
                    if felder[i+7]["figure"]!="none"and felder[i+7]["figure"].farbe=="schwarz":
                        felder_kopie=kopie_ausgeben(felder)
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[i+7]["figure"]=figur
                        schachWeisseFigurBerechnen(felder_kopie)
                        if schachWeiss==False:
                            moegliche_ziele[4]["x"]=felder[i]["x"]-47
                            moegliche_ziele[4]["y"]=felder[i]["y"]-47
                if felder[i]["x"]!=379 and felder[i+1]["figure"]!="none":
                    if felder[i+1]["figure"].art=="bauer" and felder[i+1]["figure"].farbe=="schwarz":
                        if en_passant[felder[i+1]["figure"]]==True:
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[i+9]["figure"]=figur
                            felder_kopie[i+1]["figure"]="none"
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
                                moegliche_ziele[5]["x"]=felder[i]["x"]+47
                                moegliche_ziele[5]["y"]=felder[i]["y"]-47
                if felder[i]["x"]!=50 and felder[i-1]["figure"]!="none":
                    if felder[i-1]["figure"].art=="bauer" and felder[i-1]["figure"].farbe=="schwarz":
                        if en_passant[felder[i-1]["figure"]]==True:
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[i+7]["figure"]=figur
                            felder_kopie[i-1]["figure"]="none"
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
                                moegliche_ziele[6]["x"]=felder[i]["x"]-47
                                moegliche_ziele[6]["y"]=felder[i]["y"]-47
        punkte_auswählen()
        punkte_plazieren()

def zuege_bauer_schwarz(figur):
    setzeZieleAufNull()
    farbenZurücksetzen()
    global weristdran
    global en_passant
    if weristdran=="schwarz":
        for i in felder:
            if felder[i]["figure"]==figur:
                global aktuelle_figur
                aktuelle_figur=figur
                if felder[i-8]["figure"]=="none":
                    felder_kopie=kopie_ausgeben(felder)
                    felder_kopie[i]["figure"]="none"
                    felder_kopie[i-8]["figure"]=figur
                    schachSchwarzFigurBerechnen(felder_kopie)
                    if schachSchwarz==False:
                        moegliche_ziele[1]["x"]=felder[i]["x"]
                        moegliche_ziele[1]["y"]=felder[i]["y"]+47
                if felder[i]["y"]==97 and felder[i-8]["figure"]=="none" and felder[i-16]["figure"]=="none":
                    felder_kopie=kopie_ausgeben(felder)
                    felder_kopie[i]["figure"]="none"
                    felder_kopie[i-16]["figure"]=figur
                    schachSchwarzFigurBerechnen(felder_kopie)
                    if schachSchwarz==False:
                        moegliche_ziele[2]["x"]=felder[i]["x"]
                        moegliche_ziele[2]["y"]=191
                if felder[i]["x"]!=50:
                    if felder[i-9]["figure"]!="none"and felder[i-9]["figure"].farbe=="weiss":
                        felder_kopie=kopie_ausgeben(felder)
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[i-9]["figure"]=figur
                        schachSchwarzFigurBerechnen(felder_kopie)
                        if schachSchwarz==False:
                            moegliche_ziele[3]["x"]=felder[i]["x"]-47
                            moegliche_ziele[3]["y"]=felder[i]["y"]+47
                if felder[i]["x"]!=379:
                    if felder[i-7]["figure"]!="none"and felder[i-7]["figure"].farbe=="weiss":
                        felder_kopie=kopie_ausgeben(felder)
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[i-7]["figure"]=figur
                        schachSchwarzFigurBerechnen(felder_kopie)
                        if schachSchwarz==False:
                            moegliche_ziele[4]["x"]=felder[i]["x"]+47
                            moegliche_ziele[4]["y"]=felder[i]["y"]+47
                if felder[i]["x"]!=50 and felder[i-1]["figure"]!="none":
                    if felder[i-1]["figure"].art=="bauer" and felder[i-1]["figure"].farbe=="weiss":
                        if en_passant[felder[i-1]["figure"]]==True:
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[i-9]["figure"]=figur
                            felder_kopie[i-1]["figure"]="none"
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[5]["x"]=felder[i]["x"]-47
                                moegliche_ziele[5]["y"]=felder[i]["y"]+47
                if felder[i]["x"]!=50 and felder[i+1]["figure"]!="none":
                    if felder[i+1]["figure"].art=="bauer" and felder[i+1]["figure"].farbe=="weiss":
                        if en_passant[felder[i+1]["figure"]]==True:
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[i-7]["figure"]=figur
                            felder_kopie[i+1]["figure"]="none"
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[6]["x"]=felder[i]["x"]+47
                                moegliche_ziele[6]["y"]=felder[i]["y"]+47
        punkte_auswählen()
        punkte_plazieren() 

def zuege_turm_weiss(figur):
    global weristdran
    if weristdran=="weiss":
        setzeZieleAufNull()
        farbenZurücksetzen()
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
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
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
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
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
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
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
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
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
        farbenZurücksetzen()
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
                                if felder[k]["figure"].farbe!="weiss":
                                    break
                            felder_kopie=kopie_ausgeben(felder)
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
                                if felder[k]["figure"].farbe!="weiss":
                                    break
                            felder_kopie=kopie_ausgeben(felder)
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
                                if felder[k]["figure"].farbe!="weiss":
                                    break
                            felder_kopie=kopie_ausgeben(felder)
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
                                if felder[k]["figure"].farbe!="weiss":
                                    break
                            felder_kopie=kopie_ausgeben(felder)
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

def zuege_springer_weiss(figur):
    setzeZieleAufNull()
    farbenZurücksetzen()
    global weristdran
    if weristdran=="weiss":
        for i in felder:
            if felder[i]["figure"]==figur:
                global aktuelle_figur
                aktuelle_figur=figur
                figurX=felder[i]["x"]
                figurY=felder[i]["y"]
                for j in felder:
                    if felder[j]["y"]==figurY-2*47 and felder[j]["x"]==figurX+47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
                                moegliche_ziele[1]["x"]=felder[j]["x"]
                                moegliche_ziele[1]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY-2*47 and felder[j]["x"]==figurX-47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
                                moegliche_ziele[2]["x"]=felder[j]["x"]
                                moegliche_ziele[2]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY-47 and felder[j]["x"]==figurX+2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
                                moegliche_ziele[3]["x"]=felder[j]["x"]
                                moegliche_ziele[3]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+47 and felder[j]["x"]==figurX+2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
                                moegliche_ziele[4]["x"]=felder[j]["x"]
                                moegliche_ziele[4]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+2*47 and felder[j]["x"]==figurX+47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
                                moegliche_ziele[5]["x"]=felder[j]["x"]
                                moegliche_ziele[5]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+2*47 and felder[j]["x"]==figurX-47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
                                moegliche_ziele[6]["x"]=felder[j]["x"]
                                moegliche_ziele[6]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+47 and felder[j]["x"]==figurX-2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
                                moegliche_ziele[7]["x"]=felder[j]["x"]
                                moegliche_ziele[7]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY-47 and felder[j]["x"]==figurX-2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="schwarz":
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
                                moegliche_ziele[8]["x"]=felder[j]["x"]
                                moegliche_ziele[8]["y"]=felder[j]["y"]
            punkte_auswählen()
            punkte_plazieren()

def zuege_springer_schwarz(figur):
    setzeZieleAufNull()
    farbenZurücksetzen()
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
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiss":
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[1]["x"]=felder[j]["x"]
                                moegliche_ziele[1]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY-2*47 and felder[j]["x"]==figurX-47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiss":
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[2]["x"]=felder[j]["x"]
                                moegliche_ziele[2]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY-47 and felder[j]["x"]==figurX+2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiss":
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[3]["x"]=felder[j]["x"]
                                moegliche_ziele[3]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+47 and felder[j]["x"]==figurX+2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiss":
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[4]["x"]=felder[j]["x"]
                                moegliche_ziele[4]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+2*47 and felder[j]["x"]==figurX+47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiss":
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[5]["x"]=felder[j]["x"]
                                moegliche_ziele[5]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+2*47 and felder[j]["x"]==figurX-47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiss":
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[6]["x"]=felder[j]["x"]
                                moegliche_ziele[6]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY+47 and felder[j]["x"]==figurX-2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiss":
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[7]["x"]=felder[j]["x"]
                                moegliche_ziele[7]["y"]=felder[j]["y"]
                    if felder[j]["y"]==figurY-47 and felder[j]["x"]==figurX-2*47:
                        if felder[j]["figure"]=="none"or felder[j]["figure"].farbe=="weiss":
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[j]["figure"]=figur
                            schachSchwarzFigurBerechnen(felder_kopie)
                            if schachSchwarz==False:
                                moegliche_ziele[8]["x"]=felder[j]["x"]
                                moegliche_ziele[8]["y"]=felder[j]["y"]
            punkte_auswählen()
            punkte_plazieren()

def zuege_laeufer_weiss(figur):
    global weristdran
    if weristdran=="weiss":
        setzeZieleAufNull()
        farbenZurücksetzen()
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
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
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
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
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
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
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
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
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
        farbenZurücksetzen()
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
                                if felder[k]["figure"].farbe!="weiss":
                                    break
                            felder_kopie=kopie_ausgeben(felder)
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
                                if felder[k]["figure"].farbe!="weiss":
                                    break
                            felder_kopie=kopie_ausgeben(felder)
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
                                if felder[k]["figure"].farbe!="weiss":
                                    break
                            felder_kopie=kopie_ausgeben(felder)
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
                                if felder[k]["figure"].farbe!="weiss":
                                    break
                            felder_kopie=kopie_ausgeben(felder)
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

def zuege_koenig_weiss(figur):
    global weristdran
    if weristdran=="weiss":
        setzeZieleAufNull()
        farbenZurücksetzen()
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
                        felder_kopie=kopie_ausgeben(felder)
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachWeisseFigurBerechnen(felder_kopie)
                        if schachWeiss==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX and felder[k]["y"]==figurY+47:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="schwarz":
                                break
                        felder_kopie=kopie_ausgeben(felder)
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachWeisseFigurBerechnen(felder_kopie)
                        if schachWeiss==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX+47 and felder[k]["y"]==figurY:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="schwarz":
                                break
                        felder_kopie=kopie_ausgeben(felder)
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachWeisseFigurBerechnen(felder_kopie)
                        if schachWeiss==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX-47 and felder[k]["y"]==figurY:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="schwarz":
                                break
                        felder_kopie=kopie_ausgeben(felder)
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachWeisseFigurBerechnen(felder_kopie)
                        if schachWeiss==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX-47 and felder[k]["y"]==figurY-47:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="schwarz":
                                break
                        felder_kopie=kopie_ausgeben(felder)
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachWeisseFigurBerechnen(felder_kopie)
                        if schachWeiss==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX-47 and felder[k]["y"]==figurY+47:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="schwarz":
                                break
                        felder_kopie=kopie_ausgeben(felder)
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachWeisseFigurBerechnen(felder_kopie)
                        if schachWeiss==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX+47 and felder[k]["y"]==figurY-47:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="schwarz":
                                break
                        felder_kopie=kopie_ausgeben(felder)
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachWeisseFigurBerechnen(felder_kopie)
                        if schachWeiss==False:
                            moegliche_ziele[zählvariable]["x"]=felder[k]["x"]
                            moegliche_ziele[zählvariable]["y"]=felder[k]["y"]
                        zählvariable+=1
                        break
                for k in felder:
                    if felder[k]["x"]==figurX+47 and felder[k]["y"]==figurY+47:
                        if felder[k]["figure"]!="none":
                            if felder[k]["figure"].farbe!="schwarz":
                                break
                        felder_kopie=kopie_ausgeben(felder)
                        felder_kopie[i]["figure"]="none"
                        felder_kopie[k]["figure"]=figur
                        schachWeisseFigurBerechnen(felder_kopie)
                        if schachWeiss==False:
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
                    schachWeisseFigurBerechnen(felder)
                    if schachWeiss==True:
                        rochadeGehtNicht=True
                    felder_kopie=kopie_ausgeben(felder)
                    felder_kopie[5]["figure"]="none"
                    felder_kopie[4]["figure"]=koenig_w
                    schachWeisseFigurBerechnen(felder_kopie)
                    if schachWeiss==True:
                        rochadeGehtNicht=True
                    felder_kopie[4]["figure"]="none"
                    felder_kopie[3]["figure"]=koenig_w
                    schachWeisseFigurBerechnen(felder_kopie)
                    if schachWeiss==True:
                        rochadeGehtNicht=True
                    if rochadeGehtNicht==False:
                        felder_buttons[58]["bg"]="#00FF00"
                        felder_buttons[58]["command"]=lambda:lange_rochade_machen_weiss()
                        moegliche_ziele[9]["x"]=144
                        moegliche_ziele[9]["y"]=379
                        moegliche_ziele[9]["Feld_Nr"]=59
                if rochade["koenig_w_gezogen"]==False and rochade["turm2_w_gezogen"]==False:
                    rochadeGehtNicht=False
                    if felder[7]["figure"]!="none":
                        rochadeGehtNicht=True
                    if felder[6]["figure"]!="none":
                        rochadeGehtNicht=True
                    schachWeisseFigurBerechnen(felder)
                    if schachWeiss==True:
                        rochadeGehtNicht=True
                    felder_kopie=kopie_ausgeben(felder)
                    felder_kopie[5]["figure"]="none"
                    felder_kopie[6]["figure"]=koenig_w
                    schachWeisseFigurBerechnen(felder_kopie)
                    if schachWeiss==True:
                        rochadeGehtNicht=True
                    felder_kopie[6]["figure"]="none"
                    felder_kopie[7]["figure"]=koenig_w
                    schachWeisseFigurBerechnen(felder_kopie)
                    if schachWeiss==True:
                        rochadeGehtNicht=True
                    if rochadeGehtNicht==False:
                        felder_buttons[62]["bg"]="#00FF00"
                        felder_buttons[62]["command"]=lambda:kurze_rochade_machen_weiss()
                        moegliche_ziele[10]["x"]=332
                        moegliche_ziele[10]["y"]=379
                        moegliche_ziele[10]["Feld_Nr"]=63
        punkte_auswählen()
        punkte_plazieren()

def zuege_koenig_schwarz(figur):
    global weristdran
    if weristdran=="schwarz":
        setzeZieleAufNull()
        farbenZurücksetzen()
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
                            if felder[k]["figure"].farbe!="weiss":
                                break
                        felder_kopie=kopie_ausgeben(felder)
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
                            if felder[k]["figure"].farbe!="weiss":
                                break
                        felder_kopie=kopie_ausgeben(felder)
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
                            if felder[k]["figure"].farbe!="weiss":
                                break
                        felder_kopie=kopie_ausgeben(felder)
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
                            if felder[k]["figure"].farbe!="weiss":
                                break
                        felder_kopie=kopie_ausgeben(felder)
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
                            if felder[k]["figure"].farbe!="weiss":
                                break
                        felder_kopie=kopie_ausgeben(felder)
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
                            if felder[k]["figure"].farbe!="weiss":
                                break
                        felder_kopie=kopie_ausgeben(felder)
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
                            if felder[k]["figure"].farbe!="weiss":
                                break
                        felder_kopie=kopie_ausgeben(felder)
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
                            if felder[k]["figure"].farbe!="weiss":
                                break
                        felder_kopie=kopie_ausgeben(felder)
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
                    felder_kopie=kopie_ausgeben(felder)
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
                        felder_buttons[3]["bg"]="#00FF00"
                        felder_buttons[3]["command"]=lambda:lange_rochade_machen_schwarz()
                        moegliche_ziele[9]["x"]=144
                        moegliche_ziele[9]["y"]=50
                        moegliche_ziele[9]["Feld_Nr"]=3
                if rochade["koenig_s_gezogen"]==False and rochade["turm2_s_gezogen"]==False:
                    rochadeGehtNicht=False
                    if felder[63]["figure"]!="none":
                        rochadeGehtNicht=True
                    if felder[62]["figure"]!="none":
                        rochadeGehtNicht=True
                    schachSchwarzFigurBerechnen(felder)
                    if schachSchwarz==True:
                        rochadeGehtNicht=True
                    felder_kopie=kopie_ausgeben(felder)
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
                        felder_buttons[6]["bg"]="#00FF00"
                        felder_buttons[6]["command"]=lambda:kurze_rochade_machen_schwarz()
                        moegliche_ziele[10]["x"]=332
                        moegliche_ziele[10]["y"]=50
                        moegliche_ziele[10]["Feld_Nr"]=7
        punkte_auswählen()
        punkte_plazieren()

def zuege_dame_weiss(figur):
    global weristdran
    if weristdran=="weiss":
        setzeZieleAufNull()
        farbenZurücksetzen()
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
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
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
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
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
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
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
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
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
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
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
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
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
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
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
                            felder_kopie=kopie_ausgeben(felder)
                            felder_kopie[i]["figure"]="none"
                            felder_kopie[k]["figure"]=figur
                            schachWeisseFigurBerechnen(felder_kopie)
                            if schachWeiss==False:
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
        farbenZurücksetzen()
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
                                if felder[k]["figure"].farbe!="weiss":
                                    break
                            felder_kopie=kopie_ausgeben(felder)
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
                                if felder[k]["figure"].farbe!="weiss":
                                    break
                            felder_kopie=kopie_ausgeben(felder)
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
                                if felder[k]["figure"].farbe!="weiss":
                                    break
                            felder_kopie=kopie_ausgeben(felder)
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
                                if felder[k]["figure"].farbe!="weiss":
                                    break
                            felder_kopie=kopie_ausgeben(felder)
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
                                if felder[k]["figure"].farbe!="weiss":
                                    break
                            felder_kopie=kopie_ausgeben(felder)
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
                                if felder[k]["figure"].farbe!="weiss":
                                    break
                            felder_kopie=kopie_ausgeben(felder)
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
                                if felder[k]["figure"].farbe!="weiss":
                                    break
                            felder_kopie=kopie_ausgeben(felder)
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
                                if felder[k]["figure"].farbe!="weiss":
                                    break
                            felder_kopie=kopie_ausgeben(felder)
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

def lange_rochade_machen_weiss():
    global felder
    global weristdran
    weristdran="schwarz"
    felder[5]["figure"]="none"
    felder[4]["figure"]=turm1_w
    felder[1]["figure"]="none"
    felder[3]["figure"]=koenig_w
    rochade["koenig_w_gezogen"]=True
    figuren_plazieren()
    setzeZieleAufNull()
    farbenZurücksetzen()

def kurze_rochade_machen_weiss():
    global felder
    global weristdran
    weristdran="schwarz"
    felder[5]["figure"]="none"
    felder[6]["figure"]=turm2_w
    felder[8]["figure"]="none"
    felder[7]["figure"]=koenig_w
    rochade["koenig_w_gezogen"]=True
    figuren_plazieren()
    setzeZieleAufNull()
    farbenZurücksetzen()

def lange_rochade_machen_schwarz():
    global felder
    global weristdran
    weristdran="weiss"
    felder[61]["figure"]="none"
    felder[60]["figure"]=turm1_s
    felder[57]["figure"]="none"
    felder[59]["figure"]=koenig_s
    rochade["koenig_s_gezogen"]=True
    figuren_plazieren()
    setzeZieleAufNull()
    farbenZurücksetzen()

def kurze_rochade_machen_schwarz():
    global felder
    global weristdran
    weristdran="weiss"
    felder[61]["figure"]="none"
    felder[62]["figure"]=turm2_s
    felder[64]["figure"]="none"
    felder[63]["figure"]=koenig_s
    rochade["koenig_s_gezogen"]=True
    figuren_plazieren()
    setzeZieleAufNull()
    farbenZurücksetzen()

def bauer_verwandeln_schwarz(aktuelle_figur, verwandel_figur, xpos, ypos):
    global felder
    global verwandelte_figuren
    global weristdran
    global auswahlDame
    global auswahlLaeufer
    global auswahlSpringer
    global auswahlTurm
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
    weristdran="weiss"
    schachWeissBerechnen()
    auswahlDame.place_forget()
    auswahlTurm.place_forget()
    auswahlLaeufer.place_forget()
    auswahlSpringer.place_forget()
    
def bauer_verwandeln_weiss(aktuelle_figur, verwandel_figur, xpos, ypos):
    global felder
    global verwandelte_figuren
    global weristdran
    global auswahlDame
    global auswahlLaeufer
    global auswahlSpringer
    global auswahlTurm
    if verwandel_figur=="dame":
        verwandelte_figuren["damen_weiss"][0]["image"]=dame_w_bild
        figur=verwandelte_figuren["damen_weiss"][0]
        verwandelte_figuren["damen_weiss"][0]["command"]=lambda:zuege_dame_weiss(figur)
        verwandelte_figuren["damen_weiss"][0].place(x=xpos, y=ypos)
        aktuelle_figur.place_forget()
        alle_figuren.append(verwandelte_figuren["damen_weiss"][0])
        for i in felder:
            if felder[i]["x"]==xpos and felder[i]["y"]==ypos:
                felder[i]["figure"]=verwandelte_figuren["damen_weiss"][0]
        verwandelte_figuren["damen_weiss"].pop(0)
    if verwandel_figur=="turm":
        verwandelte_figuren["tuerme_weiss"][0]["image"]=turm_w_bild
        figur=verwandelte_figuren["tuerme_weiss"][0]
        verwandelte_figuren["tuerme_weiss"][0]["command"]=lambda:zuege_turm_weiss(figur)
        verwandelte_figuren["tuerme_weiss"][0].place(x=xpos, y=ypos)
        aktuelle_figur.place_forget()
        alle_figuren.append(verwandelte_figuren["tuerme_weiss"][0])
        for i in felder:
            if felder[i]["x"]==xpos and felder[i]["y"]==ypos:
                felder[i]["figure"]=verwandelte_figuren["tuerme_weiss"][0]
        verwandelte_figuren["tuerme_weiss"].pop(0)
    if verwandel_figur=="springer":
        verwandelte_figuren["springer_weiss"][0]["image"]=springer_w_bild
        figur=verwandelte_figuren["springer_weiss"][0]
        verwandelte_figuren["springer_weiss"][0]["command"]=lambda:zuege_springer_weiss(figur)
        verwandelte_figuren["springer_weiss"][0].place(x=xpos, y=ypos)
        aktuelle_figur.place_forget()
        alle_figuren.append(verwandelte_figuren["springer_weiss"][0])
        for i in felder:
            if felder[i]["x"]==xpos and felder[i]["y"]==ypos:
                felder[i]["figure"]=verwandelte_figuren["springer_weiss"][0]
        verwandelte_figuren["springer_weiss"].pop(0)
    if verwandel_figur=="laeufer":
        verwandelte_figuren["laeufer_weiss"][0]["image"]=laeufer_w_bild
        figur=verwandelte_figuren["laeufer_weiss"][0]
        verwandelte_figuren["laeufer_weiss"][0]["command"]=lambda:zuege_laeufer_weiss(figur)
        verwandelte_figuren["laeufer_weiss"][0].place(x=xpos, y=ypos)
        aktuelle_figur.place_forget()
        alle_figuren.append(verwandelte_figuren["laeufer_weiss"][0])
        for i in felder:
            if felder[i]["x"]==xpos and felder[i]["y"]==ypos:
                felder[i]["figure"]=verwandelte_figuren["laeufer_weiss"][0]
        verwandelte_figuren["laeufer_weiss"].pop(0)
    weristdran="schwarz"
    schachSchwarzBerechnen()
    auswahlDame.place_forget()
    auswahlTurm.place_forget()
    auswahlLaeufer.place_forget()
    auswahlSpringer.place_forget()

#acht Bauern weiss
bauer_w_bild=ImageTk.PhotoImage(Image.open("Bilder\Bauer_weiss.png"))
bauer1_w=Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiss(bauer1_w))
bauer1_w.farbe="weiss"
bauer1_w.art="bauer"
bauer2_w=Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiss(bauer2_w))
bauer2_w.farbe="weiss"
bauer2_w.art="bauer"
bauer3_w=Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiss(bauer3_w))
bauer3_w.farbe="weiss"
bauer3_w.art="bauer"
bauer4_w=Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiss(bauer4_w))
bauer4_w.farbe="weiss"
bauer4_w.art="bauer"
bauer5_w=Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiss(bauer5_w))
bauer5_w.farbe="weiss"
bauer5_w.art="bauer"
bauer6_w=Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiss(bauer6_w))
bauer6_w.farbe="weiss"
bauer6_w.art="bauer"
bauer7_w=Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiss(bauer7_w))
bauer7_w.farbe="weiss"
bauer7_w.art="bauer"
bauer8_w=Schachfigur(rahmen, image=bauer_w_bild, command=lambda:zuege_bauer_weiss(bauer8_w))
bauer8_w.farbe="weiss"
bauer8_w.art="bauer"

#zwei Tuerme weiss
turm_w_bild=ImageTk.PhotoImage(Image.open("Bilder\Turm_weiss.png"))
turm1_w=Schachfigur(rahmen, image=turm_w_bild, command=lambda:zuege_turm_weiss(turm1_w))
turm1_w.farbe="weiss"
turm1_w.art="turm"
turm2_w=Schachfigur(rahmen, image=turm_w_bild, command=lambda:zuege_turm_weiss(turm2_w))
turm2_w.farbe="weiss"
turm2_w.art="turm"

#zwei Springen weiss
springer_w_bild=ImageTk.PhotoImage(Image.open("Bilder\Springer_weiss.png"))
springer1_w=Schachfigur(rahmen, image=springer_w_bild, command=lambda:zuege_springer_weiss(springer1_w))
springer1_w.farbe="weiss"
springer1_w.art="springer"
springer2_w=Schachfigur(rahmen, image=springer_w_bild, command=lambda:zuege_springer_weiss(springer2_w))
springer2_w.farbe="weiss"
springer2_w.art="springer"

#zwei Laeufer weiss
laeufer_w_bild=ImageTk.PhotoImage(Image.open("Bilder\Läufer_weiss.png"))
laeufer1_w=Schachfigur(rahmen, image=laeufer_w_bild, command=lambda:zuege_laeufer_weiss(laeufer1_w))
laeufer1_w.farbe="weiss"
laeufer1_w.art="laeufer"
laeufer2_w=Schachfigur(rahmen, image=laeufer_w_bild, command=lambda:zuege_laeufer_weiss(laeufer2_w))
laeufer2_w.farbe="weiss"
laeufer2_w.art="laeufer"

#Koenig & Dame weiss
koenig_w_bild=ImageTk.PhotoImage(Image.open("Bilder\König_weiss.png"))
koenig_w=Schachfigur(rahmen, image=koenig_w_bild, command=lambda:zuege_koenig_weiss(koenig_w))
koenig_w.farbe="weiss"
koenig_w.art="koenig"
dame_w_bild=ImageTk.PhotoImage(Image.open("Bilder\Dame_weiss.png"))
dame_w=Schachfigur(rahmen, image=dame_w_bild, command=lambda:zuege_dame_weiss(dame_w))
dame_w.farbe="weiss"
dame_w.art="dame"


#acht Bauern schwarz
bauer_s_bild=ImageTk.PhotoImage(Image.open("Bilder\Bauer_schwarz.png"))
bauer1_s=Schachfigur(rahmen, image=bauer_s_bild, command=lambda:zuege_bauer_schwarz(bauer1_s))
bauer1_s.farbe="schwarz"
bauer1_s.art="bauer"
bauer2_s=Schachfigur(rahmen, image=bauer_s_bild, command=lambda:zuege_bauer_schwarz(bauer2_s))
bauer2_s.farbe="schwarz"
bauer2_s.art="bauer"
bauer3_s=Schachfigur(rahmen, image=bauer_s_bild, command=lambda:zuege_bauer_schwarz(bauer3_s))
bauer3_s.farbe="schwarz"
bauer3_s.art="bauer"
bauer4_s=Schachfigur(rahmen, image=bauer_s_bild, command=lambda:zuege_bauer_schwarz(bauer4_s))
bauer4_s.farbe="schwarz"
bauer4_s.art="bauer"
bauer5_s=Schachfigur(rahmen, image=bauer_s_bild, command=lambda:zuege_bauer_schwarz(bauer5_s))
bauer5_s.farbe="schwarz"
bauer5_s.art="bauer"
bauer6_s=Schachfigur(rahmen, image=bauer_s_bild, command=lambda:zuege_bauer_schwarz(bauer6_s))
bauer6_s.farbe="schwarz"
bauer6_s.art="bauer"
bauer7_s=Schachfigur(rahmen, image=bauer_s_bild, command=lambda:zuege_bauer_schwarz(bauer7_s))
bauer7_s.farbe="schwarz"
bauer7_s.art="bauer"
bauer8_s=Schachfigur(rahmen, image=bauer_s_bild, command=lambda:zuege_bauer_schwarz(bauer8_s))
bauer8_s.farbe="schwarz"
bauer8_s.art="bauer"

#zwei Tuerme schwarz
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

auswahlDame=Button()
auswahlTurm=Button()
auswahlSpringer=Button()
auswahlLaeufer=Button()

def figur_ziehen(xpos, ypos):
    global felder
    global weristdran
    global rochade
    global auswahlDame
    global auswahlLaeufer
    global auswahlSpringer
    global auswahlTurm
    global en_passant
    global verlauf
    for i in moegliche_ziele:
        if moegliche_ziele[i]["x"]==xpos:
            if moegliche_ziele[i]["y"]==ypos:
                for i in felder:
                    if felder[i]["figure"]==aktuelle_figur:
                        davorx=felder[i]["x"]
                        davory=felder[i]["y"]
                        felder[i]["figure"]="none"
                for i in felder:
                    if felder[i]["x"]==xpos and felder[i]["y"]==ypos:
                        if felder[i]["figure"]!="none":
                            felder[i]["figure"].place_forget()
                            verlauf=[]
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
                    auswahlDame=Button(image=dame_s_bild, command=lambda:bauer_verwandeln_schwarz(aktuelle_figur, "dame", xpos, ypos))
                    auswahlTurm=Button(image=turm_s_bild, command=lambda:bauer_verwandeln_schwarz(aktuelle_figur, "turm", xpos, ypos))
                    auswahlLaeufer=Button(image=laeufer_s_bild, command=lambda:bauer_verwandeln_schwarz(aktuelle_figur, "laeufer", xpos, ypos))
                    auswahlSpringer=Button(image=springer_s_bild, command=lambda:bauer_verwandeln_schwarz(aktuelle_figur, "springer", xpos, ypos))
                    auswahlDame.place(y=430, x=50)
                    auswahlTurm.place(y=430, x=100)
                    auswahlLaeufer.place(y=430, x=150)
                    auswahlSpringer.place(y=430, x=200)
                    weristdran="?"
                if aktuelle_figur.art=="bauer" and ypos==50:
                    auswahlDame=Button(image=dame_w_bild, command=lambda:bauer_verwandeln_weiss(aktuelle_figur, "dame", xpos, ypos))
                    auswahlTurm=Button(image=turm_w_bild, command=lambda:bauer_verwandeln_weiss(aktuelle_figur, "turm", xpos, ypos))
                    auswahlLaeufer=Button(image=laeufer_w_bild, command=lambda:bauer_verwandeln_weiss(aktuelle_figur, "laeufer", xpos, ypos))
                    auswahlSpringer=Button(image=springer_w_bild, command=lambda:bauer_verwandeln_weiss(aktuelle_figur, "springer", xpos, ypos))
                    auswahlDame.place(y=430, x=50)
                    auswahlTurm.place(y=430, x=100)
                    auswahlLaeufer.place(y=430, x=150)
                    auswahlSpringer.place(y=430, x=200)
                    weristdran="?"
                for i in en_passant:
                    en_passant[i]=False
                if davory==332 and ypos==238 and aktuelle_figur.farbe=="weiss":
                    en_passant[aktuelle_figur]=True
                if davory==97 and ypos==191 and aktuelle_figur.farbe=="schwarz":
                    en_passant[aktuelle_figur]=True
                if aktuelle_figur.art=="bauer" and aktuelle_figur.farbe=="weiss":
                    if davory==191 and ypos==144 and (xpos==davorx+47 or xpos==davorx-47):
                        for i in felder:
                            if felder[i]["y"]==davory and felder[i]["x"]==xpos and felder[i]["figure"]!="none":
                                if felder[i]["figure"].art=="bauer" and felder[i]["figure"].farbe=="schwarz":
                                    felder[i]["figure"].place_forget()
                                    felder[i]["figure"]="none"
                if aktuelle_figur.art=="bauer" and aktuelle_figur.farbe=="schwarz":
                    if davory==238 and ypos==285 and (xpos==davorx+47 or xpos==davorx-47):
                        for i in felder:
                            if felder[i]["y"]==davory and felder[i]["x"]==xpos and felder[i]["figure"]!="none":
                                if felder[i]["figure"].art=="bauer" and felder[i]["figure"].farbe=="weiss":
                                    felder[i]["figure"].place_forget()
                                    felder[i]["figure"]="none"
                if weristdran=="schwarz":
                    weristdran="weiss"
                    schachWeissBerechnen()
                elif weristdran=="weiss":
                    weristdran="schwarz"
                    schachSchwarzBerechnen()
                if aktuelle_figur.art=="bauer":
                    verlauf=[]
                gefunden=0
                felder_kopie=kopie_ausgeben(felder)
                rochade_kopie=copy.deepcopy(rochade)
                verlauf.append([felder_kopie, rochade])
                for i in verlauf:
                    if i[0]==felder and i[1]==rochade:
                        gefunden+=1
                    if gefunden==3:
                        schrift=Label(text="Remis:\nunentschieden", font="Arial, 30")
                        weristdran="?"
                        schrift.place(x=100, y=200)
    setzeZieleAufNull()
    farbenZurücksetzen()

felder={1:{"x":50, "y":379,"figure":turm1_w},2:{"x":97, "y":379,"figure":springer1_w},3:{"x":144, "y":379,"figure":laeufer1_w },4:{"x":191, "y":379,"figure":dame_w},5:{"x":238, "y":379,"figure":koenig_w},6:{"x":285, "y":379,"figure":laeufer2_w},7:{"x":332, "y":379,"figure":springer2_w},8:{"x":379, "y":379,"figure":turm2_w},9:{"x":50, "y":332,"figure":bauer1_w},10:{"x":97, "y":332,"figure":bauer2_w},11:{"x":144, "y":332,"figure":bauer3_w},12:{"x":191, "y":332,"figure":bauer4_w},13:{"x":238, "y":332,"figure":bauer5_w},14:{"x":285, "y":332,"figure":bauer6_w},15:{"x":332, "y":332,"figure":bauer7_w},16:{"x":379, "y":332,"figure":bauer8_w},17:{"x":50, "y":285,"figure":"none"},18:{"x":97, "y":285,"figure":"none"},19:{"x":144, "y":285,"figure":"none"},20:{"x":191, "y":285,"figure":"none"},21:{"x":238, "y":285,"figure":"none"},22:{"x":285, "y":285,"figure":"none"},23:{"x":332, "y":285,"figure":"none"},24:{"x":379, "y":285,"figure":"none"},25:{"x":50, "y":238,"figure":"none"},26:{"x":97, "y":238,"figure":"none"},27:{"x":144, "y":238,"figure":"none"},28:{"x":191, "y":238,"figure":"none"},29:{"x":238, "y":238,"figure":"none"},30:{"x":285, "y":238,"figure":"none"},31:{"x":332, "y":238,"figure":"none"},32:{"x":379, "y":238,"figure":"none"},33:{"x":50, "y":191,"figure":"none"},34:{"x":97, "y":191,"figure":"none"},35:{"x":144, "y":191,"figure":"none"},36:{"x":191, "y":191,"figure":"none"},37:{"x":238, "y":191,"figure":"none"},38:{"x":285, "y":191,"figure":"none"},39:{"x":332, "y":191,"figure":"none"},40:{"x":379, "y":191,"figure":"none"},41:{"x":50, "y":144,"figure":"none"},42:{"x":97, "y":144,"figure":"none"},43:{"x":144, "y":144,"figure":"none"},44:{"x":191, "y":144,"figure":"none"},45:{"x":238, "y":144,"figure":"none"},46:{"x":285, "y":144,"figure":"none"},47:{"x":332, "y":144,"figure":"none"},48:{"x":379, "y":144,"figure":"none"},49:{"x":50, "y":97,"figure":bauer1_s},50:{"x":97, "y":97,"figure":bauer2_s},51:{"x":144, "y":97,"figure":bauer3_s},52:{"x":191, "y":97,"figure":bauer4_s},53:{"x":238, "y":97,"figure":bauer5_s},54:{"x":285, "y":97,"figure":bauer6_s},55:{"x":332, "y":97,"figure":bauer7_s},56:{"x":379, "y":97,"figure":bauer8_s},57:{"x":50, "y":50,"figure":turm1_s},58:{"x":97, "y":50,"figure":springer1_s},59:{"x":144, "y":50,"figure":laeufer1_s},60:{"x":191, "y":50,"figure":dame_s},61:{"x":238, "y":50,"figure":koenig_s},62:{"x":285, "y":50,"figure":laeufer2_s},63:{"x":332, "y":50,"figure":springer2_s},64:{"x":379, "y":50,"figure":turm2_s}}
felder_kopie=kopie_ausgeben(felder)
rochade_kopie=copy.deepcopy(rochade)
verlauf=[[felder_kopie, rochade]]
alle_figuren=[bauer1_w, bauer2_w, bauer3_w, bauer4_w, bauer5_w, bauer6_w, bauer7_w, bauer8_w, turm1_w, turm2_w, springer1_w, springer2_w, laeufer1_w, laeufer2_w, koenig_w, dame_w, bauer1_s, bauer2_s, bauer3_s, bauer4_s, bauer5_s, bauer6_s, bauer7_s, bauer8_s, turm1_s, turm2_s, springer1_s, springer2_s, laeufer1_s, laeufer2_s, koenig_s, dame_s]
en_passant={bauer1_w: False, bauer2_w: False, bauer3_w: False, bauer4_w: False, bauer5_w: False, bauer6_w: False, bauer7_w: False, bauer8_w: False, bauer1_s: False, bauer2_s: False, bauer3_s: False, bauer4_s: False, bauer5_s: False, bauer6_s: False, bauer7_s: False, bauer8_s:False}

def figuren_plazieren():
    for i in felder:
        if felder[i]["figure"]!="none":
            felder[i]["figure"].place(x=felder[i]["x"], y=felder[i]["y"])

setzeZieleAufNull()
figuren_plazieren()
fenster.mainloop()