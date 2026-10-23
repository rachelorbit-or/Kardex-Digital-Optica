"""Ordenamiento de pacientes por apellido (Algoritmo 2 del informe): metodo de burbuja."""

import datos
import validaciones


def intercambiar(i, j):
    """Intercambia las posiciones i y j en los 9 arreglos a la vez.

    Si se movieran solo los nombres, los demas datos quedarian con la persona equivocada.
    """
    for arreglo in datos.todos_los_arreglos():
        arreglo[i], arreglo[j] = arreglo[j], arreglo[i]


def ordenar_por_nombre():
    """Ordena los pacientes por apellido (y nombre) de la A a la Z con el metodo de burbuja.

    Si en una pasada no hubo ningun cambio, ya esta ordenado y termina antes.
    No distingue mayusculas ni tildes. Devuelve la cantidad de comparaciones hechas.
    """
    n = datos.cantidad()
    comparaciones = 0
    for i in range(n - 1):
        hubo_cambio = False
        for j in range(n - 1 - i):
            comparaciones = comparaciones + 1
            actual = validaciones.normalizar_texto(datos.nombres[j])
            siguiente = validaciones.normalizar_texto(datos.nombres[j + 1])
            if actual > siguiente:
                intercambiar(j, j + 1)
                hubo_cambio = True
        if not hubo_cambio:
            break
    return comparaciones
