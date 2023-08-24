from customtkinter import *
from PIL import Image

tela_perfil= CTk(fg_color="#CFD8DC") #nome da tela
tela_perfil.geometry("1360x720") #tamanho padrão do projeto
tela_perfil.resizable(False,False) #não permite o usuário redimensionar a tela
tela_perfil.title("Rumizone") #título do projeto 

#rodando as imagens pra poder inserir depois
caneta= CTkImage(light_image=Image.open(r"imagens\caneta.png"),
                dark_image=Image.open(r"imagens\caneta.png"),
                size=(60, 60))

fazendeiro= CTkImage(light_image=Image.open(r"imagens\fazendeiro.png"),
                dark_image=Image.open(r"imagens\fazendeiro.png"),
                size=(60, 60))

cerca= CTkImage(light_image=Image.open(r"imagens\cerca do curral.png"),
                dark_image=Image.open(r"imagens\cerca do curral.png"),
                size=(100, 100))
#colocando as coisa no lugar
img_funcionario = CTkLabel(tela_perfil,
                             width=180,
                             height=180,
                             fg_color="#607D8B",
                             corner_radius=200,
                             bg_color="#CFD8DC",
                             text="")
img_funcionario.place(x=120, y=35)
nome= CTkButton(tela_perfil,text_color="black",
                     text="Nome - #código",
                     fg_color="#FFDA8F",
                     font=("Times", 40),
                     corner_radius=45,
                     width=360,
                     height=120,
                     border_color="black",
                     border_width=3).place(x=420,y=120)
atividades= CTkButton(tela_perfil,text_color="black",
                     text="Atividades",
                     fg_color="#8690AF",
                     font=("Times", 40),
                     corner_radius=45,
                     width=320,
                     height=110,
                     image=caneta,
                     border_color="black",
                     compound=LEFT,
                     border_width=3).place(x=60,y=600)

botao_curral= CTkButton(tela_perfil, 
                  text="Entrar no curral",
                  text_color="black",
                  font=("Times", 20),
                  fg_color="#FFDA8F",
                  width=320,
                  height=290,
                  corner_radius= 45,
                  compound=TOP,
                  border_width=3,
                  border_color="black",
                  image= cerca)
botao_curral.place(x=60, y=260)

fundo_opcional= CTkFrame(tela_perfil, fg_color="#607D8B",width=250, height=205).place(x=850, y=50)
opcional= CTkTextbox(tela_perfil,width=240,height=195).place(x=840,y=40)

display_frame= CTkFrame(tela_perfil,
                        fg_color="#607D8B",
                        border_color="black",
                        border_width=3,
                        corner_radius=45,
                        width=830, height=400).place(x=420,y=260)
tela_perfil.mainloop()