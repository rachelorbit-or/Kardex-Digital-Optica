"""Muestra pacientes en pantalla."""

import datos
import registro


def formatear_paciente(i):
    """Devuelve el texto (dos lineas) con los datos del paciente en la posicion i."""
    serie = registro.calcular_serie(datos.medidas_od[i], datos.medidas_oi[i])
    linea1 = ("DNI " + datos.dnis[i] + " | " + datos.nombres[i] + " | "
              + str(datos.edades[i]) + " años | Tel. " + datos.telefonos[i])
    linea2 = ("    Visita: " + datos.fechas[i] + " | OD " + datos.medidas_od[i]
              + " | OI " + datos.medidas_oi[i] + " | DIP " + str(datos.dips[i])
              + " mm | " + datos.materiales[i] + " | " + serie)
    return linea1 + "\n" + linea2


def listar_pacientes(posiciones=None):
    """Imprime los pacientes de la lista "posiciones" (o todos si no se indica)."""
    if posiciones is None:
        posiciones = list(range(datos.cantidad()))
    if len(posiciones) == 0:
        print("No hay pacientes para mostrar.")
        return
    for i in posiciones:
        print(formatear_paciente(i))
