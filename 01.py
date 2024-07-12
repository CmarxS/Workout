import sqlite3

con = sqlite3.connect('mydatabase.sqlite')

cur = con.cursor()

def criar_tabela(cursor):
    
    cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(255), email VARCHAR(150))')

def registro(conexao, cursor):
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    data = (nome, email)

    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', data)
    conexao.commit()

def deletar_registro(conexao, cursor):
    id = input("Digite o ID do registro que deseja deletar: ")
    cursor.execute('DELETE FROM clientes WHERE id = ?', id)
    conexao.commit()

def atualizar(conexao, cursor):
    id = input("Digite o ID do registro que deseja deletar: ")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome = ?, email = ? WHERE id = ?', data)
    conexao.commit()

print("O que desejea fazer?")
print("1 - Criar tabela")
print("2 - Inserir registro")
print("3 - Deletar registro")
print("4 - Atualizar registro")
escolha = input("Digite o número da opção desejada: ")
while escolha != '0':
    if escolha == '1':
        criar_tabela(cur)
    elif escolha == '2':
        registro(con, cur)
    elif escolha == '3':
        deletar_registro(con, cur)
    elif escolha == '4':
        atualizar(con, cur)
    else:
        print("Opção inválida")
    escolha = input("Digite o número da opção desejada: ")