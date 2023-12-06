# Importar el MongoClient
from pymongo import MongoClient

# Crear una instancia de MongoClient
engine = MongoClient('mongodb+srv://edAchote24:241993Eddy@cluster0.0zjkhwr.mongodb.net/?retryWrites=true&w=majority')

# Seleccionar la base de datos y la colección
db = engine["Matriculas"]
collection = db["registrosestudiantes"]

# Consultar todos los registros en la colección
resultados = collection.find()

# Imprimir los resultados
for resultado in resultados:
    print(resultado)
