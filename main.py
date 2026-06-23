# main.py
# Programa principal que importa y utiliza las funciones del módulo logica_mision.

from logica_mision import *

if __name__ == "__main__":
    # 1. Llamar a configurar_nave usando argumentos por nombre (cambiando el orden)
    configurar_nave(estado="Dañado", nombre="Apolo", modelo="Aventurero")

    # 2. Obtener coordenadas y desempaquetar (unpacking) la tupla
    x, y, z = obtener_coordenadas()
    print(f"Coordenadas actuales: X = {x}, Y = {y}, Z = {z}")

    # 3. Registrar tripulantes con 4 nombres (funciona *args)
    registrar_tripulantes("Juan", "María", "Pedro", "Laura")
