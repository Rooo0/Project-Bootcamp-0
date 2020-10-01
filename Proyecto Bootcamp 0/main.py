import db
from model import Usuario
from model import Tarea
from model import Estado



def ListaTarea():
    print("Has Elegido la Opción 1: Mostrar Lista de Tareas")
    tareas = db.session.query(Tarea).all()
    db.session.commit()
    print("¡Tarea Mostrada con Éxito!")

    for tarea in tareas:
        print(tarea.titulo)

def CrearNuevaTarea():
    print("Has Elegido la Opción 2: Crear Nueva Tarea")
    titulo = input ("Escribe el Título de la Nueva Tarea: ")
    descripcion = input ("Escribe su Descripción: ")
    estado = input ("Escribe su Estado: ")
    responsable = input ("Elige su Responsable: ")
    fecha_creacion = input ("Escribe la Fecha de Creación: ")
    tarea = Tarea(titulo, descripcion, estado, responsable, fecha_creacion)
    db.session.add(tarea)
    db.session.commit()
    print("¡Nueva Tarea Creada con Éxito!")

def CambiarEstadoTarea(): 
    print("Has Elegido la Opción 3: Cambiar Estado de una Nueva Tarea")
    tarea_id = input("Escribe el ID de la tarea que quieres editar: ")
    new_estado = input("Escribe su  nuevo Estado: ")
    tarea = db.session.query(Tarea).filter_by(id=tarea_id).first()
    tarea.estado = new_estado
    db.session.commit()
    print("¡Estado Actualizado con Éxito!")

def EditarTarea():
    print("Has Elegido la Opción 4: Editar una Tarea")
    titulo_referencia = input("Escribe el Título de una Tarea Creada: ")
    descripcion_referencia = input("Escribe su Descripción: ")
    estado_referencia = input("Escribe su Estado: ")
    responsable_referencia = input("Escribe su Responsable: ")
    fecha_creacion_referencia = input("Escribe su Fecha de Creación: ")
    titulo = input("Edita el Título de la Tarea Seleccionada: ")
    descripcion = input("Edita su Descripción: ")
    estado = input("Edita su Estado: ")
    responsable = input("Edita su Responsable: ")
    fecha_creacion = input("Edita la Fecha de Creación: ")
    tarea = db.session.query(Tarea).filter_by(titulo=titulo_referencia, descripcion=descripcion_referencia, estado=estado_referencia, responsable=responsable_referencia,fecha_creacion=fecha_creacion_referencia ).first()
    tarea.titulo = titulo
    tarea.descripcion = descripcion
    tarea.estado = estado
    tarea.responsable = responsable
    tarea.fecha_creacion = fecha_creacion
    db.session.commit()
    print(tarea.titulo)
    print("¡Tarea Actualizada con Éxito!")

def BorrarTarea():
    print("Has Elegido la Opción 5: Borrar una Tarea")
    titulo_referencia = input("Escribe una Tarea Creada para Borrarla: ")
    tarea = db.session.query(Tarea).filter_by(titulo=titulo_referencia).first()
    db.session.delete(tarea)
    db.session.commit()
    print("¡Tarea Borrada con Éxito!")

def CrearUsuario():
    print("Has Elegido la Opción 6: Crear Usuario")
    nombre = input("Escribe un Nombre: ")
    apellidos = input("Escribe los Apellidos: ")
    email = input("Escribe el Email: ")
    usuario = Usuario(nombre, apellidos, email)
    db.session.add(usuario)
    db.session.commit()
    print("¡Usuario Registrado con Éxito!")

def BusquedaUsuario():
    print("Has elegido la opción 7: Busqueda de Usuario")
    nombre = input("Escribe un Nombre: ")
    usuario = db.session.query(Usuario).filter_by(nombre=nombre).first()
    print(usuario)
    print("¡Usuario Encontrado con Éxito!")

def ActualizarUsuario():
    print("Has elegido la opción 8: Actualizar Usuario")
    nombre_referencia = input("Escribe un Nombre Registrado: ")
    apellidos_referencia = input("Escribe los Apellidos Registrados: ")
    email_referencia = input("Escribe el Email Registrado: ")
    nombre = input("Escribe un Nuevo Nombre: ")
    apellidos = input("Escribe los Nuevos Apellidos: ")
    email = input("Escribe un Nuevo Email: ")
    usuario = db.session.query(Usuario).filter_by(nombre=nombre_referencia, apellidos=apellidos_referencia, email=email_referencia).first()
    usuario.nombre = nombre
    usuario.apellidos = apellidos
    usuario.email = email
    db.session.commit()
    print(usuario.nombre)
    print("¡Usuario Actualizado y Registrado con Éxito!")

def EliminarUsuario():
    print("Has elegido la opcion 9: Eliminar Usuario")
    nombre_referencia = input("Escribe un Nombre Registrado: ")
    usuario = db.session.query(Usuario).filter_by(nombre=nombre_referencia).first()
    db.session.delete(usuario)
    db.session.commit()
    print("¡Usuario Eliminado con Éxito!")


def SalirTerminal():
    print("Has elegido la opción 10: Salir del Terminal")


menu = True
while menu:
    nombre = input("¿Cual es el Nombre de Usuario? ")
    if nombre == "roo".lower():
        contraseña = input("Por favor, Introduce su Contraseña: ")
        if contraseña == "1234":
            print("Nombre y Contraseña Correctos")
            print("""
    
    ¡Bienvenido a tu Lista de Tareas!

        [1] Mostrar Tareas
        [2] Crear nueva Tarea
        [3] Cambiar estado de una nueva Tarea
        [4] Editar Tarea
        [5] Borrar Tarea
        [6] Crear Usuario
        [7] Busqueda Usuario 
        [8] Actualizar Usuario
        [9] Eliminar Usuario
        [10] Salir del Terminal
    """)
            opciones = input("Elige una de las Opciones Usando su Número Correspondiente: ")
            if(opciones == '1'):
                ListaTarea()
                break
            elif(opciones == '2'):
                CrearNuevaTarea()
                break
            elif(opciones == '3'):
                CambiarEstadoTarea()
                break
            elif(opciones == '4'):
                EditarTarea()
                break
            elif(opciones == '5'):
                BorrarTarea()
                break
            elif(opciones == '6'):
                CrearUsuario()
                break
            elif(opciones == '7'):
                BusquedaUsuario()
                break
            elif(opciones == '8'):
                ActualizarUsuario()
                break
            elif(opciones == '9'):
                EliminarUsuario()
                break
            elif(opciones == '10'):
                SalirTerminal()
                menu = False

                print("¡Cerrando Lista de Tareas!")
            else:
                print("Lo siento, esta opción no existe... ¡Inténtalo de nuevo!")

        if contraseña != "1234":
            contraseña_incorrecta = input("Contraseña incorrecta, ¿Volver a intentar? si/no: ")
            if contraseña_incorrecta == "si".lower():
                menu = True

            else:
                print("Gracias por intentar logear, hasta la próxima")
                quit()

    if nombre != "roo".lower():
        nombre_incorrecto = input("Usuario incorrecto, quieres volver a intentar? si/no: ")
        if nombre_incorrecto == "si".lower():
            menu == True
        else:
            print("Gracias por intentarlo, hasta la próxima")
            quit()
