import customtkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def clique():
    print("Fazer login")

def voltar_para_inicio(frame_atual):
    frame_atual.pack_forget()
    frame_inicio.pack()

def janela_login():
    frame_inicio.pack_forget()
    frame_registro.pack_forget() 
    frame_login.pack(fill="both", expand=True)

def janela_registro():
    frame_inicio.pack_forget()
    frame_login.pack_forget()
    frame_registro.pack(fill="both", expand=True)

def escolher_imagem():
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")])
    if filepath:
        imagem = Image.open(filepath)
        imagem.thumbnail((292, 480))  # Redimensionar a imagem para o tamanho desejado
        imagem = ImageTk.PhotoImage(imagem)
        label_imagem.configure(image=imagem)
        label_imagem.image = imagem

tela = customtkinter.CTk(fg_color="#CFD8DC")
tela.geometry("1360x720")
tela.resizable(False, False)
tela.title("Rumizone")  

frame_inicio = customtkinter.CTkFrame(tela, fg_color="#CFD8DC")
frame_inicio.pack()

iconevaca = customtkinter.CTkImage(light_image=Image.open(r"imagens\rumizone icone.png"),
                                   dark_image=Image.open(r"imagens\rumizone icone.png"),
                                   size=(300,320))
label_icone = customtkinter.CTkLabel(master=tela, text="", image=iconevaca)
label_icone.place(x=510, y=30)

texto = customtkinter.CTkLabel(tela, text="Rumizone", text_color="#607D8B", font=("Robot", 49))
texto.place(x=560, y=350)

texto1 = customtkinter.CTkLabel(tela,bg_color="transparent", text="Monitoramento e comportamento animal", text_color="#607D8B", font=("Helvetica", 20))
texto1.place(x=480, y=410)

botao1 = customtkinter.CTkButton(tela, text="Login", font=("Helvetica",40), command=janela_login, fg_color="#8690AF",text_color="white", width=370, height=70)
botao1.place(x=480, y=470)

botao2 = customtkinter.CTkButton(tela, text="Registre-se", font=("Helvetica",40), command=janela_registro, fg_color="#8690AF",text_color="white", width=370, height=70)
botao2.place(x=480, y=570)

frame_login = customtkinter.CTkFrame(master=tela, fg_color="#CFD8DC")
frame_registro = customtkinter.CTkFrame(tela, fg_color="#CFD8DC")


#Frame/Tela de login
texto_login = customtkinter.CTkLabel(frame_login, text="Fazer login", text_color="#607D8B", font=("Helvetica", 70))
texto_login.place(x=510, y=180)
email = customtkinter.CTkEntry(frame_login, placeholder_text="Digite seu usuário", text_color="black", fg_color="white", width=370, height=35, font=("Helvetica",20))
email.place(x=500, y=280)
senha = customtkinter.CTkEntry(frame_login, placeholder_text="Digite sua senha", text_color="black", fg_color="white", width=370, height=35, font=("Helvetica",20), show="*")
senha.place(x=500, y=330)
botao_login = customtkinter.CTkButton(frame_login, text="Entrar", fg_color="#8690AF", text_color="white", command=clique)
botao_login.place(x=730, y=400)
botao_voltar_login = customtkinter.CTkButton(frame_login, text="Voltar",fg_color="#8690AF", command=lambda: voltar_para_inicio(frame_login))
botao_voltar_login.place(x=500, y=400)#Botão com função de voltar pra tela inicial

#Frame/Tela de registro
botao_escolher_imagem = customtkinter.CTkButton(frame_registro, text="Escolher foto de perfil", command=escolher_imagem,
                                                 fg_color="#8690AF", text_color="white")
botao_escolher_imagem.place(x=95, y=260)

label_imagem = customtkinter.CTkLabel(frame_registro)
label_imagem.place(x=30, y=25)

nomefuncionario = customtkinter.CTkEntry(frame_registro, placeholder_text="Digite seu nome",
                                         text_color="black", fg_color="#FFDA8F", width=280, height=60, font=("Helvetica", 20))
nomefuncionario.place(x=20, y=290)

nascimentofuncionario = customtkinter.CTkEntry(frame_registro, placeholder_text="Data de nasciment.",
                                               text_color="black", fg_color="#8690AF", width=280, height=60, font=("Helvetica", 20))
nascimentofuncionario.place(x=20, y=360)

emailfuncionario = customtkinter.CTkEntry(frame_registro, placeholder_text="Diga seu e-mail",
                                           text_color="black", fg_color="#FF9EB1", width=280, height=60, font=("Helvetica", 20))
emailfuncionario.place(x=20, y=430)

telefonefuncionario = customtkinter.CTkEntry(frame_registro, placeholder_text="Diga número de celular.",
                                             text_color="black", fg_color="#8690AF", width=280, height=60, font=("Helvetica", 20))
telefonefuncionario.place(x=20, y=500)

botao_registro = customtkinter.CTkButton(frame_registro, text="Criar conta", fg_color="#8690AF", text_color="white", command=clique)
botao_registro.place(x=170, y=570)

botao_voltar_login1 = customtkinter.CTkButton(frame_registro, text="Voltar",fg_color="#8690AF", command=lambda: voltar_para_inicio(frame_registro))
botao_voltar_login1.place(x=20, y=570)#Botão com função de voltar pra tela inicial





tela.mainloop()