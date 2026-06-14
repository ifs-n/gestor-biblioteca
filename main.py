import os
import time
from functions import *

os.system("clear")
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
        os.system("cls")
        agregar_libros()
        time.sleep(2)
    elif opcion == 2:
        os.system("cls")
        mostrar_libros()
        time.sleep(2)
    elif opcion == 3:
        os.system("cls")
        buscar_libro()
        time.sleep(2)
    elif opcion == 4:
        os.system("cls")
        prestar_libro()
        time.sleep(2)
    elif opcion == 5:
        os.system("cls")
        devolver_libro()
        time.sleep(2)
        time.sleep(2)
    elif opcion == 6:
        os.system("cls")
        eliminar_libro()
        time.sleep(2)
    elif opcion == 7:
        os.system("cls")
        modificar_libro()
        time.sleep(2)
    elif opcion == 8:
        os.system("cls")
        mostrar_estadisticas()
        time.sleep(2)
    elif opcion == 9:
        banderita = False
    else:
        print("Opción Inválida")



