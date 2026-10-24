# Importar librerías necesarias
import mysql.connector
from datetime import datetime

# =============================================
# CONFIGURACIÓN DE LA BASE DE DATOS
# =============================================

# Datos de conexión a Clever Cloud (cambiar por tus datos reales)
config_bd = {
    'host': 'localhost',
    'database': 'biblioteca_db', 
    'user': 'root',
    'password': 'admin'
}

# =============================================
# FUNCIONES PARA CONECTAR A LA BASE DE DATOS
# =============================================

def conectar_bd():
    """Conectar a la base de datos MySQL"""
    conexion = mysql.connector.connect(**config_bd)
    return conexion

def desconectar_bd(conexion):
    """Cerrar la conexión a la base de datos"""
    conexion.close()

# =============================================
# FUNCIONES PARA MOSTRAR INFORMACIÓN
# =============================================

def mostrar_menu_principal():
    """Mostrar el menú principal del sistema"""
    print("\n" + "="*40)
    print("    SISTEMA GESTIÓN DE BIBLIOTECA")
    print("="*40)
    print("1. VER todos los libros")
    print("2. AGREGAR nuevo libro") 
    print("3. EDITAR libro")
    print("4. ELIMINAR libro")
    print("0. SALIR del sistema")
    print("="*40)


def mostrar_menu_edicion():
    while True:

        """Mostrar el menú edicion"""
        print("\n" + "="*40)
        print("    SELECCIONE EL DATO A EDITAR")
        print("="*40)
        print("1. TITULO")
        print("2. AUTOR") 
        print("3. AÑO DE PUBLICACION")
        print("0. CANCELAR")
        print("="*40)

        

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            editar_nombre_libro()
            break
        elif opcion == "2":
            editar_autor_libro()
            break
        elif opcion == "3":
            editar_año_libro()
            break

        elif opcion == "0":
            print("Cancelando")
            break
        else:
            print("❌ Opción inválida, intente nuevamente")

def listar_libros():
    """Mostrar todos los libros en una tabla"""
    # Conectar a la base de datos
    conexion = conectar_bd()
    cursor = conexion.cursor()
    
    # Consulta SQL para obtener todas las herramientas
    
    # Ejecutar la consulta
    cursor.execute('SELECT * FROM libros');
    resultado = cursor.fetchall()
    for persona in resultado:
        print(persona)
        
        # Cerrar conexión
        cursor.close()
        desconectar_bd(conexion)

def agregar_libro():
    """Agregar una nueva herramienta al sistema"""
    print("\n--- AGREGAR NUEVA HERRAMIENTA ---")
    
    # Pedir datos al usuario
    titulo = input("Titulo del libro: ")
    autor = input("autor: ")
    anio = int(input("año en que se publicó: "))
    
    # Mostrar categorías disponibles
    conexion = conectar_bd()
    cursor = conexion.cursor()
    
    # Consulta SQL para insertar nueva herramienta
    sql = "INSERT INTO libros (titulo, autor, anio_publicacion) VALUES (%s, %s, %s)"
    datos = (titulo, autor, anio)
    
    # Ejecutar la inserción
    cursor.execute(sql, datos)
    conexion.commit()  # Guardar cambios en la base de datos
    
    print("libro agregado correctamente")
    
    cursor.close()
    desconectar_bd(conexion)



def editar_nombre_libro():
    """Editar libro en una tabla"""
    # Conectar a la base de datos
    conexion = conectar_bd()
    cursor = conexion.cursor()

    while True:
        try:
            id_a_editar = int(
                input("Ingresa el ID del libro que deseas editar: ")
            )
            break

        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

    
        
    nuevo = input("Ingrese el nuevo titulo del libro: ")
    sql = "UPDATE libros SET titulo = %s WHERE id_libro = %s"


    valor = (nuevo, id_a_editar)
    cursor.execute(sql, valor)
    conexion.commit()

    # Cerrar conexión
    cursor.close()
    desconectar_bd(conexion)

def editar_autor_libro():
    """Editar el autor de un libro en una tabla"""
    # Conectar a la base de datos
    conexion = conectar_bd()
    cursor = conexion.cursor()

    while True:
        try:
            id_a_editar = int(
                input("Ingresa el ID del libro que deseas editar: ")
            )
            break

        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

    
        
    nuevo = input("Ingrese el nuevo autor del libro: ")
    sql = "UPDATE libros SET autor = %s WHERE id_libro = %s"


    valor = (nuevo, id_a_editar)
    cursor.execute(sql, valor)
    conexion.commit()

    # Cerrar conexión
    cursor.close()
    desconectar_bd(conexion)

def editar_año_libro():
    """Editar el autor de un libro en una tabla"""
    # Conectar a la base de datos
    conexion = conectar_bd()
    cursor = conexion.cursor()

    while True:
        try:
            id_a_editar = int(
                input("Ingresa el ID del libro que deseas editar: ")
            )
            break

        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

    
        
    nuevo = int(input("Ingrese el nuevo autor del libro: "))
    sql = "UPDATE libros SET anio_publicacion = %s WHERE id_libro = %s"


    valor = (nuevo, id_a_editar)
    cursor.execute(sql, valor)
    conexion.commit()

    # Cerrar conexión
    cursor.close()
    desconectar_bd(conexion)

def eliminar_libro():
    """Eliminar un registro de una tabla"""
    # Conectar a la base de datos
    conexion = conectar_bd()
    cursor = conexion.cursor()
    
    # Consulta WHERE para no eliminar todo sin querer
    while True:
        try:
            id_a_eliminar = int(
                input("Ingresa el ID del libro que deseas eliminar: ")
            )
            break
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

    sql = "DELETE FROM libros WHERE id_libro = %s"
    valor = (id_a_eliminar,)

    try:
        cursor.execute(sql, valor)
        conexion.commit()

        # cursor.rowcount indica cuántas filas fueron afectadas por la consulta
        if cursor.rowcount > 0:
            print(f"Registro con ID {id_a_eliminar} eliminado exitosamente.")
        else:
            print(f"No se encontró ningún libro con el ID {id_a_eliminar}.")
    
    except mysql.connector.Error as error:
        print(f"Error al eliminar el registro: {error}")
        conexion.rollback()

    finally:
        cursor.close()
        conexion.close()





# =============================================
# PROGRAMA PRINCIPAL
# =============================================

def main():
    """Función principal que ejecuta el sistema"""
    print("🔧 SISTEMA DE GESTIÓN DE PAÑOL")
    print("Conectando a la base de datos...")
    
    # Probar la conexión
    try:
        conexion_prueba = conectar_bd()
        print("✅ Conexión exitosa a la base de datos")
        desconectar_bd(conexion_prueba)
    except:
        print("❌ Error: No se pudo conectar a la base de datos")
        print("Verifique la configuración en el código")
        return
    
    # Bucle principal del programa
    while True:
        # Mostrar menú
        mostrar_menu_principal()
        
        # Leer opción del usuario
        opcion = input("Seleccione una opción: ")
        
        # Ejecutar función según la opción seleccionada
        if opcion == "1":
            listar_libros()
        elif opcion == "2":
            agregar_libro()
        elif opcion == "3":
            mostrar_menu_edicion()
        elif opcion == "4":
            eliminar_libro()
        elif opcion == "0":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida, intente nuevamente")
        
        # Pausa antes de mostrar el menú again
        input("\nPresione Enter para continuar...")

# =============================================
# INICIAR EL PROGRAMA
# =============================================

# Este if asegura que el programa solo se ejecute cuando se llama directamente
if __name__ == "__main__":
    main()