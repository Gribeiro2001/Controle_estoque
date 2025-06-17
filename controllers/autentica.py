from utils.encryption import hash_password

def cadastrar_usuario(nome, usuario, senha, perfil):
    senha_hash = hash_password(senha)
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO usuarios (nome, usuario, senha, perfil) VALUES (?, ?, ?, ?)
    """, (nome, usuario, senha_hash, perfil))
    conn.commit()
    conn.close()
