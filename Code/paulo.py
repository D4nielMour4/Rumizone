import tkinter as tk
from tkinter import ttk

def cadastrar_funcionario():
    nome = entry_nome.get()
    sexo = combo_sexo.get()
    idade = entry_idade.get()
    cargo = entry_cargo.get()
    email = entry_email.get()
    celular = entry_celular.get()
    observacoes = text_observacoes.get("1.0", "end-1c")
    


    # Exemplo de exibição dos dados, substituir pelo backend.
    print("Nome:", nome)
    print("Sexo:", sexo)
    print("Idade:", idade)
    print("Cargo:", cargo)
    print("Email:", email)
    print("Celular:", celular)
    print("Observações:", observacoes)

app = tk.Tk()
app.title("Cadastro de Funcionário")

# Labels
label_nome = tk.Label(app, text="Nome:")
label_sexo = tk.Label(app, text="Sexo:")
label_idade = tk.Label(app, text="Idade:")
label_cargo = tk.Label(app, text="Cargo:")
label_email = tk.Label(app, text="Email:")
label_celular = tk.Label(app, text="Celular:")
label_observacoes = tk.Label(app, text="Observações:")
text_observacoes = tk.Text(app, height=5, width=30)

# Entradas de texto
entry_nome = tk.Entry(app)
entry_idade = tk.Entry(app)
entry_cargo = tk.Entry(app)
entry_email = tk.Entry(app)
entry_celular = tk.Entry(app)

# Combobox para seleção do sexo
combo_sexo = ttk.Combobox(app, values=["Masculino", "Feminino", "Outro"])
combo_sexo.set("Selecione")

# Botão de cadastro
botao_cadastrar = tk.Button(app, text="Cadastrar", command=cadastrar_funcionario)

# Posicionamento dos widgets na janela
label_nome.grid(row=0, column=0)
label_sexo.grid(row=1, column=0)
label_idade.grid(row=2, column=0)
label_cargo.grid(row=3, column=0)
label_email.grid(row=4, column=0)
label_celular.grid(row=5, column=0)
label_observacoes.grid(row=6, column=0)
text_observacoes.grid(row=6, column=1)

entry_nome.grid(row=0, column=1)
combo_sexo.grid(row=1, column=1)
entry_idade.grid(row=2, column=1)
entry_cargo.grid(row=3, column=1)
entry_email.grid(row=4, column=1)
entry_celular.grid(row=5, column=1)

botao_cadastrar.grid(row=7, columnspan=2)

app.mainloop()