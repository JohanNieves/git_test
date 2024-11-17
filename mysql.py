import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user= 'root',
    password= 'eEw4Pb5d',
    database= 'prueba'
)

def poblar_tabla():
    print("Poblando la tabla 'prueba', Escribe 'salir' en cualquier campo para terminar.")
    
    while True:
        id = input("ingresa el id: ")
        if id.lower() == "salir":
            break
        
        nombre = input("ingresa el nombre: ")
        if nombre.lower() == "salir":
            break
        
        try:
            query = "INSERT INTO nombre (id, nombre) VALUES (%s, %s)"
            cursor.execute(query, (id, nombre))
            conexion.commit()
            print("Datos insertados correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al insertar datos: {e}")
            conexion.rollback()
            
poblar_tabla()
cursor.close()
conexion.close()

