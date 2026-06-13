libros = [{
    "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "estado": "Prestado"
}]
flag1 = True


#1. Agregar libros

def agregar_libros():
    
    print("----Ingreso libro----")
    while flag1:
        titulo = input("Ingrese titulo libro:\n")
        if len(libros) > 0:
            for l in libros:
                if l["titulo"] == titulo:
                    print("El nombre ingresado se repite ")
        else:
            autor = input("Ingrese autor:")
            estado = "Disponible"
            libro = {
                "titulo":titulo,
                "autor":autor,
                "estado":estado
            }
            flag1 = False

#2. Mostrar libros

def mostrar_libros():
    print("----Libros registrados----")
    for l in libros:
        print(f"----Libro---")
        print(f"Titulo: {l["titulo"]}")
        print()
        print()
        print()
        
#3. Buscar libro

def buscar_libro():
    print("opcion3")

#4. Prestar libro

def prestar_libro():
    print("opcion4")

#5. Devolver libro

def devolver_libro():
    devolver = input("Ingrese el título del libro que desea devolver")
    while len(devolver) < 3:
        devolver = input("El nombre no puede estar vacío o tener menos de 2 caracteres.\nIngrese nuevamente el titulo:")
    
    for l in libros:
        if l["titulo"] == devolver:
            if l["estado"] == "Prestado":
                l["estado"] = "Disponible"
                print(f"El libro {l["titulo"]} ha sido devuelto")
            else:
                print("El libro elegido no estaba prestado.")
        else:
            print(f"El libro {devolver} no se encuentra registrado en la biblioteca.")

#6. Eliminar libro

def eliminar_libro():
    eliminar = input("Ingrese el título del libro que desea eliminar")
    while len(eliminar) < 3:
        eliminar = input("El nombre no puede estar vacío o tener menos de 2 caracteres.\nIngrese nuevamente el titulo:")
    for l in libros:
        if l["titulo"] == eliminar:
            libros.remove(l)
            print(f"El libro {eliminar} ha sido de borrado de la faz de la tierra 💀.")
        else:
            print("El libro ingresado no esta registrado en la biblioteca.")
    
#7. Modificar libro

def modificar_libro():
    print("opcion7")

#8. Mostrar estadísticas

def mostrar_estadisticas():
    print("opcion8")
    
    
    
    
    
    
    
    
    
    
    