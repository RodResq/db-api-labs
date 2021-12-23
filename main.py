import MySQLdb

db = MySQLdb.connect(user="root", passwd="123", db="treinaweb_clientes", host="localhost", port=3306)
print("Conexao realizada com sucesso em ")

cursor = db.cursor()
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchmany(1))

cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Maria', 25)")
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())
print(cursor.lastrowid)

cursor.execute("UPDATE cliente SET nome='Ana' WHERE idCLiente=2")
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())

cursor.execute("DELETE FROM cliente WHERE idCliente=9")
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())

db.close()


