from customtkinter import *
from PIL import Image

janela_inicial= CTk(fg_color="#CFD8DC") #nome da tela
janela_inicial.geometry("1360x720") #tamanho padrão do projeto
janela_inicial.resizable(False,False) #não permite o usuário redimensionar a tela
janela_inicial.title("Rumizone") #título do projeto 

#imagens em png do projeto (se nao funcionar encaixa o diretório do seu pc)
vaquinha= CTkImage(light_image=Image.open(r"imagens\vaquinha.png"),
                dark_image=Image.open(r"imagens\vaquinha.png"),
                size=(150, 90))
cerca= CTkImage(light_image=Image.open(r"imagens\cerca do curral.png"),
                dark_image=Image.open(r"imagens\cerca do curral.png"),
                size=(60, 60))

icone= CTkImage(light_image=Image.open(r"imagens\rumizone icone.png"), 
                dark_image=Image.open(r"imagens\rumizone icone.png"),
                size=(300, 320))

logo= CTkLabel(janela_inicial, text=None, 
               image=icone).pack()
titulo= CTkLabel(janela_inicial, 
                 fg_color="transparent",
                 text="RUMIZONE",
                 font=("Times", 64),
                 width=660,
                 height=108)
titulo.place(x=390,y=250)
#os botoes ainda tao sem a variavel command pra encaixar a função
botao1= CTkButton(janela_inicial, 
                  text="cadastrar animal",
                  text_color="black",
                  font=("Times", 20),
                  fg_color="#8690AF",
                  width=300,
                  height=180,
                  corner_radius= 45,
                  border_width=3,
                  border_color="black",
                  image= vaquinha)
botao1.pack(padx=15, pady=10)
botao1.place(x=139, y=400)

botao2= CTkButton(janela_inicial, 
                  text="criar curral",
                  text_color="black",
                  font=("Times", 20),
                  fg_color="#FF9EB1",
                  width=300,
                  height=180,
                  corner_radius= 45,
                  border_width=3,
                  border_color="black",
                  image= cerca)
botao2.pack(padx=10, pady=10)
botao2.place(x=575, y=400)

botao3= CTkButton(janela_inicial, 
                  text="entrar em um curral",
                  text_color="black",
                  font=("Times", 20),
                  fg_color="#FFDA8F",
                  width=300,
                  height=180,
                  corner_radius= 45,
                  border_width=3,
                  border_color="black",
                  image= cerca)
botao3.pack(padx=10, pady=10)
botao3.place(x=1011, y=400)

janela_inicial.mainloop()
