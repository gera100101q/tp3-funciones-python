# tp3-funciones-python# TP3 - Funciones en Python

## ¿Qué es un módulo en Python?
Un **módulo** en Python es un archivo que contiene definiciones y declaraciones de funciones, clases o variables. Permite organizar el código en partes reutilizables, facilita el mantenimiento y promueve la separación de responsabilidades.

## Funciones creadas

- **`calcular_combustible(distancia, consumo_por_km)`**  
  Recibe la distancia y el consumo por kilómetro, y **retorna** el producto de ambos. Útil para estimar el combustible necesario en un viaje espacial.

- **`configurar_nave(nombre, modelo, estado)`**  
  Configura una nave recibiendo los datos por **nombre** (permite cambiar el orden). Los parámetros `modelo` y `estado` tienen valores por defecto (`"Explorador"` y `"Óptimo"`). Imprime un mensaje de confirmación.

- **`obtener_coordenadas()`**  
  No recibe argumentos y **retorna una tupla** con tres valores (X, Y, Z) que representan la posición actual en el espacio.

- **`registrar_tripulantes(*args)`**  
  Acepta un número variable de nombres de tripulantes (usando `*args`) y los lista mediante un bucle `for`. Muestra quiénes están a bordo.
