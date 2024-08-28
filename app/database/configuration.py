#DATOS PARA LA CONEXIÓN A DB
dataBaseName = "clase4gestordb"
userName = 'root'
userpassword = ''
connectionPort = 3306
server = 'localhost'

#CREANDO LA CONEXIÓN A DB
databaseConnedction = f'mysql+mysqlconnectorpython://{userName}:{userpassword}@{server}:{connectionPort}/{dataBaseName}'
