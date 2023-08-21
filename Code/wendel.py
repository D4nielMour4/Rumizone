import customtkinter
from tkinter import *
from  PIL import Image

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
    frame_login.pack(fill="both", expand=True)# Fazer com que o frame ocupe a tela inteira

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

#Frame/Tela inicial

iconevaca = customtkinter.CTkImage(light_image=Image.open(r"C:\Users\wende\OneDrive\Documentos\GitHub\Rumizone\Code\fodase.png"),
                                   dark_image=Image.open(r"C:\Users\wende\OneDrive\Documentos\GitHub\Rumizone\Code\fodase.png"),
                                   size=(250,320))
Label = customtkinter.CTkLabel(master=tela, text="", image=iconevaca)
Label.place(x=530, y=50)
texto = customtkinter.CTkLabel(tela, text="Rumizone", text_color="#607D8B", font=("Robot", 49))
texto.place(x=560, y=250)
texto1 = customtkinter.CTkLabel(tela, text="Monitoramento e comportamento animal", text_color="#607D8B", font=("Helvetica", 20))
texto1.place(x=480, y=310)
botao1 = customtkinter.CTkButton(tela, text="Login", font=("Helvetica",40), command=janela_login, fg_color="#8690AF",text_color="white", width=370, height=70)
botao1.place(x=480, y=350)
botao2 = customtkinter.CTkButton(tela, text="Registre-se", font=("Helvetica",40), command=janela_registro, fg_color="#8690AF",text_color="white", width=370, height=70)
botao2.place(x=480, y=440)

# Frames
frame_login = customtkinter.CTkFrame(master= tela, fg_color="#CFD8DC")
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
texto_registro = customtkinter.CTkLabel(frame_registro, text="Registrar-se", text_color="#607D8B", font=("Helvetica", 70))
texto_registro.place(x=491, y=180)
email_registro = customtkinter.CTkEntry(frame_registro, placeholder_text="Digite seu novo usuário", text_color="black", fg_color="white", width=370, height=35, font=("Helvetica",20))
email_registro.place(x=500, y=280)
senha_registro = customtkinter.CTkEntry(frame_registro, placeholder_text="Digite sua senha", text_color="black", fg_color="white", width=370, height=35, font=("Helvetica",20), show="*")
senha_registro.place(x=500, y=330)
botao_registro = customtkinter.CTkButton(frame_registro, text="Criar conta", fg_color="#8690AF", text_color="white", command=clique)
botao_registro.place(x=730, y=400)
botao_voltar_registro = customtkinter.CTkButton(frame_registro, text="Voltar",fg_color="#8690AF", command=lambda: voltar_para_inicio(frame_registro))
botao_voltar_registro.place(x=500, y=400)

tela.mainloop()