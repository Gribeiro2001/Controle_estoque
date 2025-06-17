import tkinter as tk
from tkinter import messagebox
from controllers.auth import login
import gui.main_window as main_window

def show_login():
    root = tk.Tk()
    root.title("Login")

    tk.Label(root, text="Usuário").grid(row=0, column=0)
    tk.Label(root, text="Senha").grid(row=1, column=0)

    entry_user = tk.Entry(root)
    entry_pass = tk.Entry(root, show="*")

    entry_user.grid(row=0, column=1)
    entry_pass.grid(row=1, column=1)

    def entrar():
        user = entry_user.get()
        pwd = entry_pass.get()
        perfil = login(user, pwd)
        if perfil:
            root.destroy()
            main_window.show_main(perfil)
        else:
            messagebox.showerror("Erro", "Login inválido")

    tk.Button(root, text="Entrar", command=entrar).grid(row=2, column=0, columnspan=2)

    root.mainloop()
