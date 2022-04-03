import mysql.connector

conexao = mysql.connector.connect(
	host = 'wagnerweinert.com.br',
	user = '',
	password = '',
	database = ''
)

cursor = conexao.cursor()

# CREATE
nome = input("Nome: ")
email = input("Email: ")
telefone = input("Telefone: ")

comando = f'INSERT INTO Pessoas (nome, email, telefone) VALUES ("{nome}", "{email}", "{telefone}")'
cursor.execute(comando)
conexao.commit()

# READ
comando = f'SELECT * FROM Pessoas'
cursor.execute(comando)
resultado = cursor.fetchall()

print(resultado)

# UPDATE
email = input("Email: ")
telefone = input("Novo Telefone: ")

comando = f'UPDATE Pessoas SET telefone = "{telefone}" WHERE email = "{email}"'
cursor.execute(comando)
conexao.commit()

# DELETE
email = input("Email: ")

comando = f'DELETE FROM Pessoas WHERE email = "{email}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()