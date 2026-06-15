libros = [{
    "titulo": "Libro troll", "autor": "El Rubius", "estado": True
}]


#funciones extra
def validacion_largo(validacion):
    if len(validacion) >= 3:
        return True
    else:
        return False
    
def disponibilidad(disponible):
    if disponible == True:
        print("Estado: Disponible.")
    else:
        print("Estado: No disponible.")


#1. Agregar libros

def agregar_libros():
    
    print("----Ingreso libro----")
    while True:
        titulo = input("Ingrese titulo libro:\n").capitalize()
        validacion_largo(titulo)
        while validacion_largo(titulo) == False:
            print("El titulo ingresado es muy corto, debe tener al menos 3 caracteres.")
            titulo = input("Ingrese titulo libro:\n").capitalize()
            validacion_largo(titulo)

        if len(libros) > 0:
            for l in libros:
                while l["titulo"] == titulo:
                    print("El titulo ingresado se repite")
                    titulo = input("Ingrese titulo libro:\n").capitalize()
        
        autor = input("Ingrese autor:\n").title()
        validacion_largo(autor)
        while validacion_largo(autor) == False:
            print("El autor ingresado es muy corto, debe tener al menos 3 caracteres.")
            autor = input("Ingrese autor libro:\n").title()
            validacion_largo(autor)
        estado = True
        libro = {
            "titulo":titulo,
            "autor":autor,
            "estado":estado
        }
        libros.append(libro)
        break

#2. Mostrar libros

def mostrar_libros():

    print("----Mostrar libros----")
    if len(libros) <= 0:
        print("\nNo se han registrado libros.\n")
    else:
        for l in libros:
            print(f"Titulo:{l["titulo"]}")
            print(f"Autor:{l["autor"]}")
            disponibilidad(l["estado"])
            print("------------")

#3. Buscar libro

def buscar_libro():
    print("----Buscar libro----")
    if len(libros) <= 0:
        print("\nNo se han registrado libros.\n")
    else:
        buscar = input("Ingrese titulo libro a buscar:\n").capitalize()
        encontrado = False
        for l in libros:
            if l["titulo"] == buscar:
                encontrado = True
                print(f"Titulo:{l["titulo"]}")
                print(f"Autor:{l["autor"]}")
                disponibilidad(l["estado"])
        if encontrado == False:
            print("El titulo ingresado no se encuentra registrado.")                 

#4. Prestar libro

def prestar_libro():
    print("----Prestar libro----")
    if len(libros) <= 0:
        print("\nNo se han registrado libros.\n")
    else:
        prestar = input("Ingrese titulo libro:\n").capitalize()
        prestado = False
        for l in libros:
            if l["titulo"] == prestar:
                if l["estado"] == True:
                    print("Se ha encontrado el libro y se encuentra disponible.")
                    print(f"Titulo:{l["titulo"]}")
                    print(f"Autor:{l["autor"]}")
                    disponibilidad(l["estado"])
                    l["estado"] = False
                    prestado = True
                elif l["estado"] == False:
                    print("Se ha encontrado el libro pero no se encuentra disponible.")
                    print(f"Titulo:{l["titulo"]}")
                    print(f"Autor:{l["autor"]}")
                    disponibilidad(l["estado"])
                    prestado = True
        if prestado == False:
            print("El titulo ingresado no se encuentra registrado.")



#5. Devolver libro

def devolver_libro():
    print("----Devolver libro----")
    devolver = input("Ingrese el título del libro que desea devolver:\n").capitalize()
    validacion_largo(devolver)
    while validacion_largo(devolver) == False:
        devolver = input("El título no puede estar vacío o tener menos de 3 caracteres.\nIngrese nuevamente el titulo:").capitalize()
    
    for l in libros:
        if l["titulo"] == devolver:
            if l["estado"] == False:
                l["estado"] = True
                print(f"El libro {l["titulo"]} ha sido devuelto")
            else:
                print("El libro elegido no estaba prestado.")
        else:
            print(f"El libro {devolver} no se encuentra registrado en la biblioteca.")

#6. Eliminar libro

def eliminar_libro():
    print("----Eliminar libro----")
    eliminar = input("Ingrese el título del libro que desea eliminar: \n").capitalize()
    validacion_largo(eliminar)
    while validacion_largo(eliminar) == False:
        eliminar = input("El título no puede estar vacío o tener menos de 3 caracteres.\nIngrese nuevamente el titulo:").capitalize()
    eliminado = False
    for l in libros:
        if l["titulo"] == eliminar:
            libros.remove(l)
            print(f"El libro {eliminar} ha sido de borrado de la faz de la tierra 💀.")
            eliminado = True
    if eliminado == False:
        print("El libro ingresado no esta registrado en la biblioteca.")
    
#7. Modificar libro

def modificar_libro():
    print("----Modificar libro----")
    modificar = input("Ingrese el libro que desea modificar: \n").capitalize()
    validacion_largo(modificar)
    while validacion_largo(modificar) == False:
        modificar = input("El titulo no puede estar vacio.\nIngresa el título nuevamente: \n").capitalize()
    for l in libros:
        if l["titulo"] == modificar:
            
            nuevo_titulo = input("Ingrese el nuevo título: \n").capitalize()
            validacion_largo(nuevo_titulo)
            while validacion_largo(nuevo_titulo) == False:
                nuevo_titulo = input("El título no puede estar vacío o tener menos de 3 caracteres.\nIngrese el titulo otra vez:\n").capitalize()
            nuevo_autor = input("Ingrese el nuevo autor:\n").capitalize()
            validacion_largo(nuevo_autor)
            while validacion_largo(nuevo_autor) == False:
                nuevo_autor = input("El autor no puede estar vacío o tener menos de 3 caracteres.\nIngrese el autor nuevamente:\n").capitalize()
            
            l["titulo"] = nuevo_titulo
            l["autor"] = nuevo_autor

            print("Libro modificado con éxito.")
        else:
            print(f"El libro {modificar} no se encuentra registrado.")

#8. Mostrar estadísticas

def mostrar_estadisticas():
    print("----Estadísticas biblioteca----")

    disponibles = 0
    prestados = 0
    if len(libros) > 0:
        for l in libros:
            if l["estado"] == True:
                disponibles += 1
            elif l["estado"] == False:
                prestados += 1
    else:
        print("No hay libros registrados.")
    
    print(f"Total de libros: {len(libros)}")
    print(f"Libros disponibles: {disponibles}")
    print(f"Libros prestados: {prestados}")
    
    
    
    
    
    
    
    