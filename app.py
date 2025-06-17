import sqlite3
import os
from gui.login_window import show_login

# Cria o banco de dados se não existir
if not os.path.exists("estoque.db"):
    with open("db/database.sql", "r") as f:
        script = f.read()
    conn = sqlite3.connect("estoque.db")
    conn.executescript(script)
    conn.commit()
    conn.close()

# Inicia a aplicação
show_login()
