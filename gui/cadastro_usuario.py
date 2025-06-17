import tkinter as tk
from tkinter import messagebox
from controllers.auth import cadastrar_usuario

def show():
    win = tk.Toplevel()
    win.title("Cadastro de Usuário")

    tk.Label(win, text="Nome").grid(row=0, column=0)
    tk.Label(win, text="Usuário").grid(row=1, column=0)
    tk.Label(win, text="Senha").grid(row=2, column=0)
    tk.Label(win, text="Perfil (admin/comum)").grid(row=3, column=0)

    nome = tk.Entry(win)
    usuario = tk.Entry(win)
    senha = tk.Entry(win, show="*")
    perfil = tk.Entry(win)

    nome.grid(row=0, column=1)
    usuario.grid(row=1, column=1)
    senha.grid(row=2, column=1)
    perfil.grid(row=3, column=1)

    def salvar():
        if perfil.get() not in ["admin", "comum"]:
            messagebox.showerror("Erro", "Perfil deve ser 'admin' ou 'comum'")
            return
        cadastrar_usuario(nome.get(), usuario.get(), senha.get(), perfil.get())
        messagebox.showinfo("Sucesso", "Usuário cadastrado")
        win.destroy()

    tk.Button(win, text="Salvar", command=salvar).grid(row=4, columnspan=2)
