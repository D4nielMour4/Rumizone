import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def clique():
    print("Fazer login")

def janela_login():
    nova_janela = customtkinter.CTk()
    nova_janela.geometry("800x550")
    nova_janela.title("Sessão do Usuário")
    texto = customtkinter.CTkLabel(nova_janela, text="Fazer login")
    texto.pack(padx=10, pady=10)
    email = customtkinter.CTkEntry(nova_janela, placeholder_text="Seu e-mail")
    email.pack(padx=10, pady=10)
    senha = customtkinter.CTkEntry(nova_janela, placeholder_text="Digite sua senha", show="*")
    senha.pack(padx=10, pady=10)
    checkbox = customtkinter.CTkCheckBox(nova_janela, text="Lembrar login")
    checkbox.pack(padx=10, pady=10)
    botao = customtkinter.CTkButton(nova_janela, text="Login", command=clique)
    botao.pack(padx=10, pady=10)
    nova_janela.mainloop()
    
def janela_registro():
    nova_janela2 = customtkinter.CTk()
    nova_janela2.geometry("800x550")
    nova_janela2.title("Sessão de registro")
    
    

janela = customtkinter.CTk()
janela.geometry("800x550")
janela.resizable(False, False)
janela.title("Rumizone")

espaco = customtkinter.CTkLabel(janela, text=" ")
espaco.pack(padx=10, pady=10)
espaco.pack(padx=10, pady=10)
espaco1 = customtkinter.CTkLabel(janela, text=" ")
espaco1.pack(padx=10, pady=10)
espaco2 = customtkinter.CTkLabel(janela, text=" ")
espaco2.pack(padx=10, pady=10)
texto = customtkinter.CTkLabel(janela, text="Rumizone", font=("Helvetica", 36))
texto.pack(padx=10, pady=10)
texto1 = customtkinter.CTkLabel(janela, text="Monitoramento e comportamento animal", font=("Helvetica", 14))
texto1.pack(padx=5, pady=5)

botao3 = customtkinter.CTkButton(janela, text="Login", command=janela_login)
botao3.pack(padx=10, pady=10)

botao2 = customtkinter.CTkButton(janela, text="Registre-se")
botao2.pack(padx=10, pady=10)


janela.mainloop()
