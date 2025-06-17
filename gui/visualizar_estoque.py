import tkinter as tk
from tkinter import messagebox
from controllers.estoque import listar_produtos, atualizar_produto, deletar_produto

def show():
    win = tk.Toplevel()
    win.title("Estoque Atual")

    produtos = listar_produtos()

    for idx, (id, nome, qtd, minimo) in enumerate(produtos):
        bg_color = "red" if qtd < minimo else "white"

        nome_var = tk.StringVar(value=nome)
        qtd_var = tk.StringVar(value=str(qtd))
        min_var = tk.StringVar(value=str(minimo))

        tk.Entry(win, textvariable=nome_var, bg=bg_color, width=20).grid(row=idx, column=0)
        tk.Entry(win, textvariable=qtd_var, bg=bg_color, width=10).grid(row=idx, column=1)
        tk.Entry(win, textvariable=min_var, bg=bg_color, width=10).grid(row=idx, column=2)

        def make_salvar(i=id, n=nome_var, q=qtd_var, m=min_var):
            return lambda: atualizar_produto(i, n.get(), int(q.get()), int(m.get()))

        def make_excluir(i=id):
            return lambda: (deletar_produto(i), win.destroy(), show())

        tk.Button(win, text="Salvar", command=make_salvar()).grid(row=idx, column=3)
        tk.Button(win, text="Excluir", command=make_excluir()).grid(row=idx, column=4)
