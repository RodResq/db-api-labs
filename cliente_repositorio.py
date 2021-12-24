import MySQLdb

class ClienteRepositorio():

    @staticmethod
    def listar_clientes():
        db = MySQLdb.connect(user="root", passwd="123", db="treinaweb_clientes", host="localhost", port=3306, autocommit=True)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM cliente")
        print(cursor.fetchall())
        db.close()

    @staticmethod
    def inserir_cliente(cliente):
        db = MySQLdb.connect(user="root", passwd="123", db="treinaweb_clientes", host="localhost", port=3306, autocommit=True)
        cursor = db.cursor()
        cursor.execute("INSERT INTO cliente (nome, idade) VALUES (%s, %s)", (cliente.nome, cliente.idade))
        db.close()

    @staticmethod
    def editar_cliente(id_cliente, cliente):
        db = MySQLdb.connect(user="root", passwd="123", db="treinaweb_clientes", host="localhost", port=3306, autocommit=True)
        cursor = db.cursor()
        cursor.execute("UPDATE cliente SET nome=%(nome)s, idade=%(idade)s WHERE idCLiente=%(id_cliente)s", ({'nome': cliente.nome, 'idade': cliente.idade, 'id_cliente': id_cliente}))
        db.close()

    @staticmethod
    def remover_cliente(id_cliente):
        db = MySQLdb.connect(user="root", passwd="123", db="treinaweb_clientes", host="localhost", port=3306, autocommit=True)
        cursor = db.cursor()
        cursor.execute("DELETE FROM cliente WHERE idCliente=%s", (id_cliente, ))
        db.close()