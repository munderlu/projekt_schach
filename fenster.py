from tkinter import *
from PIL import ImageTk, Image
fenster = Tk()
fenster.geometry("500x500")
text=Label(text="Test")
text.pack(expand=1)
bild = ImageTk.PhotoImage(Image.open("Bilder\König_schwarz.png"))
bildInFenster = Label(image=bild)
bildInFenster.pack()
fenster.mainloop()