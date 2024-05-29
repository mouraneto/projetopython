import tkinter as tk
from tkinter import messagebox

estoque = {}

def adicionar_produto():
    produto = entry_produto.get()
    if produto:
        try:
            quantidade = int(entry_quantidade.get())
            estoque[produto] = quantidade
            atualizar_estoque()
            entry_produto.delete(0, tk.END)
            entry_quantidade.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite uma quantidade válida.")
    else:
        messagebox.showerror("Erro", "Por favor, digite o nome do produto.")

def revisar_estoque():
    estoque_str = "\n".join([f"{produto}: {quantidade}" for produto, quantidade in estoque.items()])
    quantidade_total = sum(estoque.values())
    messagebox.showinfo("Estoque Atual", f"{estoque_str}\n\nQuantidade total de produtos: {quantidade_total}")

def remover_produto():
    produto = entry_produto.get()
    if produto in estoque:
        del estoque[produto]
        atualizar_estoque()
        entry_produto.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Produto não encontrado no estoque.")

def limpar_estoque():
    confirmacao = messagebox.askyesno("Confirmar", "Tem certeza que deseja limpar o estoque?")
    if confirmacao:
        estoque.clear()
        atualizar_estoque()

def atualizar_estoque():
    text_estoque.delete("1.0", tk.END)
    for produto, quantidade in estoque.items():
        text_estoque.insert(tk.END, f"{produto}: {quantidade}\n")

def sair():
    root.destroy()

root = tk.Tk()
root.title("PaCoTãO - Seu Estoque Online")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_produto = tk.Label(frame, text="Nome do Produto:")
label_produto.grid(row=0, column=0, padx=5, pady=5)
entry_produto = tk.Entry(frame)
entry_produto.grid(row=0, column=1, padx=5, pady=5)

label_quantidade = tk.Label(frame, text="Quantidade:")
label_quantidade.grid(row=1, column=0, padx=5, pady=5)
entry_quantidade = tk.Entry(frame)
entry_quantidade.grid(row=1, column=1, padx=5, pady=5)

btn_adicionar = tk.Button(frame, text="Adicionar Produto", command=adicionar_produto)
btn_adicionar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

btn_revisar = tk.Button(frame, text="Revisar Estoque", command=revisar_estoque)
btn_revisar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

btn_remover = tk.Button(frame, text="Remover Produto", command=remover_produto)
btn_remover.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

btn_limpar = tk.Button(frame, text="Limpar Estoque", command=limpar_estoque)
btn_limpar.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

btn_sair = tk.Button(frame, text="Sair", command=sair)
btn_sair.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

text_estoque = tk.Text(root, height=10, width=40)
text_estoque.pack(padx=10, pady=10)

root.mainloop()