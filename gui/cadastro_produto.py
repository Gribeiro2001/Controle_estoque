import tkinter as tk
from tkinter import messagebox
from controllers.estoque import cadastrar_produto

def show():
    win = tk.Toplevel()
    win.title("Cadastrar Produto")

    tk.Label(win, text="Nome").grid(row=0, column=0)
    tk.Label(win, text="Quantidade").grid(row=1, column=0)
    tk.Label(win, text="Estoque Mínimo").grid(row=2, column=0)

    nome = tk.Entry(win)
    qtd = tk.Entry(win)
    minimo = tk.Entry(win)

    nome.grid(row=0, column=1)
    qtd.grid(row=1, column=1)
    minimo.grid(row=2, column=1)

    def salvar():
        try:
            quantidade = int(qtd.get())
            estoque_minimo = int(minimo.get())
            cadastrar_produto(nome.get(), quantidade, estoque_minimo)
            messagebox.showinfo("Sucesso", "Produto cadastrado")
            win.destroy()
        except ValueError:
            messagebox.showerror("Erro", "Quantidade e Estoque Mínimo devem ser números")

    tk.Button(win, text="Salvar", command=salvar).grid(row=3, columnspan=2)
