import sqlite3  #importar a biblioteca do sqlite (banco de dados)

'''
Este arquivo cria uma tabela no banco de dados para gravar
as informações dos resultados obtidos elos usuarios
'''

connection = sqlite3.connect('brain_color_db.sqlite') #criar uma conexão sqlite

cursor = connection.cursor() # Criar um cursor para executar os comandos sql

# Abaixo criamos a tabela usuarios, nela inserimos o nome a cor que resultar no teste
cursor.execute("""CREATE TABLE usuarios (
	id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
	name TEXT NOT NULL,
	cor TEXT NOT NULL)""")

connection.commit() # Dar um Ok
connection.close()  # Encerrar a conexão