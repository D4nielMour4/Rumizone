import customtkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

#criando tela
tela = customtkinter.CTk(fg_color="#CFD8DC")
tela.geometry("1360x720")
tela.resizable(False, False)
tela.title("Rumizone")

#Declarando Funcoes de Botao da tela Home

def janela_login():
    frame_home.pack_forget()
    frame_login.pack(fill="both", expand=True)

def janela_registro():
    frame_home.pack_forget()
    frame_registro.pack(fill="both", expand=True)

#Criando Frames Home
frame_home = customtkinter.CTkFrame(tela, fg_color="#CFD8DC")
frame_home.pack()

iconevaca = customtkinter.CTkImage(light_image=Image.open(r"imagens\rumizone icone.png"),
                                   dark_image=Image.open(r"imagens\rumizone icone.png"),
                                   size=(250,320))

label_icone = customtkinter.CTkLabel(master=tela, text="", image=iconevaca)
label_icone.place(x=530, y=5)

titulo_rumizone_home = customtkinter.CTkLabel(tela, text="Rumizone", text_color="#607D8B", font=("Robot", 49))
titulo_rumizone_home.place(x=550, y=250)

subtitulo_rumizone_home = customtkinter.CTkLabel(tela, text="Monitoramento e comportamento animal", text_color="#607D8B", font=("Helvetica", 20))
subtitulo_rumizone_home.place(x=480, y=310)

botao_login_home = customtkinter.CTkButton(tela, text="Login", font=("Helvetica",40), command=janela_login, fg_color="#8690AF",text_color="white", width=370, height=70, corner_radius=200)
botao_login_home.place(x=480, y=350)

botao_registro_home = customtkinter.CTkButton(tela, text="Registre-se", font=("Helvetica",40), command=janela_registro, fg_color="#8690AF",text_color="white", width=370, height=70, corner_radius=200)
botao_registro_home.place(x=480, y=440)
#----------------------------------------------
#Declarando Funcoes de Botao da tela Login

def volta__login_to_home():
    frame_login.pack_forget()
    frame_home.pack(fill="both", expand=True)

#Criando Frames Login
frame_login = customtkinter.CTkFrame(master=tela, fg_color="#CFD8DC")

texto_login = customtkinter.CTkLabel(frame_login, text="Fazer login", text_color="#607D8B", font=("Helvetica", 70))
texto_login.place(x=510, y=180)

entrada_email_login = customtkinter.CTkEntry(frame_login, placeholder_text="Digite seu usuário", text_color="black", fg_color="white", width=370, height=35, font=("Helvetica",20))
entrada_email_login.place(x=500, y=280)

entrada_senha_login = customtkinter.CTkEntry(frame_login, placeholder_text="Digite sua senha", text_color="black", fg_color="white", width=370, height=35, font=("Helvetica",20), show="*")
entrada_senha_login.place(x=500, y=350)

botao_login = customtkinter.CTkButton(frame_login, text="Entrar", fg_color="#8690AF", text_color="white", command="")
botao_login.place(x=730, y=400)
botao_voltar_login = customtkinter.CTkButton(frame_login, text="Voltar",fg_color="#8690AF", command=volta__login_to_home)
botao_voltar_login.place(x=500, y=400)#Botão com função de voltar pra tela inicial

#----------------------------------------------
#Declarando Funcoes de Botao da tela Registro

def volta_registro_to_home():
    frame_registro.pack_forget()
    frame_home.pack(fill="both", expand=True)

def abre_arquivo():
    arquivo = filedialog.askopenfilename(initialdir="/", title="Selecione o arquivo", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    print(arquivo)

#Criando Frames Registro
frame_registro = customtkinter.CTkFrame(master=tela, fg_color="#CFD8DC")

iconevaca_registro = customtkinter.CTkImage(light_image=Image.open(r"imagens\rumizone icone.png"),
                                      dark_image=Image.open(r"imagens\rumizone icone.png"),
                                        size=(250,320))

botao_continuar_registo = customtkinter.CTkButton(frame_registro, text="Continuar", fg_color="#8690AF", text_color="white", command="")
botao_continuar_registo.place(x=730, y=400)

#----------------------------------------------

tela.mainloop()