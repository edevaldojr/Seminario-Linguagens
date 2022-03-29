import pymysql


conn = pymysql.connect(host="localhost", user="root", password="", db="seminario_pessoas")

crudPessoa = conn.cursor()


opcao = 0

while opcao != 5:
    print("1 - INSERT")
    print("2 - UPDATE")
    print("3 - DELETE")
    print("4 - SELECT")
    print("5 - EXIT")
    print("insira uma opção> ")
    opcao = input()

    if opcao == 1:
        crudPessoa.execute("INSERT INTO pessoa(nome, email, telefone, idade) VALUES(Lucas Gomes da Silva, lucasg@gmail.com, 20)")
        print(" > Dados inseridos!!")
    
    else:
        print("Saindo do loop")



#crudPessoa.execute("UPDATE seminario_pessoas SET nome=?, email=?, telefone=?, idade=? WHERE id=?")
#print(" > Dados atualizados!!")

#crudPessoa.execute("DELETE FROM seminario_pessoas WHERE id=?")
#print(" > Dados apagados!!")

#crudPessoa.execute("SELECT * FROM seminario_pessoas WHERE id=?")
#print(" > Dados recuperados!!")


conn.commit()
conn.close