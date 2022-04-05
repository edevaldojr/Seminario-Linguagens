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
	print("\n")
	print("1 - Create")
	print("2 - Read")
	print("3 - Update")
	print("4 - Delete")
	print("5 - Sair")

	opcao = int(input("\n> "))

	if opcao == 1:
		nome = input("Nome: ")
		email = input("Email: ")
		telefone = input("Telefone: ")
		idade = int(input("Idade: "))

		comando = f'INSERT INTO pessoas_python (nome, email, telefone, idade) VALUES ("{nome}", "{email}", "{telefone}", "{idade}")'
		cursor.execute(comando)
		conexao.commit()

	elif opcao == 2:
		comando = f'SELECT * FROM pessoas_python'
		cursor.execute(comando)
		resultado = cursor.fetchall()
	
		print(resultado)

	elif opcao == 3:
		email = input("Email: ")
		telefone = input("Novo Telefone: ")

		comando = f'UPDATE pessoas_python SET telefone = "{telefone}" WHERE email = "{email}"'
		cursor.execute(comando)
		conexao.commit()

	elif opcao == 4:
		email = input("Email: ")

		comando = f'DELETE FROM pessoas_python WHERE email = "{email}"'
		cursor.execute(comando)
		conexao.commit()

	elif opcao == 5:
		cursor.close()
		conexao.close()
		break
		
	else:
		print("Opcao inválida!")