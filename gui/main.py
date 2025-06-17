import gui.cadastro_usuario as cadastro_usuario

if usuario['perfil'] == 'admin':
    tk.Button(root, text="Cadastrar Usuário", command=cadastro_usuario.show).pack()

