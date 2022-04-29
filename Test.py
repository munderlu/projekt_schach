from ast import IfExp
from multiprocessing.connection import wait
from tkinter import *
from turtle import filling
from PIL import ImageTk, Image
fenster = Tk()
fenster.title("Schach Projekt")
rahmen=Frame(fenster, relief="ridge", borderwidth=5)
rahmen.pack()
schachbrett_bild = ImageTk.PhotoImage(Image.open("Bilder\Schachbrett.png"))
schachbrett = Label(rahmen, image=schachbrett_bild)
schachbrett.pack(expand=True, padx=30, pady=30)

mögliche_ziele={1:{"x":"none", "y":"none"}, 2:{"x":"none", "y":"none"}, 3:{"x":"none", "y":"none"}, 4:{"x":"none", "y":"none"}, 5:{"x":"none", "y":"none"}, 6:{"x":"none", "y":"none"}, 7:{"x":"none", "y":"none"}, 8:{"x":"none", "y":"none"}, 9:{"x":"none", "y":"none"}, 10:{"x":"none", "y":"none"}, 11:{"x":"none", "y":"none"}, 12:{"x":"none", "y":"none"}, 13:{"x":"none", "y":"none"}, 14:{"x":"none", "y":"none"}, 15:{"x":"none", "y":"none"}, 16:{"x":"none", "y":"none"}, 17:{"x":"none", "y":"none"}, 18:{"x":"none", "y":"none"}, 19:{"x":"none", "y":"none"}, 20:{"x":"none", "y":"none"}, 21:{"x":"none", "y":"none"}, 22:{"x":"none", "y":"none"}, 23:{"x":"none", "y":"none"}, 24:{"x":"none", "y":"none"}, 25:{"x":"none", "y":"none"}, 26:{"x":"none", "y":"none"}, 27:{"x":"none", "y":"none"}}

#acht Bauern weiß
bauer_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Bauer_weiß.png"))
bauer1_w = Button(rahmen, image=bauer_w_bild, command=lambda:bauer1_w.zeige_bauer_weiß("bauer1_w"))
bauer2_w = Button(rahmen, image=bauer_w_bild, command=lambda:bauer2_w.zeige_bauer_weiß("bauer2_w"))
bauer3_w = Button(rahmen, image=bauer_w_bild, command=lambda:bauer3_w.zeige_bauer_weiß("bauer3_w"))
bauer4_w = Button(rahmen, image=bauer_w_bild, command=lambda:bauer4_w.zeige_bauer_weiß("bauer4_w"))
bauer5_w = Button(rahmen, image=bauer_w_bild, command=lambda:bauer5_w.zeige_bauer_weiß("bauer5_w"))
bauer6_w = Button(rahmen, image=bauer_w_bild, command=lambda:bauer6_w.zeige_bauer_weiß("bauer6_w"))
bauer7_w = Button(rahmen, image=bauer_w_bild, command=lambda:bauer7_w.zeige_bauer_weiß("bauer7_w"))
bauer8_w = Button(rahmen, image=bauer_w_bild, command=lambda:bauer8_w.zeige_bauer_weiß("bauer8_w"))

#zwei Türme weiß
turm_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Turm_weiß.png"))
turm1_w = Button(rahmen, image=turm_w_bild)
turm2_w = Button(rahmen, image=turm_w_bild)

#zwei Springen weiß
springer_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Springer_weiß.png"))
springer1_w = Button(rahmen, image=springer_w_bild)
springer2_w = Button(rahmen, image=springer_w_bild)

#zwei Laeufer weiß
laeufer_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Läufer_weiß.png"))
laeufer1_w = Button(rahmen, image=laeufer_w_bild)
laeufer2_w = Button(rahmen, image=laeufer_w_bild)

#Koenig & Dame weiß
koenig_w_bild = ImageTk.PhotoImage(Image.open("Bilder\König_weiß.png"))
koenig_w = Button(rahmen, image=koenig_w_bild)
dame_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Dame_weiß.png"))
dame_w = Button(rahmen, image=dame_w_bild)


#acht Bauern schwarz
bauer_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Bauer_schwarz.png"))
bauer1_s = Button(rahmen, image=bauer_s_bild, command=lambda: bauer1_s.zeige_bauer_schwarz("bauer1_s"))
bauer2_s = Button(rahmen, image=bauer_s_bild, command=lambda: bauer2_s.zeige_bauer_schwarz("bauer2_s"))
bauer3_s = Button(rahmen, image=bauer_s_bild, command=lambda: bauer3_s.zeige_bauer_schwarz("bauer3_s"))
bauer4_s = Button(rahmen, image=bauer_s_bild, command=lambda: bauer4_s.zeige_bauer_schwarz("bauer4_s"))
bauer5_s = Button(rahmen, image=bauer_s_bild, command=lambda: bauer5_s.zeige_bauer_schwarz("bauer5_s"))
bauer6_s = Button(rahmen, image=bauer_s_bild, command=lambda: bauer6_s.zeige_bauer_schwarz("bauer6_s"))
bauer7_s = Button(rahmen, image=bauer_s_bild, command=lambda: bauer7_s.zeige_bauer_schwarz("bauer7_s"))
bauer8_s = Button(rahmen, image=bauer_s_bild, command=lambda: bauer8_s.zeige_bauer_schwarz("bauer8_s"))

#zwei Türme schwarz
turm_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Turm_schwarz.png"))
turm1_s = Button(rahmen, image=turm_s_bild)
turm2_s = Button(rahmen, image=turm_s_bild)

#zwei Springen schwarz
springer_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Springer_schwarz.png"))
springer1_s = Button(rahmen, image=springer_s_bild)
springer2_s = Button(rahmen, image=springer_s_bild)

#zwei Laeufer schwarz
laeufer_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Läufer_schwarz.png"))
laeufer1_s = Button(rahmen, image=laeufer_s_bild)
laeufer2_s = Button(rahmen, image=laeufer_s_bild)

#Koenig & Dame schwarz
koenig_s_bild = ImageTk.PhotoImage(Image.open("Bilder\König_schwarz.png"))
koenig_s = Button(rahmen, image=koenig_s_bild)
dame_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Dame_schwarz.png"))
dame_s = Button(rahmen, image=dame_s_bild)

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



def plazieren(x):
    if x == "figuren":
        for i in felder:
            if felder[i]["figure"]!="none":
                felder[i]["figure"].place(x=felder[i]["x"], y=felder[i]["y"])
    elif x == "ziele":
        for i in mögliche_ziele:
            if mögliche_ziele[i]["x"]!="none":
                ziele[i].place(x=mögliche_ziele[i]["x"], y=mögliche_ziele[i]["y"])

            




    

plazieren("figuren")
plazieren("ziele")

fenster.mainloop()