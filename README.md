# 📦 Sistema de Controle de Estoque

## 🧾 Descrição

Este sistema tem como objetivo controlar a entrada e saída de produtos e materiais. É possível cadastrar, editar e excluir produtos, visualizar estoque com alertas para baixo estoque e cadastrar novos usuários (somente perfil administrador).

---

## 🚀 Funcionalidades

✅ Login com validação de senha (criptografada)  
✅ Perfis de usuário: **Administrador** e **Comum**  
✅ Cadastro de produtos com quantidade mínima  
✅ Edição e exclusão de produtos  
✅ Alerta visual para produtos abaixo do estoque mínimo  
✅ Cadastro de usuários (apenas administrador)  
✅ Interface gráfica com `Tkinter`  
✅ Banco de dados local com `SQLite`

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- SQLite
- Tkinter
- Bcrypt (criptografia de senha)

---

## 📂 Estrutura de Pastas


---

## 🧠 Modelagem do Banco de Dados

### Entidades

#### Tabela `usuarios`

| Campo   | Tipo    | Descrição                |
|---------|---------|--------------------------|
| id      | INT     | Chave primária           |
| nome    | TEXT    | Nome do usuário          |
| usuario | TEXT    | Nome de login (único)    |
| senha   | TEXT    | Senha criptografada      |
| perfil  | TEXT    | admin ou comum           |

#### Tabela `produtos`

| Campo      | Tipo    | Descrição                          |
|------------|---------|------------------------------------|
| id         | INT     | Chave primária                     |
| nome       | TEXT    | Nome do produto                    |
| quantidade | INT     | Quantidade atual em estoque        |
| minimo     | INT     | Quantidade mínima permitida        |

---

## 🔐 Segurança

- Senhas são armazenadas com **hash Bcrypt**
- Validação de login com criptografia
- Sessão de usuário controlada por memória
- Permissões baseadas em perfil
- Apenas **administradores** podem cadastrar novos usuários

---

## 🔁 Fluxograma da Aplicação

```text
[Início]
   ↓
[Tela de Login]
   ↓
[Usuário e Senha]
   ↓
[Validação no Banco]
   ↓───[Inválido]───> [Mensagem de Erro]
   ↓
[Menu Principal]
   ↓
+--------------------------+
| Se Admin:                |
| - Cadastrar Produto      |
| - Visualizar Estoque     |
| - Cadastrar Usuário      |
+--------------------------+
| Se Comum:                |
| - Visualizar Estoque     |
+--------------------------+
