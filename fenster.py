from tkinter import *
from PIL import ImageTk, Image
from funktionen import *
fenster = Tk()
fenster.title("Schach Projekt")
rahmen=Frame(fenster, relief="ridge", borderwidth=5)
rahmen.pack()
schachbrett_bild = ImageTk.PhotoImage(Image.open("Bilder\Schachbrett.png"))
schachbrett = Label(rahmen, image=schachbrett_bild)
schachbrett.pack(expand=True, padx=30, pady=30)

#acht Bauern weiß
bauer_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Bauer_weiß.png"))
bauer1_w = Button(rahmen, image=bauer_w_bild)
bauer1_w["command"] = zeige_bauer
bauer1_w.place(y=333, x=52)
bauer2_w = Button(rahmen, image=bauer_w_bild)
bauer2_w.place(y=333, x=100)
bauer3_w = Button(rahmen, image=bauer_w_bild)
bauer3_w.place(y=333, x=147)
bauer4_w = Button(rahmen, image=bauer_w_bild)
bauer4_w.place(y=333, x=194)
bauer5_w = Button(rahmen, image=bauer_w_bild)
bauer5_w.place(y=333, x=242)
bauer6_w = Button(rahmen, image=bauer_w_bild)
bauer6_w.place(y=333, x=287)
bauer7_w = Button(rahmen, image=bauer_w_bild)
bauer7_w.place(y=333, x=332)
bauer8_w = Button(rahmen, image=bauer_w_bild)
bauer8_w.place(y=333, x=382)

#zwei Türme weiß
turm_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Turm_weiß.png"))
turm1_w = Label(rahmen, image=turm_w_bild)
turm1_w.place(y=383, x=52)
turm2_w = Button(rahmen, image=turm_w_bild)
turm2_w.place(y=383, x=382)

#zwei Springen weiß
springer_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Springer_weiß.png"))
springer1_w = Button(rahmen, image=springer_w_bild)
springer1_w.place(y=383, x=100)
springer2_w = Button(rahmen, image=springer_w_bild)
springer2_w.place(y=383, x=332)

#zwei Laefer weiß
laefer_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Läufer_weiß.png"))
laefer1_w = Button(rahmen, image=laefer_w_bild)
laefer1_w.place(y=383, x=147)
laefer2_w = Button(rahmen, image=laefer_w_bild)
laefer2_w.place(y=383, x=287)

#Koenig & Dame weiß
koenig_w_bild = ImageTk.PhotoImage(Image.open("Bilder\König_weiß.png"))
koenig_w = Button(rahmen, image=koenig_w_bild)
koenig_w.place(y=383, x=240)
dame_w_bild = ImageTk.PhotoImage(Image.open("Bilder\Dame_weiß.png"))
dame_w = Button(rahmen, image=dame_w_bild)
dame_w.place(y=383, x=194)


#acht Bauern schwarz
bauer_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Bauer_schwarz.png"))
bauer1_s = Button(rahmen, image=bauer_s_bild)
bauer1_s.place(y=102, x=52)
bauer2_s = Button(rahmen, image=bauer_s_bild)
bauer2_s.place(y=102, x=100)
bauer3_s = Button(rahmen, image=bauer_s_bild)
bauer3_s.place(y=102, x=147)
bauer4_s = Button(rahmen, image=bauer_s_bild)
bauer4_s.place(y=102, x=194)
bauer5_s = Button(rahmen, image=bauer_s_bild)
bauer5_s.place(y=102, x=242)
bauer6_s = Button(rahmen, image=bauer_s_bild)
bauer6_s.place(y=102, x=287)
bauer7_s = Button(rahmen, image=bauer_s_bild)
bauer7_s.place(y=102, x=332)
bauer8_s = Button(rahmen, image=bauer_s_bild)
bauer8_s.place(y=102, x=382)

#zwei Türme schwarz
turm_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Turm_schwarz.png"))
turm1_s = Button(rahmen, image=turm_s_bild)
turm1_s.place(y=52, x=52)
turm2_s = Button(rahmen, image=turm_s_bild)
turm2_s.place(y=52, x=382)

#zwei Springen schwarz
springer_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Springer_schwarz.png"))
springer1_s = Button(rahmen, image=springer_s_bild)
springer1_s.place(y=52, x=100)
springer2_s = Button(rahmen, image=springer_s_bild)
springer2_s.place(y=52, x=332)

#zwei Laefer schwarz
laefer_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Läufer_schwarz.png"))
laefer1_s = Button(rahmen, image=laefer_s_bild)
laefer1_s.place(y=52, x=147)
laefer2_s = Button(rahmen, image=laefer_s_bild)
laefer2_s.place(y=52, x=287)

#Koenig & Dame schwarz
koenig_s_bild = ImageTk.PhotoImage(Image.open("Bilder\König_schwarz.png"))
koenig_s = Button(rahmen, image=koenig_s_bild)
koenig_s.place(y=52, x=240)
dame_s_bild = ImageTk.PhotoImage(Image.open("Bilder\Dame_schwarz.png"))
dame_s = Button(rahmen, image=dame_s_bild)
dame_s.place(y=52, x=194)

fenster.mainloop()