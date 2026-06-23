# logica_mision.py
# Módulo que contiene las funciones auxiliares para la misión espacial.

def calcular_combustible(distancia, consumo_por_km):
    """
    Calcula la cantidad de combustible necesaria.
    Recibe distancia y consumo por km, retorna la multiplicación de ambos.
    """
    return distancia * consumo_por_km

def configurar_nave(nombre, modelo="Explorador", estado="Óptimo"):
    """
    Configura una nave con nombre, modelo y estado.
    Parámetros por nombre y valores por defecto.
    Imprime un mensaje de confirmación.
    """
    print(f"Nave configurada: {nombre}, modelo: {modelo}, estado: {estado}")

def obtener_coordenadas():
    """
    Retorna una tupla con tres coordenadas (X, Y, Z). 
    En este ejemplo se devuelven valores fijos para simulación.
    """
    return (10, 20, 30)

def registrar_tripulantes(*args):
    """
    Recibe una cantidad variable de nombres de tripulantes.
    Itera e imprime la lista de tripulantes a bordo.
    """
    print("Tripulantes a bordo:")
    for tripulante in args:
        print(f"- {tripulante}")
