# se importa el engine
from base_datos import engine

# se crea la clase llamada Base que permite definir las clases bajo las
# características de SQLAlchemy
db = engine["Matriculas"]
collection = db["registrosestudiantes"]

# Se crea la una entidad llamada Autor, que hereda
# de Base

#data_01 ={"nombre":"Edison", "apellido": "Achote","matricula": "utpl","modalidad": "adistancia","carrera": "TDE","correo": "erachote@gmail.com","direccion": "latacunga"}
#collection.insert_one(data_01)

collection2= db["RegistroVehiculos"]
data_02={"marca": "Toyota","modelo": "toyota","placa": "PDC5828","año": 2020,"color": "Rojo","propietario": "Edison Achote"}
collection2.insert_one(data_02)