"""Datos del sistema: los 9 arreglos paralelos (listas) donde se guardan los pacientes.

Idea clave: la MISMA posicion "i" en los 9 arreglos corresponde al MISMO paciente.
Ejemplo: dnis[0], nombres[0], edades[0]... son los datos del primer paciente.

Los otros modulos usan estos arreglos asi:   import datos   ->   datos.dnis
(no se usa "from datos import dnis" porque entonces se perderia el vinculo
cuando limpiar_pacientes() vacia las listas).
"""

dnis = []         # texto, 8 digitos
nombres = []      # texto, "Apellidos, Nombres"
edades = []       # entero
telefonos = []    # texto, 9 digitos
medidas_od = []   # texto, "esfera/cilindro/eje" del ojo derecho
medidas_oi = []   # texto, "esfera/cilindro/eje" del ojo izquierdo
dips = []         # entero, distancia interpupilar en mm
materiales = []   # texto, material del lente
fechas = []       # texto, dd/mm/aaaa


def todos_los_arreglos():
    """Devuelve la lista con los 9 arreglos (sirve para recorrerlos juntos)."""
    return [dnis, nombres, edades, telefonos, medidas_od, medidas_oi,
            dips, materiales, fechas]


def cantidad():
    """Cantidad de pacientes registrados."""
    return len(dnis)


def agregar_paciente(dni, nombre, edad, telefono, medida_od, medida_oi, dip, material, fecha):
    """Agrega un paciente al final de los 9 arreglos (no valida: eso lo hace registro.py)."""
    dnis.append(dni)
    nombres.append(nombre)
    edades.append(edad)
    telefonos.append(telefono)
    medidas_od.append(medida_od)
    medidas_oi.append(medida_oi)
    dips.append(dip)
    materiales.append(material)
    fechas.append(fecha)


def limpiar_pacientes():
    """Vacia los 9 arreglos."""
    for arreglo in todos_los_arreglos():
        arreglo.clear()
