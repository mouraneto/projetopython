import tkinter as tk
from tkinter import messagebox

estoque = {}

def adicao():
    produto = entry_produto.get()
    quantidade = entry_quantidade.get()
    if produto.strip() == '':
        messagebox.showerror("Erro", "Por favor, insira o nome do produto.")
        return
    if quantidade.strip() == '':
        messagebox.showerror("Erro", "Por favor, insira a quantidade do produto.")
        return
    try:
        quantidade = int(quantidade)
    except ValueError:
        messagebox.showerror("Erro", "A quantidade deve ser um número inteiro.")
        return

    estoque[produto] = quantidade
    update_display()

def revisao():
    if not estoque:
        messagebox.showinfo("Revisão de Estoque", "O estoque está vazio.")
        return

    revisao_window = tk.Toplevel(root)
    revisao_window.title("Revisão de Estoque")

    for i, (produto, quantidade) in enumerate(estoque.items()):
        tk.Label(revisao_window, text=f"{produto}: {quantidade}").grid(row=i, column=0, sticky="w")

def exclusao():
    produto = entry_produto.get()
    if produto not in estoque:
        messagebox.showerror("Erro", f"Produto '{produto}' não encontrado.")
        return

    del estoque[produto]
    update_display()

def limpeza():
    estoque.clear()
    update_display()

def update_display():
    display_text.set("\n".join([f"{produto}: {quantidade}" for produto, quantidade in estoque.items()]))

root = tk.Tk()
root.title("PaCoTãO - Seu Estoque Online")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Produto:").grid(row=0, column=0)
entry_produto = tk.Entry(frame)
entry_produto.grid(row=0, column=1)

tk.Label(frame, text="Quantidade:").grid(row=1, column=0)
entry_quantidade = tk.Entry(frame)
entry_quantidade.grid(row=1, column=1)

btn_adicionar = tk.Button(frame, text="Adicionar", command=adicao)
btn_adicionar.grid(row=2, columnspan=2, pady=5)

btn_revisar = tk.Button(frame, text="Revisar Estoque", command=revisao)
btn_revisar.grid(row=3, columnspan=2, pady=5)

btn_excluir = tk.Button(frame, text="Excluir Produto", command=exclusao)
btn_excluir.grid(row=4, columnspan=2, pady=5)

btn_limpar = tk.Button(frame, text="Limpar Estoque", command=limpeza)
btn_limpar.grid(row=5, columnspan=2, pady=5)

display_text = tk.StringVar()
display_text.set("")
display_label = tk.Label(root, textvariable=display_text, justify="left")
display_label.pack()

root.mainloop()
