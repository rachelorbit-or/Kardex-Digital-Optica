"""Guardar y cargar los pacientes en un archivo de texto (un paciente por linea, datos separados por ;)."""

import os
import time

import datos
import validaciones

RUTA_POR_DEFECTO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "pacientes.txt")


def guardar_en_archivo(ruta=RUTA_POR_DEFECTO):
    """Guarda todos los pacientes. Devuelve la cantidad guardada.

    Primero escribe en un archivo temporal y luego lo reemplaza, para no perder
    los datos si el programa se cierra a la mitad de guardar.
    """
    ruta_temporal = ruta + ".tmp"
    with open(ruta_temporal, "w", encoding="utf-8") as archivo:
        for i in range(datos.cantidad()):
            linea = ";".join([datos.dnis[i], datos.nombres[i], str(datos.edades[i]),
                              datos.telefonos[i], datos.medidas_od[i], datos.medidas_oi[i],
                              str(datos.dips[i]), datos.materiales[i], datos.fechas[i]])
            archivo.write(linea + "\n")
    os.replace(ruta_temporal, ruta)
    return datos.cantidad()


def linea_valida(partes):
    """Revisa que las 9 partes de una linea cumplan las mismas reglas del registro."""
    if len(partes) != 9:
        return False
    dni, nombre, edad, telefono, med_od, med_oi, dip, material, fecha = partes
    return (validaciones.validar_dni(dni) and validaciones.validar_nombre_completo(nombre)
            and validaciones.validar_edad(edad) and validaciones.validar_telefono(telefono)
            and validaciones.validar_medida_ojo(med_od) and validaciones.validar_medida_ojo(med_oi)
            and validaciones.validar_dip(dip) and validaciones.validar_texto(material)
            and validaciones.validar_fecha(fecha))


def cargar_desde_archivo(ruta=RUTA_POR_DEFECTO):
    """Carga los pacientes del archivo (reemplaza lo que haya en memoria).

    Devuelve la cantidad de lineas dañadas o repetidas que se omitieron.
    Si el archivo no existe, no hace nada y devuelve 0.
    """
    datos.limpiar_pacientes()
    omitidas = 0
    if not os.path.exists(ruta):
        return 0
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            partes = linea.split(";")
            if not linea_valida(partes) or partes[0] in datos.dnis:
                omitidas = omitidas + 1
                continue
            datos.agregar_paciente(partes[0], partes[1], int(partes[2]), partes[3], partes[4],
                                   partes[5], int(partes[6]), partes[7], partes[8])
    return omitidas


def crear_respaldo(carpeta_destino):
    """Guarda una copia de los pacientes en "carpeta_destino" (por ejemplo una USB).

    Devuelve (True, ruta_del_respaldo) o (False, motivo).
    """
    carpeta_destino = carpeta_destino.strip().strip('"')
    if not os.path.isdir(carpeta_destino):
        return False, "La carpeta '" + carpeta_destino + "' no existe."
    nombre_archivo = "respaldo_pacientes_" + time.strftime("%Y%m%d_%H%M%S") + ".txt"
    ruta = os.path.join(carpeta_destino, nombre_archivo)
    try:
        guardar_en_archivo(ruta)
    except OSError as error:
        return False, "No se pudo crear el respaldo: " + str(error)
    return True, ruta
