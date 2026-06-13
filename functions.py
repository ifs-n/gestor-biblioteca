libros = []


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
            print("El tirulo ingresado no se encuentra registrado.")



#5. Devolver libro

def devolver_libro():
    print("opcion5")

#6. Eliminar libro

def eliminar_libro():
    print("opcion6")

#7. Modificar libro

def modificar_libro():
    print("opcion7")

#8. Mostrar estadísticas

def mostrar_estadisticas():
    print("opcion8")










