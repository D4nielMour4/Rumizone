import customtkinter  # Importa o módulo customtkinter
from tkinter import *  # Importa o módulo tkinter
from PIL import Image  # Importa o módulo Image do PIL

#Iniciando a tela e os frames Principais
tela = customtkinter.CTk()  # Cria a tela
tela.geometry("1360x720")  # Define o tamanho da tela
tela.resizable(False, False)  # Impede que a tela seja redimensionada

frame_inicio = customtkinter.CTkFrame(tela, fg_color="black")

frame_info_vaca = customtkinter.CTkFrame(tela, fg_color="#CFD8DC")
frame_info_vaca.pack(fill="both", expand=True)

#Definindo Funções dos botões
def clique():
    print("Voltar para a tela inicial")
    frame_info_vaca.pack_forget()
    frame_inicio.pack()
    
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

#Definindo Labels e Botões    
texto_info = customtkinter.CTkLabel(frame_info_vaca, text="", text_color="black", font=("Helvetica", 11), width=292, height=401, fg_color="#FFDA8F", corner_radius=100)
texto_info.place(x=10, y=275)

player= customtkinter.CTkImage(light_image=Image.open(r"imagens\player.png"),
                dark_image=Image.open(r"imagens\player.png"),
                size=(205, 205))
carne= customtkinter.CTkImage(light_image=Image.open(r"imagens\carne.png"),
                dark_image=Image.open(r"imagens\carne.png"),
                size=(80, 70))
leite= customtkinter.CTkImage(light_image=Image.open(r"imagens\caixa de leite.png"),
                dark_image=Image.open(r"imagens\caixa de leite.png"),
                size=(75, 85))
voltar= customtkinter.CTkImage(light_image=Image.open(r"imagens\voltar.png"),
                dark_image=Image.open(r"imagens\voltar.png"),
                size=(20, 20))
img_vaca = customtkinter.CTkLabel(frame_info_vaca, width=200, height=200, fg_color="black", corner_radius=200, bg_color="#CFD8DC", text="")
img_vaca.place(x=60, y=20)

texto_nome = customtkinter.CTkButton(frame_info_vaca, text="-Creusa-\n #3321", text_color="black", font=("Times", 24), width=400, height=100, fg_color="#8690AF", corner_radius=100, border_color="black", border_width=3, hover=DISABLED)
texto_nome.place(x=330, y=20)

img_leite = customtkinter.CTkLabel(frame_info_vaca,image=leite, text="")
img_leite.place(x=800, y=25)

img_carne = customtkinter.CTkLabel(frame_info_vaca,image=carne ,text="")
img_carne.place(x=900, y=35)

video_frame = customtkinter.CTkFrame(frame_info_vaca, width=900,border_width=3,border_color="black", height=500, fg_color="#FF9EB1", corner_radius=100)
video_frame.place(x=330, y=175)
button_player= customtkinter.CTkButton(video_frame,image=player, text=None, fg_color="#FF9EB1",hover=DISABLED).place(x=350,y=150,)

button_back = customtkinter.CTkButton(frame_info_vaca,border_width=3,border_color="black", text=None, fg_color="#FF9EB1", command=clique, corner_radius=100, width=50, height=50,image=voltar)
button_back.place(x=1250, y=650)

button_curral = customtkinter.CTkButton(texto_info, text="Curral", fg_color="#FF9EB1", command=curral_button, border_width=1, corner_radius=100, width=50, height=50)
button_curral.place(x=105, y=10)

button_cuidadores = customtkinter.CTkButton(texto_info, text="Cuidadores", fg_color="#FF9EB1", command=cuidadores_button, border_width=1, corner_radius=100, width=50, height=50)
button_cuidadores.place(x=90, y=70)

button_alimentos = customtkinter.CTkButton(texto_info, text="Alimentos", fg_color="#FF9EB1", command=alimentos_button, border_width=1, corner_radius=100, width=50, height=50)
button_alimentos.place(x=95, y=130)

button_historico_vacina = customtkinter.CTkButton(texto_info, text="Histórico de vacinação", fg_color="#FF9EB1", command=historico_vacina_button, border_width=1, corner_radius=100, width=50, height=50)
button_historico_vacina.place(x=60, y=190)

button_hitorico_doenca = customtkinter.CTkButton(texto_info, text="Histórico de doenças", fg_color="#FF9EB1", command=historico_doenca_button, border_width=1, corner_radius=100, width=50, height=50)
button_hitorico_doenca.place(x=65, y=250)

button_producao = customtkinter.CTkButton(texto_info, text="Produção", fg_color="#FF9EB1", command=producao_button, border_width=1, corner_radius=100, width=50, height=50)
button_producao.place(x=95, y=310)


tela.mainloop()  # Inicia a tela