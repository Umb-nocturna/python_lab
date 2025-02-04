#libraries
import sqlite3

#Object Class
class Heroe:
    def __init__(self, nombre: str, codigo: str, fuerza: int, destreza: int, inteligencia: int):
        self.nombre = nombre
        self.codigo = codigo
        self.fuerza = fuerza
        self.destreza = destreza
        self.inteligencia = inteligencia

    def __str__(self):
        return f"Heroe({self.nombre}, {self.codigo}, F:{self.fuerza}, D:{self.destreza}, I:{self.inteligencia})"

#Functions
    
def guardar_heroe(heroe):
    """
    Función para guardar un héroe en la base de datos SQLite.
    """
    try:
        #conexion = sqlite3.connect("heroes.db")
        #cursor = conexion.cursor()
        ## Insertar datos en la tabla
        cursor.execute("""
            INSERT INTO heroes (nombre, codigo, fuerza, destreza, inteligencia)
            VALUES (?, ?, ?, ?, ?);
        """, (heroe.nombre, heroe.codigo, heroe.fuerza, heroe.destreza, heroe.inteligencia))

        #conexion.commit()
        print(f"Héroe '{heroe.nombre}' guardado con éxito.")

    except sqlite3.IntegrityError:
        print("Error: El código del héroe ya existe en la base de datos.")
    except Exception as e:
        print("Error al guardar el héroe:", e)
    finally:
        cursor.close()
        conexion.close()


# main code
if __name__ == "__main__":
    print("Hello Wolrd!")

