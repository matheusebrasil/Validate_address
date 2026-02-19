import tkinter as tk
from tkinter import messagebox
import re
import requests

def validar_por_cep(cep):
    # Limpa o CEP (mantém apenas números)
    cep = re.sub(r'\D', '', cep)
    if len(cep) != 8:
        return False, "CEP deve ter 8 dígitos."
    
    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        data = response.json()
        if "erro" in data:
            return False, "CEP não encontrado na base de dados."
        return True, f"CEP Válido: {data['logradouro']}, {data['bairro']} - {data['localidade']}/{data['uf']}"
    except:
        return False, "Erro na conexão com o serviço de busca."

def validar_por_escrita(endereco):
    endereco = " ".join(endereco.split()).strip()
    padrao = r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+,\s?\d+"
    if len(endereco) < 10 or not re.search(padrao, endereco):
        return False, "Formato inválido. \n Use: Nome da Rua, Número"
    return True, "Endereço escrito validado com sucesso!"

def processar():
    opcao = var_escolha.get()
    entrada = entry_input.get()
    
    if opcao == "CEP":
        sucesso, mensagem = validar_por_cep(entrada)
    else:
        sucesso, mensagem = validar_por_escrita(entrada)
    
    if sucesso:
        messagebox.showinfo("Resultado", mensagem)
    else:
        messagebox.showerror("Erro de Validação", mensagem)

# --- Interface ---
root = tk.Tk()
root.title("Validator Address")
root.geometry("390x350")
root.configure(padx=20, pady=20)

tk.Label(root, text="\nSelecione o Método de Entrada:", font=("Arial", 10, "bold")).pack()

# Variável de controle para os RadioButtons
var_escolha = tk.StringVar(value="CEP")

tk.Radiobutton(root, text="Validar por CEP", variable=var_escolha, value="CEP").pack()
tk.Radiobutton(root, text="Validar por Endereço", variable=var_escolha, value="Texto").pack()

tk.Label(root, text="\n Digite abaixo:", font=("Arial", 9)).pack()
entry_input = tk.Entry(root, width=40, font=("Arial", 10))
entry_input.pack(pady=10)

btn_validar = tk.Button(root, text="Executar Validação", command=processar, 
                       bg="#1976D2", fg="white", width=20, font=("Arial", 10, "bold"))
btn_validar.pack(pady=20)

root.mainloop()