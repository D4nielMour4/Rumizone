import customtkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

tela = customtkinter.CTk(fg_color="#CFD8DC")
tela.geometry("1360x720")
tela.resizable(False, False)
tela.title("Rumizone")



button_redondo = customtkinter.CTkButton(tela, text="", fg_color="black", width=50, height=50, corner_radius=300)
button_redondo.place(x=560, y=300)

tela.mainloop()