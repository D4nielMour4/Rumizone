from customtkinter import *
from PIL import Image
from tkinter import filedialog 


cadastro_vacas= CTk(fg_color="#CFD8DC") #nome da tela 
cadastro_vacas.geometry("1360x720") #tamanho padrão do projeto
cadastro_vacas.resizable(False,False) #não permite o usuário redimensionar a tela
cadastro_vacas.title("Rumizone") #título do projeto 

#barra= CTkFrame(cadastro_vacas, fg_color="#607D8B",width=250, height=720).place(x=0)
icone= CTkImage(light_image=Image.open(r"C:\Users\Seabroso\Documents\GitHub\Rumizone\imagens\rumizone icone.png"), 
                dark_image=Image.open(r"C:\Users\Seabroso\Documents\GitHub\Rumizone\imagens\rumizone icone.png"),
                size=(200, 180))

carne= CTkImage(light_image=Image.open(r"C:\Users\Seabroso\Documents\GitHub\Rumizone\imagens\carne.png"),
                dark_image=Image.open(r"C:\Users\Seabroso\Documents\GitHub\Rumizone\imagens\carne.png"),
                size=(60, 60))

leite= CTkImage(light_image=Image.open(r"C:\Users\Seabroso\Documents\GitHub\Rumizone\imagens\caixa de leite.png"),
                dark_image=Image.open(r"C:\Users\Seabroso\Documents\GitHub\Rumizone\imagens\caixa de leite.png"),
                size=(60, 60))

feto= CTkImage(light_image=Image.open(r"C:\Users\Seabroso\Documents\GitHub\Rumizone\imagens\feto.png"),
                dark_image=Image.open(r"C:\Users\Seabroso\Documents\GitHub\Rumizone\imagens\feto.png"),
                size=(60, 60))

genders= CTkImage(light_image=Image.open(r"C:\Users\Seabroso\Documents\GitHub\Rumizone\imagens\genders.png"),
                dark_image=Image.open(r"C:\Users\Seabroso\Documents\GitHub\Rumizone\imagens\genders.png"),
                size=(60, 50))
voltar= CTkImage(light_image=Image.open(r"C:\Users\Seabroso\Documents\GitHub\Rumizone\imagens\botao voltar.png"),
                dark_image=Image.open(r"C:\Users\Seabroso\Documents\GitHub\Rumizone\imagens\botao voltar.png"),
                size=(25, 25))

botao_voltar= CTkButton(cadastro_vacas,
                        text= None,
                        fg_color="#FF9EB1",
                        width=80,
                        height=60,
                        corner_radius=45,
                        border_width=3,
                        border_color="black",
                        image=voltar)
botao_voltar.place(x=60, y=620)

imagem_vaca = CTkButton(cadastro_vacas,
                     text="add\nimage",
                    width=150, 
                    height=150, 
                    fg_color="#607D8B", 
                    corner_radius=220,
                    border_color="black",
                     border_width=3 )
imagem_vaca.place(x=306, y=35)
# 3 checkbox pro cadastro das vaquinha
checkbox_leite= CTkCheckBox(cadastro_vacas,text=None,
                            checkbox_height=30,
                            checkbox_width=30,
                            fg_color="#B8EB7C",
                            checkmark_color="black",
                            border_color="black",
                            border_width=3,
                            ).place(x=1060,y=345)
checkbox_abate= CTkCheckBox(cadastro_vacas,text=None,
                            checkbox_height=30,
                            checkbox_width=30,
                            fg_color="#B8EB7C",
                            checkmark_color="black",
                            border_color="black",
                            border_width=3,).place(x=1060, y=470)
checkbox_gravidez= CTkCheckBox(cadastro_vacas,text=None,
                            checkbox_height=30,
                            checkbox_width=30,
                            fg_color="#B8EB7C",
                            checkmark_color="black",
                            border_color="black",
                            border_width=3,).place(x=1060,y=220)
# 2 checkbox que vão ser do sexo da vaca
femea=CTkCheckBox(cadastro_vacas,text=None,
                            checkbox_height=30,
                            checkbox_width=30,
                            fg_color="#FF9EB1",
                            checkmark_color="black",
                            border_color="black",
                            border_width=3,
                            ).place(x=595,y=140)
macho=CTkCheckBox(cadastro_vacas,text=None,
                            checkbox_height=30,
                            checkbox_width=30,
                            fg_color="#00BCD4",
                            checkmark_color="black",
                            border_color="black",
                            border_width=3,
                            ).place(x=630,y=140)

#labels pra conseguir usar as imagens
logo= CTkLabel(cadastro_vacas, text=None, 
               image=icone, bg_color="transparent", fg_color="transparent").place(x=60, y=35)

fetobox= CTkLabel(cadastro_vacas, text=None,
                  image=feto).place(x=970, y=220)

leitebox= CTkLabel(cadastro_vacas, text=None,
                   image=leite).place(x=970, y=345)
carnebox= CTkLabel(cadastro_vacas, text=None,
                   image=carne).place(x=970, y=470)
sexo=  CTkLabel(cadastro_vacas, text=None,
                   image=genders).place(x=515, y=130)

#entrys para as informações da vaquinha
pelagem= CTkEntry(cadastro_vacas,
                  corner_radius=45,
                  placeholder_text="Pelagem:",
                  placeholder_text_color="black",
                  font=("Times", 30),
                  width=270,
                  height=75,
                  border_width=3,
                  border_color="black",
                  fg_color="#8690AF").place(x=305,y=265)
idade= CTkEntry(cadastro_vacas,
                corner_radius=45,
                  placeholder_text="Idade:",
                  placeholder_text_color="black",
                  font=("Times", 30),
                  width=270,
                  height=75,
                  border_width=3,
                  border_color="black",
                  fg_color="#FF9EB1").place(x=305, y=395)
peso= CTkEntry(cadastro_vacas,
               corner_radius=45,
                  placeholder_text="Peso - Kg:",
                  placeholder_text_color="black",
                  font=("Times", 30),
                  width=270,
                  height=75,
                  border_width=3,
                  border_color="black",
                  fg_color="#8690AF").place(x=305, y=520)
produção= CTkEntry(cadastro_vacas,
                   corner_radius=45,
                  placeholder_text="Produção:",
                  placeholder_text_color="black",
                  font=("Times", 30),
                  width=270,
                  height=75,
                  border_width=3,
                  border_color="black",
                  fg_color="#FFDA8F").place(x=645, y=265)
nome= CTkEntry(cadastro_vacas,
               corner_radius=45,
                  placeholder_text="Nome:",
                  placeholder_text_color="black",
                  font=("Times", 30),
                  width=270,
                  height=75,
                  border_width=3,
                  border_color="black",
                  fg_color="#FFDA8F").place(x=505, y=40)
codvaca= CTkEntry(cadastro_vacas,
                  corner_radius=45,
                  placeholder_text="#Cód:",
                  placeholder_text_color="black",
                  font=("Times", 18),
                  width=115,
                  height=75,
                  border_width=3,
                  border_color="black",
                  fg_color="#FF9EB1").place(x=805,y=40)

fundo_opcional= CTkFrame(cadastro_vacas, fg_color="#607D8B",width=260, height=210).place(x=650, y=390)
opcional= CTkTextbox(cadastro_vacas,width=260,
                     height=215).place(x=640,y=370)
cadastro_vacas.mainloop()