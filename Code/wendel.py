import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def clique():
    print("Fazer login")

def voltar_para_inicio(frame_atual):
    frame_atual.pack_forget()
    frame_inicio.pack()

def janela_login():
    frame_inicio.pack_forget()
    frame_registro.pack_forget() 
    frame_login.pack()

def janela_registro():
    frame_inicio.pack_forget()
    frame_login.pack_forget()
    frame_registro.pack()

janela = customtkinter.CTk()
janela.geometry("1360x720")
janela.resizable(False, False)
janela.title("Rumizone")

frame_inicio = Frame(janela)
frame_inicio.pack()

espaco = customtkinter.CTkLabel(frame_inicio, text=" ")
espaco.pack(padx=10, pady=10)
espaco.pack(padx=10, pady=10)
espaco1 = customtkinter.CTkLabel(frame_inicio, text=" ")
espaco1.pack(padx=10, pady=10)
espaco2 = customtkinter.CTkLabel(frame_inicio, text=" ")
espaco2.pack(padx=10, pady=10)
texto = customtkinter.CTkLabel(frame_inicio, text="Rumizone", text_color="#2ca474", font=("Helvetica", 36))
texto.pack(padx=10, pady=10)
texto1 = customtkinter.CTkLabel(frame_inicio, text="Monitoramento e comportamento animal", font=("Helvetica", 14))
texto1.pack(padx=5, pady=5)

botao3 = customtkinter.CTkButton(frame_inicio, text="Login", command=janela_login)
botao3.pack(padx=10, pady=10)

botao2 = customtkinter.CTkButton(frame_inicio, text="Registre-se", command=janela_registro)
botao2.pack(padx=10, pady=10)

frame_login = Frame(janela)
frame_registro = Frame(janela)

texto_login = customtkinter.CTkLabel(frame_login, text="Fazer login")
texto_login.pack(padx=10, pady=10)
email = customtkinter.CTkEntry(frame_login, placeholder_text="Seu e-mail")
email.pack(padx=10, pady=10)
senha = customtkinter.CTkEntry(frame_login, placeholder_text="Digite sua senha", show="*")
senha.pack(padx=10, pady=10)
checkbox = customtkinter.CTkCheckBox(frame_login, text="Lembrar login")
checkbox.pack(padx=10, pady=10)
botao_login = customtkinter.CTkButton(frame_login, text="Login", command=clique)
botao_login.pack(padx=10, pady=10)
botao_voltar_login = customtkinter.CTkButton(frame_login, text="Voltar", command=lambda: voltar_para_inicio(frame_login))
botao_voltar_login.pack(padx=10, pady=10)

texto_registro = customtkinter.CTkLabel(frame_registro, text="Fazer registro")
texto_registro.pack(padx=10, pady=10)
email_registro = customtkinter.CTkEntry(frame_registro, placeholder_text="Digite seu e-mail")
email_registro.pack(padx=10, pady=10)
confirmacao_senha = customtkinter.CTkEntry(frame_registro, placeholder_text="Digite sua senha de novo", show="*")
confirmacao_senha.pack(padx=10, pady=10)
senha_registro = customtkinter.CTkEntry(frame_registro, placeholder_text="Digite sua senha", show="*")
senha_registro.pack(padx=10, pady=10)
checkbox_registro = customtkinter.CTkCheckBox(frame_registro, text="Lembrar registro")
checkbox_registro.pack(padx=10, pady=10)
botao_registro = customtkinter.CTkButton(frame_registro, text="Registrar", command=clique)
botao_registro.pack(padx=10, pady=10)
botao_voltar_registro = customtkinter.CTkButton(frame_registro, text="Voltar", command=lambda: voltar_para_inicio(frame_registro))
botao_voltar_registro.pack(padx=10, pady=10)

janela.mainloop()

# Resolver problema da barra branca no meio de todas as telas
