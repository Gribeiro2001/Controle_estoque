def listar_produtos():
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, quantidade, minimo FROM produtos")
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def atualizar_produto(id, nome, quantidade, minimo):
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE produtos SET nome = ?, quantidade = ?, minimo = ? WHERE id = ?
    """, (nome, quantidade, minimo, id))
    conn.commit()
    conn.close()

def deletar_produto(id):
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
