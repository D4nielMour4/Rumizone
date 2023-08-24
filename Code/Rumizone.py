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

icone_vaca_home = customtkinter.CTkImage(light_image=Image.open(r"imagens\rumizone icone.png"),
                                   dark_image=Image.open(r"imagens\rumizone icone.png"),
                                   size=(300,320))

img_vaquinha = customtkinter.CTkImage(light_image=Image.open(r"imagens\vaquinha.png"), 
                                        dark_image=Image.open(r"imagens\vaquinha.png"),
                                        size=(150, 90))

img_cerca = customtkinter.CTkImage(light_image=Image.open(r"imagens\cerca do curral.png"),
                                    dark_image=Image.open(r"imagens\cerca do curral.png"),
                                    size=(60, 60))

img_fazendeiro = customtkinter.CTkImage(light_image=Image.open(r"imagens\fazendeiro.png"),
                                    dark_image=Image.open(r"imagens\fazendeiro.png"),
                                    size=(150, 90))

icone_vaca_login = customtkinter.CTkImage(light_image=Image.open(r"imagens\rumizone icone.png"),
                                   dark_image=Image.open(r"imagens\rumizone icone.png"),
                                   size=(150,158))

img_feto = customtkinter.CTkImage(light_image=Image.open(r"imagens\feto.png"),
                                    dark_image=Image.open(r"imagens\feto.png"),
                                    size=(60, 60))

img_carne = customtkinter.CTkImage(light_image=Image.open(r"imagens\carne.png"),
                                    dark_image=Image.open(r"imagens\carne.png"),
                                    size=(60, 60))

img_leite = customtkinter.CTkImage(light_image=Image.open(r"imagens\caixa de leite.png"),
                                    dark_image=Image.open(r"imagens\caixa de leite.png"),
                                    size=(60, 60))

img_genders = customtkinter.CTkImage(light_image=Image.open(r"imagens\genders.png"),
                                    dark_image=Image.open(r"imagens\genders.png"),
                                    size=(60, 50))

img_lixo = customtkinter.CTkImage(light_image=Image.open(r"imagens\lata de lixo.png"),
                                    dark_image=Image.open(r"imagens\lata de lixo.png"),
                                    size=(60, 60))

img_vaquinha_lista = customtkinter.CTkImage(light_image=Image.open(r"imagens\vaquinha.png"),
                                            dark_image=Image.open(r"imagens\vaquinha.png"),
                                            size=(100, 70))

img_vaca_cadastro = customtkinter.CTkImage(light_image=Image.open(r"imagens\rumizone icone.png"), 
                dark_image=Image.open(r"imagens\rumizone icone.png"),
                size=(200, 180))

player= customtkinter.CTkImage(light_image=Image.open(r"imagens\player.png"),
                dark_image=Image.open(r"imagens\player.png"),
                size=(205, 205))



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

label_icone = customtkinter.CTkLabel(master=tela, text="", image=icone_vaca_home)
label_icone.place(x=510, y=30)

titulo_rumizone_home = customtkinter.CTkLabel(tela, text="Rumizone", text_color="#607D8B", font=("Robot", 49))
titulo_rumizone_home.place(x=560, y=300)

subtitulo_rumizone_home = customtkinter.CTkLabel(tela, text="Monitoramento e comportamento animal", text_color="#607D8B", font=("times", 20))
subtitulo_rumizone_home.place(x=480, y=360)

botao_login_home = customtkinter.CTkButton(tela, text="Login",font=("Times",40),corner_radius=45,border_width=3,border_color="black",command=janela_login,fg_color="#8690AF",text_color="white",width=570, height=90)

botao_login_home.place(x=380, y=420)

botao_registro_home = customtkinter.CTkButton(tela,
text="Registre-se", font=("Times",40),command=janela_registro,corner_radius=45,border_width=3,border_color="black",fg_color="#8690AF",text_color="white",width=570, height=90)
botao_registro_home.place(x=380, y=520)
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

logo_login = customtkinter.CTkLabel(frame_login, text=None, image=icone_vaca_login).place(x=600,y=60)

texto_login = customtkinter.CTkLabel(frame_login, text="Fazer login", text_color="#607D8B", font=("times", 45))
texto_login.place(x=570, y=200)

entrada_email_login = customtkinter.CTkEntry(frame_login, 
                               placeholder_text="Digite seu usuário",
                               placeholder_text_color="black",
                               border_color="black",
                                border_width=3,
                                text_color="black", fg_color="#FFDA8F",
                                corner_radius=45,
                                width=370, height=55, font=("Times",20))
entrada_email_login.place(x=500, y=280)

entrada_senha_login = customtkinter.CTkEntry(frame_login,
                                placeholder_text="Digite sua senha",
                                placeholder_text_color="black",
                                border_color="black",
                                border_width=3,
                                  text_color="black", fg_color="#FFDA8F",
                                    width=370, height=55,
                                    corner_radius=45,
                                      font=("Times",20),
                                        show="*")
entrada_senha_login.place(x=500, y=350)

botao_login = customtkinter.CTkButtonbotao_login = customtkinter.CTkButton(frame_login,
                                      border_width=2,
                                     border_color="black",
                                      corner_radius=45,
                                       text="Entrar",
                                     fg_color="#FF9EB1",
                                      text_color="black",
                                     command=Continuar_login_to_principal,)
botao_login.place(x=730, y=450)

botao_voltar_login = customtkinter.CTkButton(frame_login,
                                             border_width=2,
                                             border_color="black",
                                              text="Voltar",
                                              fg_color="#FF9EB1",
                                              corner_radius=45,
                                              text_color="black",command=volta__login_to_home)
botao_voltar_login.place(x=500, y=450)

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

label_icone_registro = customtkinter.CTkLabel(master=frame_registro, text="", image=icone_vaca_home)
label_icone_registro.place(x=50, y=2)

botao_continuar_registo = customtkinter.CTkButton(frame_registro, text="Continuar", fg_color="#FFDA8F", text_color="black", command=volta_registro_to_home)
botao_continuar_registo.place(x=1150, y=650)

botao_voltar_registro = customtkinter.CTkButton(frame_registro,
                        text= None,
                        fg_color="#FF9EB1",
                        width=80,
                        height=60,
                        corner_radius=45,
                        border_width=3,
                        border_color="black",
                        image=img_botao_voltar,
                        command=volta_registro_to_home)
botao_voltar_registro.place(x=60, y=650)#Botão com função de voltar pra tela inicial

entradra_nome_registro = customtkinter.CTkEntry(frame_registro, placeholder_text="Nome", text_color="black", fg_color="#FFDA8F", width=370, height=35, font=("times",40), corner_radius=200)
entradra_nome_registro.place(x=320, y=100)

entrada_idade_registro = customtkinter.CTkEntry(frame_registro, placeholder_text="Idade", text_color="black", fg_color="#FF9EB1", width=370, height=35, font=("times",40), corner_radius=200)
entrada_idade_registro.place(x=60, y=250)

entrada_profissao_registro = customtkinter.CTkEntry(frame_registro, placeholder_text="Profissão", text_color="black", fg_color="#FFDA8F", width=370, height=35, font=("times",40), corner_radius=200)
entrada_profissao_registro.place(x=60, y=350)

entrada_celular_registro = customtkinter.CTkEntry(frame_registro, placeholder_text="Celular", text_color="black", fg_color="#FF9EB1", width=370, height=35, font=("times",40), corner_radius=200)
entrada_celular_registro.place(x=60, y=450)

entrada_email_registro = customtkinter.CTkEntry(frame_registro, placeholder_text="Email", text_color="black", fg_color="#FFDA8F", width=370, height=35, font=("times",40), corner_radius=200)
entrada_email_registro.place(x=60, y=550)

entrada_comentarios_registro = customtkinter.CTkTextbox(frame_registro, fg_color="#607D8B",width=500, height=390).place(x=550, y=260)
opcional= customtkinter.CTkTextbox(frame_registro,width=500,height=395,fg_color="white").place(x=540,y=240)

botao_arquivo_registro = customtkinter.CTkButton(frame_registro, command=abre_arquivo, text="", fg_color="#607D8B", width=150, height=150, corner_radius=200)
botao_arquivo_registro.place(x=825, y=70)
#----------------------------------------------

#Declarando Funcoes de Botao da tela principal

def botao_voltar_principal():
    frame_principal.pack_forget()
    frame_login.pack(fill="both", expand=True)


def botao_cadastrar_animal():
    frame_principal.pack_forget()
    frame_cadastrar_animal.pack(fill="both", expand=True)

def botao_acessar_curral():
    frame_principal.pack_forget()
    frame_acessar_curral.pack(fill="both", expand=True)

def botao_acessar_perfil():
    frame_principal.pack_forget()
    frame_perfil.pack(fill="both", expand=True)

#Criando Frames Principal
frame_principal = customtkinter.CTkFrame(master=tela, fg_color="#CFD8DC")

Toplevel_verificar_saida = customtkinter.CTkToplevel(frame_principal, fg_color="#CFD8DC")
Toplevel_verificar_saida.destroy()

icon_vaca_principal = customtkinter.CTkLabel(master=frame_principal, text="", image=icone_vaca_home)
icon_vaca_principal.pack()

titulo_rumizone_principal= customtkinter.CTkLabel(frame_principal,fg_color="transparent",text="RUMIZONE",font=("Times", 64),width=660,height=108,text_color="#607D8B")
titulo_rumizone_principal.place(x=350,y=250)

botao_cadastrar_animal= customtkinter.CTkButton(frame_principal,text="cadastrar\n animal",text_color="black",font=("Times", 20),fg_color="#8690AF",width=300,height=180,corner_radius= 45,border_width=3,border_color="black",image= img_vaquinha,command=botao_cadastrar_animal)
botao_cadastrar_animal.place(x=140, y=400)

botao_acessar_curral= customtkinter.CTkButton(frame_principal,text="Entrar no curral",text_color="black",font=("Times", 20),fg_color="#FF9EB1",width=300,height=180,corner_radius= 45,border_width=3,border_color="black",image= img_cerca,command=botao_acessar_curral)
botao_acessar_curral.place(x=550, y=400)

botao_acessar_perfil= customtkinter.CTkButton(frame_principal,text="Ir para o Perfil",text_color="black",font=("Times", 20),fg_color="#FFDA8F",width=300,height=180,corner_radius= 45,border_width=3,border_color="black",image= img_fazendeiro)
botao_acessar_perfil.place(x=960, y=400)

botao_voltar = customtkinter.CTkButton(frame_principal,
                        text= None,
                        fg_color="#FF9EB1",
                        width=60,
                        height=40,
                        corner_radius=45,
                        border_width=3,
                        border_color="black",
                        image=img_botao_voltar,
                        command=botao_voltar_principal)
botao_voltar.place(x=60, y=620)
#----------------------------------------------

#Declarando Funcoes de Botao da tela cadastrar animal

def botao_voltar_cadastrar_animal():
    frame_cadastrar_animal.pack_forget()
    frame_principal.pack(fill="both", expand=True)

def botao_continuar_cadastrar_animal():
    frame_cadastrar_animal.pack_forget()
    frame_principal.pack(fill="both", expand=True)

#Criando Frames Cadastrar Animal
frame_cadastrar_animal = customtkinter.CTkFrame(master=tela, fg_color="#CFD8DC")

img_vaca_cadastro_animal = customtkinter.CTkLabel(frame_cadastrar_animal, text="", image=img_vaca_cadastro)
img_vaca_cadastro_animal.place(x=60, y=35)

botao_voltar_cadastrar_animal = customtkinter.CTkButton(frame_cadastrar_animal,
                        text= None,
                        fg_color="#FF9EB1",
                        width=80,
                        height=60,
                        corner_radius=45,
                        border_width=3,
                        border_color="black",
                        image=img_botao_voltar,
                        command=botao_voltar_cadastrar_animal)
botao_voltar_cadastrar_animal.place(x=60, y=620)

checkbox_leite = customtkinter.CTkCheckBox(frame_cadastrar_animal,text=None,checkbox_height=30,checkbox_width=30,fg_color="#B8EB7C",checkmark_color="black",border_width=3,border_color="black")
checkbox_leite.place(x=1060,y=345)

checkbox_abate= customtkinter.CTkCheckBox(frame_cadastrar_animal,text=None,checkbox_height=30,checkbox_width=30,fg_color="#B8EB7C",checkmark_color="black",border_width=3,border_color="black")
checkbox_abate.place(x=1060, y=470)

checkbox_gravidez = customtkinter.CTkCheckBox(frame_cadastrar_animal,text=None,checkbox_height=30,checkbox_width=30,fg_color="#B8EB7C",checkmark_color="black",border_width=3,border_color="black")
checkbox_gravidez.place(x=1060,y=220)

checkbox_femea = customtkinter.CTkCheckBox(frame_cadastrar_animal,text=None,checkbox_height=30,checkbox_width=30,fg_color="#FF9EB1",checkmark_color="black",border_width=3,border_color="black")

checkbox_macho = customtkinter.CTkCheckBox(frame_cadastrar_animal,text=None,checkbox_height=30,checkbox_width=30,fg_color="#00BCD4",checkmark_color="black",border_width=3,border_color="black")

img_feto_cadastro_animal = customtkinter.CTkLabel(frame_cadastrar_animal, text="", image=img_feto)
img_feto_cadastro_animal.place(x=970, y=220)

img_leite_cadastro_animal = customtkinter.CTkLabel(frame_cadastrar_animal, text="", image=img_leite)
img_leite_cadastro_animal.place(x=970, y=345)

img_carne_cadastro_animal = customtkinter.CTkLabel(frame_cadastrar_animal, text="", image=img_carne)
img_carne_cadastro_animal.place(x=970, y=470)

img_sexo = customtkinter.CTkLabel(frame_cadastrar_animal, text="", image=img_genders)
img_sexo.place(x=515, y=130)

entrada_pelagem_cadastro_animal = customtkinter.CTkEntry(frame_cadastrar_animal,corner_radius=45,placeholder_text="Pelagem:",placeholder_text_color="black",font=("Times", 30),width=270,height=75,border_width=3,border_color="black",fg_color="#8690AF").place(x=305,y=265)

entrada_idade_cadastro_animal = customtkinter.CTkEntry(frame_cadastrar_animal,corner_radius=45,placeholder_text="Idade:",placeholder_text_color="black",font=("Times", 30),width=270,height=75,border_width=3,border_color="black",fg_color="#FF9EB1").place(x=305, y=395)

entrada_imagem_vaca_cadastro_animal = customtkinter.CTkButton(frame_cadastrar_animal,text="",width=150, height=150, fg_color="#607D8B", corner_radius=220,border_color="black",border_width=3,command=abre_arquivo)
entrada_imagem_vaca_cadastro_animal.place(x=306, y=35)

entrada_peso_cadastro_animal = customtkinter.CTkEntry(frame_cadastrar_animal,corner_radius=45,placeholder_text="Peso - Kg:",placeholder_text_color="black",font=("Times", 30),width=270,height=75,border_width=3,border_color="black",fg_color="#8690AF").place(x=305, y=520)

entrada_produção_cadastro_animal = customtkinter.CTkEntry(frame_cadastrar_animal,corner_radius=45,placeholder_text="Produção:",placeholder_text_color="black",font=("Times", 30),width=270,height=75,border_width=3,border_color="black",fg_color="#FFDA8F").place(x=645, y=265)

entrada_nome_cadastro_animal = customtkinter.CTkEntry(frame_cadastrar_animal,corner_radius=45,placeholder_text="Nome:",placeholder_text_color="black",font=("Times", 30),width=270,height=75,border_width=3,border_color="black",fg_color="#FFDA8F").place(x=505, y=40)

entrada_cod_vaca_cadastro_animal = customtkinter.CTkEntry(frame_cadastrar_animal,corner_radius=45,placeholder_text="#Cód:",placeholder_text_color="black",font=("Times", 18),width=115,height=75,border_width=3,border_color="black",fg_color="#FF9EB1").place(x=805,y=40)

entrada_comentarios_cadastro_animal = customtkinter.CTkTextbox(frame_cadastrar_animal, fg_color="#607D8B",width=260, height=210,text_color="black").place(x=650, y=390)
opcional= customtkinter.CTkTextbox(frame_cadastrar_animal,width=260,height=215,fg_color="white").place(x=640,y=370)

botao_enviar_cadastro_animal = customtkinter.CTkButton(frame_cadastrar_animal,text="Enviar",fg_color="#FFDA8F",text_color="black",font=("Times", 30),width=270,height=75,corner_radius=45,border_width=3,border_color="black",command=botao_continuar_cadastrar_animal)
botao_enviar_cadastro_animal.place(x=900, y=620)

#----------------------------------------------

#Declarando Funcoes de Botao da tela acessar curral

def botao_voltar_acessar_curral():
    frame_acessar_curral.pack_forget()
    frame_principal.pack(fill="both", expand=True)

def botao_acessar_perfil_vaca():
    frame_acessar_curral.pack_forget()
    frame_perfil_vaca.pack(fill="both", expand=True)
    
def botao_cadastrar_animal_curral():
    frame_acessar_curral.pack_forget()
    frame_cadastrar_animal.pack(fill="both", expand=True)


#Criando Frames Acessar Curral

frame_acessar_curral = customtkinter.CTkFrame(master=tela, fg_color="#CFD8DC")

barra_lateral_curral = customtkinter.CTkFrame(frame_acessar_curral,fg_color="#607D8B",
                width=430,
                height=720)
barra_lateral_curral.place(x=0,y=0)

curral = customtkinter.CTkLabel(barra_lateral_curral,width=380,height=140,corner_radius=45,fg_color="#FF9EB1",text="CURRAL",text_color="black",font=("Times", 30),image=img_cerca,compound=LEFT).place(x=20,y=25)

botao_voltar = customtkinter.CTkButton(barra_lateral_curral,text= None,fg_color="#FF9EB1",width=60,height=40,corner_radius=45,border_width=3,border_color="black",image=img_botao_voltar,command=botao_voltar_acessar_curral)
botao_voltar.place(x=60, y=620)

adicionar_vaca = customtkinter.CTkButton(barra_lateral_curral,fg_color="#FFDA8F",corner_radius=45,width=220,height=90,text="adicionar\nanimal",font=("Times", 20),image= img_vaquinha_lista,text_color="black",compound=LEFT,border_color="black",border_width=3,command=botao_cadastrar_animal_curral).place(x=120, y=200)

remover_vaca = customtkinter.CTkButton(barra_lateral_curral,fg_color="#FFDA8F",corner_radius=45,width=280,height=90,text="remover\nanimal",font=("Times", 20),image= img_lixo,text_color="black",compound=LEFT,border_color="black",border_width=3).place(x=120, y=300)

icone_leite= customtkinter.CTkLabel(frame_acessar_curral,
                      image=img_leite,
                      text=None).place(x=1060,y=70)

icone_carne= customtkinter.CTkLabel(frame_acessar_curral, 
                      image=img_carne,
                      text=None).place(x=1160, y=75)

nome_vaca= customtkinter.CTkButton(frame_acessar_curral,
                     text="Nome - #código",
                     fg_color="#8690AF",
                     font=("Times", 40),
                     corner_radius=45,
                     width=280,
                     height=90,
                     border_color="black",
                     border_width=3, command=botao_acessar_perfil_vaca).place(x=700,y=70)

perfil_vaca= customtkinter.CTkButton(frame_acessar_curral,
                       text=None,
                       hover=DISABLED , 
                      width=130,
                      height=130,
                      border_width=3,
                      border_color="black",
                      fg_color="#8690AF",
                      corner_radius=200, ).place(x=500,y=45)

#----------------------------------------------
#Declarando Funcoes de Botao da tela perfil

def botao_voltar_perfil():
    frame_perfil.pack_forget()
    frame_principal.pack(fill="both", expand=True)

def botao_continuar_perfil():
    frame_perfil.pack_forget()
    frame_principal.pack(fill="both", expand=True)

#Criando Frames Perfil

frame_perfil = customtkinter.CTkFrame(master=tela, fg_color="#CFD8DC")




#----------------------------------------------
#Declarando Funcoes de Botao da tela perfil vaca

def botao_voltar_perfil_vaca():
    frame_perfil_vaca.pack_forget()
    frame_acessar_curral.pack(fill="both", expand=True)

def curral_button():
    print("Clicou no botão curral")
    curral_toplevel = customtkinter.CTkToplevel(tela, fg_color="#CFD8DC")
    curral_toplevel.geometry("500x300")
    curral_toplevel.resizable(False, False)
    curral_toplevel.title("Curral")
    curral_toplevel.focus_force()
    curral_toplevel.grab_set()
    curral_toplevel.transient(tela)
    texto_curral_toplevel = customtkinter.CTkLabel(curral_toplevel, text="Curral", text_color="#607D8B", font=("Helvetica", 49)).place(x=175, y=10)

    text_numero_curral = customtkinter.CTkLabel(curral_toplevel, text="Número do curral", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=100)

    text1_numero_curral = customtkinter.CTkLabel(curral_toplevel, text="1", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=130)

    text_endereco_curral = customtkinter.CTkLabel(curral_toplevel, text="Endereço do curral", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=175)

    text1_endereco_curral = customtkinter.CTkLabel(curral_toplevel, text="Rua dos bobos, 0", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=200)

def cuidadores_button():
    print("Clicou no botão cuidadores")
    cuidadores_toplevel = customtkinter.CTkToplevel(tela, fg_color="#CFD8DC")
    cuidadores_toplevel.geometry("500x300")
    cuidadores_toplevel.resizable(False, False)
    cuidadores_toplevel.title("Cuidadores")
    cuidadores_toplevel.focus_force()
    cuidadores_toplevel.grab_set()
    cuidadores_toplevel.transient(tela)
    texto_cuidadores_toplevel = customtkinter.CTkLabel(cuidadores_toplevel, text="Cuidadores", text_color="#607D8B", font=("Helvetica", 49)).place(x=100, y=10)

    text_nome_cuidador = customtkinter.CTkLabel(cuidadores_toplevel, text="Nome do cuidador", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=100)
    text1_nome_cuidador = customtkinter.CTkLabel(cuidadores_toplevel, text="João Viscente", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=130)

    text_codigo_cuidador = customtkinter.CTkLabel(cuidadores_toplevel, text="Código do cuidador", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=175)
    text1_codigo_cuidador = customtkinter.CTkLabel(cuidadores_toplevel, text="123456789", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=200)

def alimentos_button():
    print("Clicou no botão alimentos")
    alimentos_toplevel = customtkinter.CTkToplevel(tela, fg_color="#CFD8DC")
    alimentos_toplevel.geometry("500x300")
    alimentos_toplevel.resizable(False, False)
    alimentos_toplevel.title("Alimentos")
    alimentos_toplevel.focus_force()
    alimentos_toplevel.grab_set()
    alimentos_toplevel.transient(tela)
    texto_alimentos_toplevel = customtkinter.CTkLabel(alimentos_toplevel, text="Alimentos", text_color="#607D8B", font=("Helvetica", 49)).place(x=100, y=10)

    text_nome_alimento = customtkinter.CTkLabel(alimentos_toplevel, text="Nome do alimento", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=100)
    
    text1_nome_alimento = customtkinter.CTkLabel(alimentos_toplevel, text="Ração", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=130)

    text_quantidade_alimento = customtkinter.CTkLabel(alimentos_toplevel, text="Quantidade do alimento", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=175)
    
    text1_quantidade_alimento = customtkinter.CTkLabel(alimentos_toplevel, text="10kg", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=200)

def historico_vacina_button():
    print("Clicou no botão histórico de vacinação")
    historico_vacina_toplevel = customtkinter.CTkToplevel(tela, fg_color="#CFD8DC")
    historico_vacina_toplevel.geometry("500x300")
    historico_vacina_toplevel.resizable(False, False)
    historico_vacina_toplevel.title("Histórico de vacinação")
    historico_vacina_toplevel.focus_force()
    historico_vacina_toplevel.grab_set()
    historico_vacina_toplevel.transient(tela)
    texto_historico_vacina_toplevel = customtkinter.CTkLabel(historico_vacina_toplevel, text="Histórico de vacinação", text_color="#607D8B", font=("Helvetica", 49)).place(x=25, y=10)

    text_nome_vacina = customtkinter.CTkLabel(historico_vacina_toplevel, text="Nome da vacina", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=100)
    
    text1_nome_vacina = customtkinter.CTkLabel(historico_vacina_toplevel, text="Vacina 1", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=130)

    text_data_vacina = customtkinter.CTkLabel(historico_vacina_toplevel, text="Data da vacina", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=175)
    
    text1_data_vacina = customtkinter.CTkLabel(historico_vacina_toplevel, text="01/01/2021", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=200)

def historico_doenca_button():
    print("Clicou no botão histórico de doenças")
    historico_doenca_toplevel = customtkinter.CTkToplevel(tela, fg_color="#CFD8DC")
    historico_doenca_toplevel.geometry("500x300")
    historico_doenca_toplevel.resizable(False, False)
    historico_doenca_toplevel.title("Histórico de doenças")
    historico_doenca_toplevel.focus_force()
    historico_doenca_toplevel.grab_set()
    historico_doenca_toplevel.transient(frame_principal)
    texto_historico_doenca_toplevel = customtkinter.CTkLabel(historico_doenca_toplevel, text="Histórico de doenças", text_color="#607D8B", font=("Helvetica", 49)).place(x=25, y=10)

    text_nome_doenca = customtkinter.CTkLabel(historico_doenca_toplevel, text="Nome da doença", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=100)
    
    text1_nome_doenca = customtkinter.CTkLabel(historico_doenca_toplevel, text="Doença 1", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=130)

    text_data_doenca = customtkinter.CTkLabel(historico_doenca_toplevel, text="Data da doença", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=175)
    
    text1_data_doenca = customtkinter.CTkLabel(historico_doenca_toplevel, text="01/01/2021", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=200)

def producao_button():
    print("Clicou no botão produção")
    producao_toplevel = customtkinter.CTkToplevel(tela, fg_color="#CFD8DC")
    producao_toplevel.geometry("500x300")
    producao_toplevel.resizable(False, False)
    producao_toplevel.title("Produção")
    producao_toplevel.focus_force()
    producao_toplevel.grab_set()
    producao_toplevel.transient(tela)
    texto_producao_toplevel = customtkinter.CTkLabel(producao_toplevel, text="Produção", text_color="#607D8B", font=("Helvetica", 49)).place(x=100, y=10)

    text_producao = customtkinter.CTkLabel(producao_toplevel, text="Produção", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=100)
    
    text1_producao = customtkinter.CTkLabel(producao_toplevel, text="10L", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=130)

    text_data_producao = customtkinter.CTkLabel(producao_toplevel, text="Data da produção", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=175)
    
    text1_data_producao = customtkinter.CTkLabel(producao_toplevel, text="01/01/2021", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=200)    


#Criando Frames Perfil Vaca

frame_perfil_vaca = customtkinter.CTkFrame(master=tela, fg_color="#CFD8DC")


frame_info_perfil_vaca = customtkinter.CTkLabel(frame_perfil_vaca, text="esse", text_color="black", font=("Helvetica", 11), width=292, height=401, fg_color="#FFDA8F", corner_radius=100)
frame_info_perfil_vaca.place(x=10, y=275)

img_vaca = customtkinter.CTkLabel(frame_perfil_vaca, width=200, height=200, fg_color="black", corner_radius=200, bg_color="#CFD8DC", text="")
img_vaca.place(x=60, y=20)

texto_nome = customtkinter.CTkButton(frame_perfil_vaca, text="-Creusa-\n #3321", text_color="black", font=("Times", 24), width=400, height=100, fg_color="#8690AF", corner_radius=100, border_color="black", border_width=3, hover=DISABLED)
texto_nome.place(x=330, y=20)

img_leite_perfil_vaca = customtkinter.CTkLabel(frame_perfil_vaca, text="", image=img_leite)
img_leite_perfil_vaca.place(x=800, y=25)

img_carne_perfil_vaca = customtkinter.CTkLabel(frame_perfil_vaca, text="", image=img_carne)
img_carne_perfil_vaca.place(x=900, y=35)

video_frame = customtkinter.CTkFrame(frame_perfil_vaca, width=900,border_width=3,border_color="black", height=500, fg_color="#FF9EB1", corner_radius=100)
video_frame.place(x=330, y=175)
button_player= customtkinter.CTkButton(video_frame,image=player, text=None, fg_color="#FF9EB1",hover=DISABLED).place(x=350,y=150,)

button_back = customtkinter.CTkButton(frame_perfil_vaca,border_width=3,border_color="black", text=None, fg_color="#FF9EB1", command=botao_voltar_perfil_vaca, corner_radius=100, width=50, height=50,image=img_botao_voltar)
button_back.place(x=1250, y=650)

button_curral = customtkinter.CTkButton(frame_info_perfil_vaca, text="Curral", fg_color="#FF9EB1", command=curral_button, border_width=1, corner_radius=100, width=50, height=50)
button_curral.place(x=105, y=10)

button_cuidadores = customtkinter.CTkButton(frame_info_perfil_vaca, text="Cuidadores", fg_color="#FF9EB1", command=cuidadores_button, border_width=1, corner_radius=100, width=50, height=50)
button_cuidadores.place(x=90, y=70)

button_alimentos = customtkinter.CTkButton(frame_info_perfil_vaca, text="Alimentos", fg_color="#FF9EB1", command=alimentos_button, border_width=1, corner_radius=100, width=50, height=50)
button_alimentos.place(x=95, y=130)

button_historico_vacina = customtkinter.CTkButton(frame_info_perfil_vaca, text="Histórico de vacinação", fg_color="#FF9EB1", command=historico_vacina_button, border_width=1, corner_radius=100, width=50, height=50)
button_historico_vacina.place(x=60, y=190)

button_hitorico_doenca = customtkinter.CTkButton(frame_info_perfil_vaca, text="Histórico de doenças", fg_color="#FF9EB1", command=historico_doenca_button, border_width=1, corner_radius=100, width=50, height=50)
button_hitorico_doenca.place(x=65, y=250)

button_producao = customtkinter.CTkButton(frame_info_perfil_vaca, text="Produção", fg_color="#FF9EB1", command=producao_button, border_width=1, corner_radius=100, width=50, height=50)
button_producao.place(x=95, y=310)

tela.mainloop()