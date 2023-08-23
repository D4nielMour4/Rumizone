import customtkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def escolher_imagem():
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")])
    if filepath:
        imagem = Image.open(filepath)
        imagem.thumbnail((292, 480))  # Redimensionar a imagem para o tamanho do ícone
        imagem = ImageTk.PhotoImage(imagem)
        label_imagem.config(image=imagem)
        label_imagem.image = imagem

telacadfunci = customtkinter.CTk(fg_color="#CFD8DC")
telacadfunci.geometry("1360x720")
telacadfunci.resizable(False, False)
telacadfunci.title("Cadastro de funcionários")

frame_inicio = customtkinter.CTkFrame(telacadfunci, fg_color="#CFD8DC")

iconevaca1 = customtkinter.CTkImage(light_image=Image.open(r"imagens\ícone rumizone.png"),
                                   dark_image=Image.open(r"imagens\ícone rumizone.png"), size=(292, 480))
label_icone = customtkinter.CTkLabel(master=telacadfunci, text="", image=iconevaca1)
label_icone.place(x=5, y=5)

botao_escolher_imagem = customtkinter.CTkButton(telacadfunci, text="Escolher Imagem", command=escolher_imagem,
                                                 fg_color="#8690AF", text_color="white")
botao_escolher_imagem.place(x=20, y=570)

label_imagem = Label(telacadfunci)
label_imagem.place(x=5, y=5)

nomefuncionario = customtkinter.CTkEntry(telacadfunci, placeholder_text="Digite seu nome",
                                         text_color="black", fg_color="#FFDA8F", width=280, height=60, font=("Helvetica", 20))
nomefuncionario.place(x=20, y=290)

nascimentofuncionario = customtkinter.CTkEntry(telacadfunci, placeholder_text="Data de nasciment.",
                                               text_color="black", fg_color="#8690AF", width=280, height=60, font=("Helvetica", 20))
nascimentofuncionario.place(x=20, y=360)

emailfuncionario = customtkinter.CTkEntry(telacadfunci, placeholder_text="Diga seu e-mail",
                                           text_color="black", fg_color="#FF9EB1", width=280, height=60, font=("Helvetica", 20))
emailfuncionario.place(x=20, y=430)

telefonefuncionario = customtkinter.CTkEntry(telacadfunci, placeholder_text="Diga número de celular.",
                                             text_color="black", fg_color="#8690AF", width=280, height=60, font=("Helvetica", 20))
telefonefuncionario.place(x=20, y=500)



telacadfunci.mainloop()