import MySQLdb

db = MySQLdb.connect(user="root", passwd="123", db="treinaweb_clientes", host="localhost", port=3306, autocommit=True)
print("Conexao realizada com sucesso em ")

cursor = db.cursor()
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchmany(1))


# Refatorando o Codiga para aplicar a POO
def listar_clientes():
    cursor.execute("SELECT * FROM cliente")
    print(cursor.fetchall())


def inserir_cliente(cliente):
    cursor.execute("INSERT INTO cliente (nome, idade) VALUES (%s, %s)", cliente.nome, cliente.idade)


def editar_cliente(id_cliente, cliente):
    cursor.execute("UPDATE cliente SET nome=%(nome)s, idade=%(idade)s WHERE idCLiente=%(id_cliente)s", ({'nome': cliente.nome, 'idade': cliente.idade, 'id_cliente': id_cliente}))


def remover_cliente(id_cliente):
    cursor.execute("DELETE FROM cliente WHERE idCliente=%s", (id_cliente, ))


listar_clientes()

db.close()
