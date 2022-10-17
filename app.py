from alumno import Alumno
from db import crearBDD,insertarAlumno,buscarAlumnoPorNombre

# se crean nombres y apellidos:
nombres_apellidos = [
    ('Esteban','Cabarcas'),('Alicia','Alcalá'),('Bob','Barba'),
    ('Carlos','Cable'),('Dolores','Delicada'),('Ernesto','Erizo'),
    ('Fernanda','Flores'),('Gisela','Guerra'),('Hector','Herrero'),
    ('Fernanda','Flatulencia'),('Gisela','Guarra'),('Hector','Hediondez')
]
# se crea una lista con objetos de la clase alumno
alumnos = []
for alumno in nombres_apellidos:
    alumnos.append(Alumno(alumno[0].capitalize(),alumno[1].capitalize()))

# se crea la base de datos, si ya existe borra la tabla Alumno y crea una nueva.
crearBDD()

# se insertan los alumnos en la base de datos.
for alumno in alumnos:
    insertarAlumno(alumno)
    
# se solicita por consola un nombre de alumno a buscar en la base de datos:
nombre = input('Escriba nombre de alumno a buscar: ').capitalize()
resultado = buscarAlumnoPorNombre(nombre)
if resultado:
    print(f"\nDatos de alumnos con nombre '{nombre.capitalize()}':")
    for alumno in resultado:
        print(f"\nID: {alumno.id}, Nombre: {alumno.nombre}, Apellido: {alumno.apellido}")

else: print(f'\nUsuario con nombre "{nombre}" no encontrado.')