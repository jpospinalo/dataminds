import mysql.connector

# Configura los detalles de tu conexión
def connect():
    conexion = mysql.connector.connect(
        host="proyecto-dataminds.cfzybbinygh8.us-east-1.rds.amazonaws.com",         # O la dirección de tu servidor MySQL
        user="admin",         # Tu usuario de MySQL
        password="adminadmin",  # Tu contraseña de MySQL
        database="DataMinds" # El nombre de la base de datos a la que te quieres conectar
    )
    return conexion

 
