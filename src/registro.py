"""Registro de pacientes (Algoritmo 3 del informe): valida y agrega un paciente nuevo."""

import datos
import validaciones


def buscar_indice(arreglo, valor):
    """Busqueda secuencial: devuelve la posicion de "valor" en el arreglo, o -1 si no esta."""
    for i in range(len(arreglo)):
        if arreglo[i] == valor:
            return i
    return -1


def calcular_serie(medida_od, medida_oi):
    """Serie de precio segun el mayor cilindro (en valor absoluto) de los dos ojos.

    Primera serie: hasta 2 | Segunda: de 2.25 a 4 | Tercera: de 4.25 a 6.
    Recibe las medidas ya validadas.
    """
    _, _, cilindro_od, _ = validaciones.obtener_partes_medida(medida_od)
    _, _, cilindro_oi, _ = validaciones.obtener_partes_medida(medida_oi)
    cilindro = max(abs(cilindro_od), abs(cilindro_oi))
    if cilindro <= 2:
        return "Primera serie"
    elif cilindro <= 4:
        return "Segunda serie"
    else:
        return "Tercera serie"


def registrar_paciente(dni, nombre, edad, telefono, medida_od, medida_oi, dip, material, fecha):
    """Valida y registra un paciente. Todos los datos llegan como TEXTO.

    Devuelve (True, mensaje) si se registro o (False, motivo) si fue rechazado.
    Solo se muestra el PRIMER error encontrado, en este orden.
    """
    # Quitar espacios sobrantes
    dni = dni.strip()
    nombre = nombre.strip()
    edad = edad.strip()
    telefono = telefono.strip()
    medida_od = medida_od.strip()
    medida_oi = medida_oi.strip()
    dip = dip.strip()
    material = material.strip()
    fecha = fecha.strip()

    # Validaciones (todos los datos son obligatorios)
    if not validaciones.validar_dni(dni):
        return False, "El DNI debe tener 8 dígitos."
    if not validaciones.validar_nombre_completo(nombre):
        return False, "El nombre debe tener el formato: Apellidos, Nombres."
    if not validaciones.validar_edad(edad):
        return False, "La edad debe ser un número entero entre 1 y 110."
    if not validaciones.validar_telefono(telefono):
        return False, "El teléfono debe tener 9 dígitos."
    if not validaciones.validar_medida_ojo(medida_od):
        return False, ("La medida del ojo derecho no es válida. Formato: esfera/cilindro/eje "
                       "(esfera de -20 a 20, cilindro hasta 6, eje de 0 a 180).")
    if not validaciones.validar_medida_ojo(medida_oi):
        return False, ("La medida del ojo izquierdo no es válida. Formato: esfera/cilindro/eje "
                       "(esfera de -20 a 20, cilindro hasta 6, eje de 0 a 180).")
    if not validaciones.validar_dip(dip):
        return False, "La distancia interpupilar debe ser un entero entre 40 y 80 mm."
    if not validaciones.validar_texto(material):
        return False, "El material no puede estar vacío ni contener ';'."
    if not validaciones.validar_fecha(fecha):
        return False, "La fecha debe tener el formato dd/mm/aaaa y ser una fecha real."

    # DNI repetido
    if buscar_indice(datos.dnis, dni) != -1:
        return False, "Ese DNI ya está registrado."

    datos.agregar_paciente(dni, nombre, int(edad), telefono, medida_od, medida_oi,
                           int(dip), material, fecha)
    serie = calcular_serie(medida_od, medida_oi)
    return True, "Paciente registrado. Serie de precio: " + serie + "."
