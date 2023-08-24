import customtkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def escolher_imagem():
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")])
    if filepath:
        imagem = Image.open(filepath)
        imagem.thumbnail((292, 480))  # Redimensionar a imagem para o tamanho desejado
        imagem = ImageTk.PhotoImage(imagem)
        label_imagem.configure(image=imagem)
        label_imagem.image = imagem

def voltar_para_inicio(frame_atual):
    frame_atual.pack_forget()
    frame_inicio.pack()

def clique():
    print("Fazer login")

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
iconevaca_login = customtkinter.CTkImage(light_image=Image.open(r"imagens\rumizone icone.png"),
                                   dark_image=Image.open(r"imagens\rumizone icone.png"),
                                   size=(150,158))
iconevaca = customtkinter.CTkImage(light_image=Image.open(r"imagens\rumizone icone.png"),
                                   dark_image=Image.open(r"imagens\rumizone icone.png"),
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

frame_login = customtkinter.CTkFrame(master=tela, fg_color="#CFD8DC")
frame_registro = customtkinter.CTkFrame(tela, fg_color="#CFD8DC")

#Frame/Tela de login
logo_login= customtkinter.CTkLabel(frame_login, text=None,
                                    image=iconevaca_login).place(x=600,y=60)
texto_login = customtkinter.CTkLabel(frame_login, text="Fazer login", text_color="#607D8B", font=("Helvetica", 45))
texto_login.place(x=570, y=200)
email = customtkinter.CTkEntry(frame_login, 
                               placeholder_text="Digite seu usuário",
                               placeholder_text_color="black",
                               border_color="black",
                                border_width=3,
                                text_color="black", fg_color="#FFDA8F",
                                corner_radius=45,
                                width=370, height=55, font=("Times",20))
email.place(x=500, y=280)
senha = customtkinter.CTkEntry(frame_login,
                                placeholder_text="Digite sua senha",
                                placeholder_text_color="black",
                                border_color="black",
                                border_width=3,
                                  text_color="black", fg_color="#FFDA8F",
                                    width=370, height=55,
                                    corner_radius=45,
                                      font=("Times",20),
                                        show="*")
senha.place(x=500, y=350)
botao_login = customtkinter.CTkButton(frame_login,
                                      border_width=2,
                                     border_color="black",
                                      corner_radius=45,
                                       text="Entrar",
                                     fg_color="#FF9EB1",
                                      text_color="black",
                                     command=clique)
botao_login.place(x=730, y=450)
botao_voltar_login = customtkinter.CTkButton(frame_login,
                                             border_width=2,
                                             border_color="black",
                                              text="Voltar",
                                              fg_color="#FF9EB1",
                                              corner_radius=45,
                                              text_color="black",
                                                command=lambda: voltar_para_inicio(frame_login))
botao_voltar_login.place(x=500, y=450)#Botão com função de voltar pra tela inicial

tela.mainloop()