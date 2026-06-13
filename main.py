import os
import time
from functions import *

os.system("cls")

banderita = True

while True:
    print("===== BIBLIOTECA =====\n")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Eliminar libro")
    print("7. Modificar libro")
    print("8. Mostrar estadísticas")
    print("9. Salir")

    opcion = int(input("Ingrese una opción:\n"))

    if opcion == 1:
        agregar_libros()
    elif opcion == 2:
        mostrar_libros()
    elif opcion == 3:
        buscar_libro()
    elif opcion == 4:
        prestar_libro()
    elif opcion == 5:
        os.system("cls")
        devolver_libro()
        time.sleep(2)
    elif opcion == 6:
        os.system("cls")
        eliminar_libro()
        time.sleep(2)
    elif opcion == 7:
        modificar_libro()
    elif opcion == 8:
        mostrar_estadisticas()
    elif opcion == 9:
        banderita = False
    else:
        print("Opción Inválida")



