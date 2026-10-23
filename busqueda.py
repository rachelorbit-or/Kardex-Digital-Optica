"""Busqueda de pacientes (Algoritmo 1 del informe): busqueda secuencial."""

import datos
import validaciones


def buscar_por_dni(dni):
    """Devuelve la posicion del paciente con ese DNI, o -1 si no existe.

    Recorre los arreglos desde el inicio y se detiene en cuanto lo encuentra.
    """
    dni = dni.strip()
    i = 0
    while i < datos.cantidad():
        if datos.dnis[i] == dni:
            return i
        i = i + 1
    return -1


def buscar_por_apellido(texto):
    """Devuelve la LISTA de posiciones de los pacientes cuyo apellido empieza con "texto".

    No importan mayusculas ni tildes. Puede haber varios con el mismo apellido,
    por eso recorre todos los pacientes y devuelve todas las coincidencias.
    """
    buscado = validaciones.normalizar_texto(texto)
    coincidencias = []
    if buscado == "":
        return coincidencias
    for i in range(datos.cantidad()):
        apellido = validaciones.normalizar_texto(validaciones.apellido_de(datos.nombres[i]))
        if apellido.startswith(buscado):
            coincidencias.append(i)
    return coincidencias
