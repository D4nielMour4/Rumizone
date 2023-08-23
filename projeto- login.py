import customtkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def janela_login():
    frame_inicio.pack_forget()
    frame_registro.pack_forget() 
    frame_login.pack(fill="both", expand=True)

def janela_registro():
    frame_inicio.pack_forget()
    frame_login.pack_forget()
    frame_registro.pack(fill="both", expand=True)


tela = customtkinter.CTk(fg_color="#CFD8DC")
tela.geometry("1360x720")
tela.resizable(False, False)
tela.title("Rumizone")  

frame_inicio = customtkinter.CTkFrame(tela, fg_color="#CFD8DC")
frame_inicio.pack()

iconevaca = customtkinter.CTkImage(light_image=Image.open(r"C:\Users\Seabroso\Documents\GitHub\Rumizone\imagens\rumizone icone.png"),
                                   dark_image=Image.open(r"C:\Users\Seabroso\Documents\GitHub\Rumizone\imagens\rumizone icone.png"),
                                   size=(300,320))
label_icone = customtkinter.CTkLabel(master=tela, text="", image=iconevaca)
label_icone.place(x=510, y=30)

texto = customtkinter.CTkLabel(tela, text="Rumizone", text_color="#607D8B", font=("Robot", 49))
texto.place(x=560, y=300)

texto1 = customtkinter.CTkLabel(tela,bg_color="transparent", text="Monitoramento e comportamento animal", text_color="#607D8B", font=("Helvetica", 20))
texto1.place(x=480, y=360)

botao1 = customtkinter.CTkButton(tela, 
                                 text="Login",
                                  font=("Times",40),
                                  corner_radius=45,
                                  border_width=3,
                                  border_color="black",
                                 command=janela_login,
                                  fg_color="#8690AF",
                                  text_color="white",
                                   width=570, height=90)
botao1.place(x=380, y=420)

botao2 = customtkinter.CTkButton(tela,
                                  text="Registre-se", 
                                  font=("Times",40),
                                  command=janela_registro,
                                  corner_radius=45,
                                  border_width=3,
                                  border_color="black",
                                  fg_color="#8690AF",
                                  text_color="white",
                                  width=570, height=90)
botao2.place(x=380, y=520)



tela.mainloop()