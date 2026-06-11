libros = []
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
                "nombre":titulo,
                "autor":autor,
                "estado":estado
            }
            flag1 = False

#2. Mostrar libros

def mostrar_libros():

    print("----Libros registrados----")
    for l in libros:
        print(f"----Libro---")
        print(f"Titulo: ")
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
    
    
    
    
    
    
    
    
    
    
    