import MySQLdb

db = MySQLdb.connect(user="root", passwd="123", db="treinaweb_clientes", host="localhost", port=3306, autocommit=True)
print("Conexao realizada com sucesso em ")

cursor = db.cursor()
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchmany(1))

# Transacao
# try:
#     db.begin()
#     cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Pedro', 25)")
#     cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Joana', 25)")
#     db.commit()
# except:
#     db.rollback()
# print(cursor.execute("SELECT * FROM cliente"))
# print(cursor.fetchall())

# cursor.execute("SELECT * FROM cliente")
# print(cursor.fetchall())
# print(cursor.lastrowid)
#
# cursor.execute("UPDATE cliente SET nome='Ana' WHERE idCLiente=2")
# cursor.execute("SELECT * FROM cliente")
# print(cursor.fetchall())
#
# cursor.execute("DELETE FROM cliente WHERE idCliente=9")
# cursor.execute("SELECT * FROM cliente")
# print(cursor.fetchall())

# Passando parametro para a consulta
nome = "Josefina"
idade = 80
cursor.execute("UPDATE cliente SET nome=%(nome)s, idade=%(idade)s WHERE idCLiente=2", ({'nome': nome, 'idade': idade}))
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())

db.close()
