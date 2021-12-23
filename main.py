import MySQLdb

db = MySQLdb.connect(user="root", passwd="123", db="treinaweb_clientes", host="localhost", port=3306)
print("Conexao realizada com sucesso em ")
db.close()


