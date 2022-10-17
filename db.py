from sqlite3 import connect
from alumno import Alumno

BDD_NOMBRE = 'app.db'
def crearBDD():
    db = connect(BDD_NOMBRE)
    cursor = db.cursor()
    cursor.execute(
        """
        DROP TABLE IF EXISTS Alumnos;
        """
    )
    cursor.execute("""
    CREATE TABLE Alumnos (
        id       INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre   TEXT    NOT NULL,
        apellido TEXT    NOT NULL
    );
    """)
    db.commit()
    cursor.close()
    db.close

def insertarAlumno(alumno:Alumno):
    db = connect(BDD_NOMBRE)
    cursor = db.cursor()
    cursor.execute(
        f"""
        INSERT INTO Alumnos (nombre,apellido)
        VALUES(
        '{alumno.nombre}',
        '{alumno.apellido}'
        );
        """
    )
    db.commit()
    cursor.close()
    db.close()

def buscarAlumnoPorNombre(nombre):
    """
    Recibe nombre de alumno como parámetro
    y devuelve una lista de tipo Alumno() 
    con todos los alumnos con ese nombre
    """
    db = connect(BDD_NOMBRE)
    cursor = db.cursor()
    queryResults = cursor.execute(
        f"""
        SELECT * FROM Alumnos
        WHERE nombre = '{nombre}';
        """
    ).fetchall()
    cursor.close()
    db.close()
    resultado = []
    for result in queryResults:
        resultado.append(
            Alumno(result[1],result[2],result[0])
        )
    return(resultado)