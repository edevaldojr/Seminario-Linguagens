import mysql.connector

conexao = mysql.connector.connect(
	host = 'wagnerweinert.com.br',
	user = 'tads20_lucas_silva',
	password = 'Y6S4aSxDk3K2vO6C',
	database = 'tads20_lucas_silva'
)

cursor = conexao.cursor()

opcao = 0

while opcao != 5:
	print("\n1 - Create")
	print("2 - Read")
	print("3 - Update")
	print("4 - Delete")
	print("5 - Sair")

	opcao = int(input("\n> "))

	if opcao == 1:
		nome = input("Nome: ")
		email = input("Email: ")
		telefone = input("Telefone: ")

		comando = f'INSERT INTO Pessoas (nome, email, telefone) VALUES ("{nome}", "{email}", "{telefone}")'
		cursor.execute(comando)
		conexao.commit()

	elif opcao == 2:
		comando = f'SELECT * FROM Pessoas'
		cursor.execute(comando)
		resultado = cursor.fetchall()

		print(resultado)

	elif opcao == 3:
		email = input("Email: ")
		telefone = input("Novo Telefone: ")

		comando = f'UPDATE Pessoas SET telefone = "{telefone}" WHERE email = "{email}"'
		cursor.execute(comando)
		conexao.commit()

	elif opcao == 4:
		email = input("Email: ")

		comando = f'DELETE FROM Pessoas WHERE email = "{email}"'
		cursor.execute(comando)
		conexao.commit()

		cursor.close()
		conexao.close()

	else:
		print("Opcao inválida!")
