from datetime import datetime
from connection import *

##Función de la lectura de clientes.

def read_clients():
    
    conexion = connect()
    ## ------------------ Consulta ___________
    cursor = conexion.cursor()
    
    # Ejemplo de una consulta SELECT
    cursor.execute("SELECT * FROM Cliente")
    
    # Obtener todos los resultados
    resultados = cursor.fetchall()
    
    # Imprimir los resultados
    for fila in resultados:
        print(fila)
    
    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

##Función de la creación de clientes.

def create_client():
    
    conexion = connect()
    ## ------------------ Consulta ___________
    cursor = conexion.cursor()
    
    # Solicitar al usuario los datos a actualizar (por ejemplo, ID del cliente y nuevo valor)
    tipo_documento = input("Ingrese el Tipo de Documento: ")
    numero_documento = input("Ingrese el número de Documento: ")
    nombres = input("Ingrese el nombre: ")
    apellidos = input("Ingrese el apellido: ")
    fecha_pago = input("Ingrese la fecha de pago: ")
    fecha_pago = datetime.strptime(fecha_pago, "%Y-%m-%d").date()
    
    # Ejemplo de una consulta SELECT
    cursor.execute("INSERT INTO Cliente (tipo_documento, numero_documento, nombres, apellidos, fecha_pago) VALUES (%s, %s, %s, %s, %s)", (tipo_documento, numero_documento, nombres, apellidos, fecha_pago))
    
    # enviar todos las inserciones.
    conexion.commit()
    
    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close() 
    
##Función de la actualización de clientes.

def update_client():

    conexion = connect()
    ## ------------------ Consulta ___________
    cursor = conexion.cursor()

    # Solicitar al usuario los datos a actualizar (por ejemplo, ID del cliente y nuevo valor)
    cliente_id = input("Ingrese el ID del cliente a actualizar: ")
    fecha_pago = input("Ingrese nueva fecha de pago: ")

    # Consulta UPDATE para modificar el registro
    cursor.execute("UPDATE Cliente SET fecha_pago = %s WHERE cliente_id = %s", (fecha_pago, cliente_id))

    # enviar todas las actualizaciones..
    conexion.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

##Función de la eliminación de clientes.

def delete_client():

    conexion = connect()
    ## ------------------ Consulta ___________
    cursor = conexion.cursor()

    # Solicitar al usuario el ID del cliente a eliminar
    cliente_id = input("Ingrese el ID del cliente a eliminar: ")

    # Consulta DELETE para eliminar el registro
    cursor.execute("DELETE FROM Cliente WHERE cliente_id = %s", (cliente_id,))

    # enviar todas las eliminaciones.
    conexion.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()
