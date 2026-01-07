import mysql.connector

# Conectar ao servidor MariaDB
conexao = mysql.connector.connect(
    host="localhost",
    user="nome do usuario",
    password="sua senha"
)

cursor = conexao.cursor()

# Criar um banco de dados
cursor.execute("CREATE DATABASE IF NOT EXISTS meu_banco")

# Selecionar o banco
cursor.execute("USE meu_banco")

# Criar tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    idade INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(5,2) NOT NULL,
    estoque INT NOT NULL
)
""")

# Inserir dados na tabela usuarios
cursor.execute("INSERT INTO usuarios (nome, email, idade) VALUES (%s, %s, %s)",
               ("Maria", "maria@email.com", 25))
cursor.execute("INSERT INTO usuarios (nome, email, idade) VALUES (%s, %s, %s)",
               ("João", "joao@email.com", 30))

# Salvar alterações
conexao.commit()

# Inserir dados na tabela produtos
cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)",
               ("biscoito", 2.99, 50))
cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)",
               ("ARROZ", 5.00, 50))

# Salvar alterações
conexao.commit()

# Consultar dados
cursor.execute("SELECT * FROM usuarios")
for linha in cursor.fetchall():
    print(linha)

cursor.execute("SELECT * FROM produtos")
for linha in cursor.fetchall():
    print(linha)

# Fechar conexão
cursor.close()
conexao.close()
