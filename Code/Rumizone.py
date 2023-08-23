import customtkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

#criando tela
tela = customtkinter.CTk(fg_color="#CFD8DC")
tela.geometry("1360x720")
tela.resizable(False, False)
tela.title("Rumizone")

#Imagens
img_botao_voltar = customtkinter.CTkImage(light_image=Image.open(r"imagens\botao voltar.png"),
                                        dark_image=Image.open(r"imagens\botao voltar.png"),
                                        size=(50,50))

iconevaca = customtkinter.CTkImage(light_image=Image.open(r"imagens\rumizone icone.png"),
                                   dark_image=Image.open(r"imagens\rumizone icone.png"),
                                   size=(250,320))

img_vaquinha = customtkinter.CTkImage(light_image=Image.open(r"imagens\vaquinha.png"), 
                                        dark_image=Image.open(r"imagens\vaquinha.png"),
                                        size=(150, 90))

img_cerca = customtkinter.CTkImage(light_image=Image.open(r"imagens\cerca do curral.png"),
                                    dark_image=Image.open(r"imagens\cerca do curral.png"),
                                    size=(60, 60))

img_fazendeiro = customtkinter.CTkImage(light_image=Image.open(r"imagens\fazendeiro.png"),
                                    dark_image=Image.open(r"imagens\fazendeiro.png"),
                                    size=(150, 90))

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

def Continuar_login_to_principal():
    frame_login.pack_forget()
    frame_principal.pack(fill="both", expand=True)

#Criando Frames Login
frame_login = customtkinter.CTkFrame(master=tela, fg_color="#CFD8DC")

texto_login = customtkinter.CTkLabel(frame_login, text="Fazer login", text_color="#607D8B", font=("Helvetica", 70))
texto_login.place(x=510, y=180)

entrada_email_login = customtkinter.CTkEntry(frame_login, placeholder_text="Digite seu usuário", text_color="black", fg_color="white", width=370, height=35, font=("Helvetica",20))
entrada_email_login.place(x=500, y=280)

entrada_senha_login = customtkinter.CTkEntry(frame_login, placeholder_text="Digite sua senha", text_color="black", fg_color="white", width=370, height=35, font=("Helvetica",20), show="*")
entrada_senha_login.place(x=500, y=350)

botao_login = customtkinter.CTkButton(frame_login, text="Entrar", fg_color="#8690AF", text_color="white", command=Continuar_login_to_principal)
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

label_icone_registro = customtkinter.CTkLabel(master=frame_registro, text="", image=iconevaca)
label_icone_registro.place(x=50, y=2)

botao_continuar_registo = customtkinter.CTkButton(frame_registro, text="Continuar", fg_color="#FFDA8F", text_color="black", command="")
botao_continuar_registo.place(x=1150, y=650)

botao_voltar_registro = customtkinter.CTkButton(frame_registro, corner_radius=200, text="", fg_color="#FF9EB1", text_color="black", command=volta_registro_to_home, image=img_botao_voltar)
botao_voltar_registro.place(x=60, y=650)#Botão com função de voltar pra tela inicial

entradra_nome_registro = customtkinter.CTkEntry(frame_registro, placeholder_text="Nome", text_color="black", fg_color="#FFDA8F", width=370, height=35, font=("Helvetica",40), corner_radius=200)
entradra_nome_registro.place(x=320, y=100)

entrada_idade_registro = customtkinter.CTkEntry(frame_registro, placeholder_text="Idade", text_color="black", fg_color="#FF9EB1", width=370, height=35, font=("Helvetica",40), corner_radius=200)
entrada_idade_registro.place(x=60, y=250)

entrada_profissao_registro = customtkinter.CTkEntry(frame_registro, placeholder_text="Profissão", text_color="black", fg_color="#FFDA8F", width=370, height=35, font=("Helvetica",40), corner_radius=200)
entrada_profissao_registro.place(x=60, y=350)

entrada_celular_registro = customtkinter.CTkEntry(frame_registro, placeholder_text="Celular", text_color="black", fg_color="#FF9EB1", width=370, height=35, font=("Helvetica",40), corner_radius=200)
entrada_celular_registro.place(x=60, y=450)

entrada_email_registro = customtkinter.CTkEntry(frame_registro, placeholder_text="Email", text_color="black", fg_color="#FFDA8F", width=370, height=35, font=("Helvetica",40), corner_radius=200)
entrada_email_registro.place(x=60, y=550)

entrada_comentarios_registro = customtkinter.CTkEntry(frame_registro, placeholder_text="Comentários", text_color="black", fg_color="white", width=370, height=35, font=("Helvetica",40), corner_radius=200)
entrada_comentarios_registro.place(x=500, y=500)

#----------------------------------------------

#Declarando Funcoes de Botao da tela principal


#Criando Frames Principal
frame_principal = customtkinter.CTkFrame(master=tela, fg_color="#CFD8DC")

botao_voltar_principal = customtkinter.CTkButton(frame_principal, corner_radius=200, text="", fg_color="#FF9EB1", text_color="black", command=volta_registro_to_home, image=img_botao_voltar)
botao_voltar_principal.place(x=60, y=650)

iconevaca_principal = customtkinter.CTkLabel(master=frame_principal, text="", image=iconevaca)
iconevaca_principal.place(x=530, y=0)

botao_perfil_principal = customtkinter.CTkButton(frame_principal, text="", fg_color="#FFDA8F", text_color="black", command="", width=200, height=200, image=img_fazendeiro)
botao_perfil_principal.place(x=300, y=300)

botao_curral_principal = customtkinter.CTkButton(frame_principal, text="", fg_color="#FF9EB1", text_color="black", command="", width=200, height=200, image=img_cerca)
botao_curral_principal.place(x=560, y=300)

botao_cadastrar_animal_principal = customtkinter.CTkButton(frame_principal, text="", fg_color="#8690AF", text_color="black", command="", width=200, height=200, image=img_vaquinha)
botao_cadastrar_animal_principal.place(x=820, y=300)


#----------------------------------------------
tela.mainloop()