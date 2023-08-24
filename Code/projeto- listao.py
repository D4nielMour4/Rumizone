from customtkinter import *
from PIL import Image

tela_lista= CTk(fg_color="#CFD8DC") #nome da tela
tela_lista.geometry("1360x720") #tamanho padrão do projeto
tela_lista.resizable(False,False) #não permite o usuário redimensionar a tela
tela_lista.title("Rumizone") #título do projeto 

leite= CTkImage(light_image=Image.open(r"imagens\caixa de leite.png"),
                dark_image=Image.open(r"imagens\caixa de leite.png"),
                size=(75, 85))

carne= CTkImage(light_image=Image.open(r"imagens\carne.png"),
                dark_image=Image.open(r"imagens\carne.png"),
                size=(80, 70))

lixo=CTkImage(light_image=Image.open(r"imagens\lata de lixo.png"),
                dark_image=Image.open(r"imagens\lata de lixo.png"),
                size=(70, 70))
vaquinha= CTkImage(light_image=Image.open(r"imagens\vaquinha.png"),
                dark_image=Image.open(r"imagens\vaquinha.png"),
                size=(100, 70))
cerca= CTkImage(light_image=Image.open(r"imagens\cerca do curral.png"),
                dark_image=Image.open(r"imagens\cerca do curral.png"),
                size=(60, 60))

icone= CTkImage(light_image=Image.open(r"imagens\rumizone icone.png"), 
                dark_image=Image.open(r"imagens\rumizone icone.png"),
                size=(300, 320))
voltar= CTkImage(light_image=Image.open(r"imagens\voltar.png"),
                dark_image=Image.open(r"imagens\voltar.png"),
                size=(20, 20))

barra= CTkFrame(tela_lista,fg_color="#607D8B",
                width=430,
                height=720)
barra.place(x=0,y=0)  
#barra lateral
curral= CTkLabel(barra,
                 width=380,
                 height=140,
                 corner_radius=45,
                 fg_color="#FF9EB1",
                 text="CURRAL",
                 text_color="black",
                 font=("Times", 30),
                 image=cerca,
                 compound=LEFT).place(x=20,y=25)

botao_voltar= CTkButton(barra,
                        text= None,
                        fg_color="#FF9EB1",
                        width=60,
                        height=40,
                        corner_radius=45,
                        border_width=3,
                        border_color="black",
                        image=voltar)
botao_voltar.place(x=60, y=620)

adicionar_vaca= CTkButton(barra,
                        fg_color="#FFDA8F",
                        corner_radius=45,
                        width=220,
                        height=90,
                        text="adicionar\nanimal",
                        font=("Times", 20),
                        image= vaquinha,
                        text_color="black",
                        compound=LEFT,
                        border_color="black",
                        border_width=3).place(x=120, y=200)
remover_vaca=CTkButton(barra,
                        fg_color="#FFDA8F",
                        corner_radius=45,
                        width=280,
                        height=90,
                        text="remover\nanimal",
                        font=("Times", 20),
                        image= lixo,
                        text_color="black",
                        compound=LEFT,
                        border_color="black",
                        border_width=3).place(x=120, y=300)
#lista de vacas
#ícones que indicam as condições das vaquinhas (leite e carne)
icone_leite= CTkLabel(tela_lista,
                      image=leite,
                      text=None).place(x=1060,y=70)
icone_carne= CTkLabel(tela_lista, 
                      image=carne,
                      text=None).place(x=1160, y=75)

#quero que clicar no nome da vaca leve até a tela de perfil
nome_vaca= CTkButton(tela_lista,
                     text="Nome - #código",
                     fg_color="#8690AF",
                     font=("Times", 40),
                     corner_radius=45,
                     width=280,
                     height=90,
                     border_color="black",
                     border_width=3).place(x=700,y=70)
perfil_vaca= CTkButton(tela_lista,
                       text=None,
                       hover=DISABLED , 
                      width=130,
                      height=130,
                      border_width=3,
                      border_color="black",
                      fg_color="#8690AF",
                      corner_radius=200, ).place(x=500,y=45)



tela_lista.mainloop()
