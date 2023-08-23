import customtkinter  

from tkinter import *  

 

#Iniciando a tela e os frames Principais

tela = customtkinter.CTk()  # Cria a tela

tela.geometry("1360x720")  # Define o tamanho da tela

tela.resizable(False, False)  # Impede que a tela seja redimensionada

 

frame_inicio = customtkinter.CTkFrame(tela, fg_color="black")

 

frame_info_func = customtkinter.CTkFrame(tela, fg_color="#CFD8DC")

frame_info_func.pack(fill="both", expand=True)

 

#Funções dos botões

def clique():

    print("Voltar para a tela inicial")

    frame_info_func.pack_forget()

    frame_inicio.pack()

   

def curral_button():

    print("Clicou no botão currais")

    curral_toplevel = customtkinter.CTkToplevel(tela, fg_color="#CFD8DC")

    curral_toplevel.geometry("500x300")

    curral_toplevel.resizable(False, False)

    curral_toplevel.title("Currais")

    curral_toplevel.focus_force()

    curral_toplevel.grab_set()

    curral_toplevel.transient(tela)

    texto_curral_toplevel = customtkinter.CTkLabel(curral_toplevel, text="Currais", text_color="#607D8B", font=("Helvetica", 49)).place(x=175, y=10)

 

    text_numero_curral = customtkinter.CTkLabel(curral_toplevel, text="Curral que trabalha", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=100)

 

    text1_numero_curral = customtkinter.CTkLabel(curral_toplevel, text="2", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=130)

 

    text_endereco_curral = customtkinter.CTkLabel(curral_toplevel, text="Endereço do curral", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=175)

 

    text1_endereco_curral = customtkinter.CTkLabel(curral_toplevel, text="Rua dos coqueirais, 210", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=200)

 

def Atividades_button():

    print("Clicou no botão Atividades")

    Atividades_toplevel = customtkinter.CTkToplevel(tela, fg_color="#CFD8DC")

    Atividades_toplevel.geometry("500x300")

    Atividades_toplevel.resizable(False, False)

    Atividades_toplevel.title("Atividades")

    Atividades_toplevel.focus_force()

    Atividades_toplevel.grab_set()

    Atividades_toplevel.transient(tela)

    texto_Atividades_toplevel = customtkinter.CTkLabel(Atividades_toplevel, text="Atividades", text_color="#607D8B", font=("Helvetica", 49)).place(x=100, y=10)

 

    text_nome_Atividades = customtkinter.CTkLabel(Atividades_toplevel, text="Lista das Atividades", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=100)

    text1_nome_Atividades = customtkinter.CTkLabel(Atividades_toplevel, text="Check up", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=130)

 

    text_codigo_Atividades = customtkinter.CTkLabel(Atividades_toplevel, text="Código do Atividades", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=175)

    text1_codigo_Atividades = customtkinter.CTkLabel(Atividades_toplevel, text="123456789", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=200)

 

def Afazeres_button():

    print("Clicou no botão Afazeres")

    Afazeres_toplevel = customtkinter.CTkToplevel(tela, fg_color="#CFD8DC")

    Afazeres_toplevel.geometry("500x300")

    Afazeres_toplevel.resizable(False, False)

    Afazeres_toplevel.title("Afazeres")

    Afazeres_toplevel.focus_force()

    Afazeres_toplevel.grab_set()

    Afazeres_toplevel.transient(tela)

    texto_Afazeres_toplevel = customtkinter.CTkLabel(Afazeres_toplevel, text="Afazeres", text_color="#607D8B", font=("Helvetica", 49)).place(x=100, y=10)

 

    text_nome_Afazeres = customtkinter.CTkLabel(Afazeres_toplevel, text="Afazeres", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=100)

   

    text1_nome_Afazeres = customtkinter.CTkLabel(Afazeres_toplevel, text="lista de afazeres", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=130)

 

    text_quantidade_Afazeres = customtkinter.CTkLabel(Afazeres_toplevel, text="Datas dos afazeres", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=175)

   

    text1_quantidade_Afazeres = customtkinter.CTkLabel(Afazeres_toplevel, text="23/07 - Limpeza do Curral 2", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=200)

 

def tabela_de_alimentacao_button():

    print("Clicou no botão Tabela de Alimentação")

    tabela_de_alimentacao_toplevel = customtkinter.CTkToplevel(tela, fg_color="#CFD8DC")

    tabela_de_alimentacao_toplevel.geometry("500x300")

    tabela_de_alimentacao_toplevel.resizable(False, False)

    tabela_de_alimentacao_toplevel.title("Tabela de Alimentação")

    tabela_de_alimentacao_toplevel.focus_force()

    tabela_de_alimentacao_toplevel.grab_set()

    tabela_de_alimentacao_toplevel.transient(tela)

    texto_tabela_de_alimentacao_toplevel = customtkinter.CTkLabel(tabela_de_alimentacao_toplevel, text="Alimentação \ndos animais", text_color="#607D8B", font=("Helvetica", 38)).place(x=25, y=10)

 

    text_tabela_de_alimentacao = customtkinter.CTkLabel(tabela_de_alimentacao_toplevel, text="Data da Alimentação", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=100)

   

    text1_nome_vacina = customtkinter.CTkLabel(tabela_de_alimentacao_toplevel, text="01/01/2021", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=130)

 

    text_data_vacina = customtkinter.CTkLabel(tabela_de_alimentacao_toplevel, text="Horario da Alimentação", text_color="#607D8B", font=("Helvetica", 20)).place(x=10, y=175)

   

    text1_data_vacina = customtkinter.CTkLabel(tabela_de_alimentacao_toplevel, text="07:32", text_color="#607D8B", font=("Helvetica", 20)).place(x=20, y=200)

 

def remedios_button():

    print("Clicou no botão histórico de remédios")

    remedios_toplevel = customtkinter.CTkToplevel(tela, fg_color="#CFD8DC")

    remedios_toplevel.geometry("500x300")

    remedios_toplevel.resizable(False, False)

    remedios_toplevel.title("Histórico de Remédios")

    remedios_toplevel.focus_force()

    remedios_toplevel.grab_set()

    remedios_toplevel

tela.mainloop()