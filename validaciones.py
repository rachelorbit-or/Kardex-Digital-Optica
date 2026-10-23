"""Validaciones: revisan cada dato ANTES de aceptarlo.

Todas las funciones validar_* reciben el dato como TEXTO (tal como lo escribe el usuario)
y devuelven True si es valido o False si no.
"""

DIGITOS = "0123456789"


# ---------------------------------------------------------------- utilidades de texto

def es_solo_digitos(texto):
    """True si el texto no esta vacio y todos sus caracteres son digitos."""
    if len(texto) == 0:
        return False
    for caracter in texto:
        if caracter not in DIGITOS:
            return False
    return True


def normalizar_texto(texto):
    """Pasa a minusculas, quita espacios de los extremos y quita tildes y la ñ.

    Sirve para comparar y ordenar sin que importen mayusculas ni tildes
    ("Perez" = "pérez" = "PEREZ").
    """
    texto = texto.strip().lower()
    con_tilde = "áéíóúüñ"
    sin_tilde = "aeiouun"
    resultado = ""
    for caracter in texto:
        posicion = con_tilde.find(caracter)
        if posicion != -1:
            resultado = resultado + sin_tilde[posicion]
        else:
            resultado = resultado + caracter
    return resultado


def apellido_de(nombre_completo):
    """De "Quispe Rojas, Ana" devuelve "Quispe Rojas" (lo que esta antes de la coma)."""
    posicion_coma = nombre_completo.find(",")
    if posicion_coma == -1:
        return nombre_completo.strip()
    return nombre_completo[:posicion_coma].strip()


# ---------------------------------------------------------------- validaciones simples

def validar_dni(texto):
    """El DNI debe tener exactamente 8 digitos."""
    return len(texto) == 8 and es_solo_digitos(texto)


def validar_telefono(texto):
    """El telefono debe tener exactamente 9 digitos."""
    return len(texto) == 9 and es_solo_digitos(texto)


def validar_texto(texto):
    """Texto no vacio y sin ';' (porque ';' separa los datos en el archivo)."""
    return len(texto.strip()) > 0 and ";" not in texto


def validar_nombre_completo(texto):
    """Formato "Apellidos, Nombres": una sola coma, con texto antes y despues."""
    if not validar_texto(texto):
        return False
    if texto.count(",") != 1:
        return False
    posicion_coma = texto.find(",")
    apellidos = texto[:posicion_coma].strip()
    nombres = texto[posicion_coma + 1:].strip()
    return len(apellidos) > 0 and len(nombres) > 0


def validar_edad(texto):
    """Edad: numero entero entre 1 y 110."""
    if not es_solo_digitos(texto):
        return False
    return 1 <= int(texto) <= 110


def validar_dip(texto):
    """Distancia interpupilar en mm: entero entre 40 y 80."""
    if not es_solo_digitos(texto):
        return False
    return 40 <= int(texto) <= 80


# ---------------------------------------------------------------- medidas

def convertir_decimal(texto):
    """Convierte texto a decimal. Acepta coma o punto ("-1,50" o "-1.50").

    Devuelve (True, valor) o (False, 0.0) si no es un numero valido.
    """
    texto = texto.strip().replace(",", ".")
    if texto == "":
        return False, 0.0
    try:
        valor = float(texto)
    except ValueError:
        return False, 0.0
    # float() acepta "nan" e "inf": los descartamos
    if valor != valor or valor in (float("inf"), float("-inf")):
        return False, 0.0
    return True, valor


def obtener_partes_medida(texto):
    """Separa "esfera/cilindro/eje" y devuelve (True, esfera, cilindro, eje) o (False, 0, 0, 0)."""
    partes = texto.split("/")
    if len(partes) != 3:
        return False, 0.0, 0.0, 0
    ok_esfera, esfera = convertir_decimal(partes[0])
    ok_cilindro, cilindro = convertir_decimal(partes[1])
    texto_eje = partes[2].strip()
    if not ok_esfera or not ok_cilindro or not es_solo_digitos(texto_eje):
        return False, 0.0, 0.0, 0
    return True, esfera, cilindro, int(texto_eje)


def validar_medida_ojo(texto):
    """Medida de un ojo con formato "esfera/cilindro/eje", por ejemplo "-2.00/-1.00/90".

    Reglas: esfera entre -20 y 20; cilindro de 6 como maximo (en valor absoluto);
    eje entero entre 0 y 180 (lo dijo el dueño en la entrevista).
    """
    ok, esfera, cilindro, eje = obtener_partes_medida(texto)
    if not ok:
        return False
    if esfera < -20 or esfera > 20:
        return False
    if abs(cilindro) > 6:
        return False
    if eje < 0 or eje > 180:
        return False
    return True


# ---------------------------------------------------------------- fecha

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0


def dias_del_mes(mes, anio):
    if mes == 2:
        return 29 if es_bisiesto(anio) else 28
    if mes in (4, 6, 9, 11):
        return 30
    return 31


def validar_fecha(texto):
    """Fecha con formato dd/mm/aaaa y que exista en el calendario (anio entre 2000 y 2100)."""
    partes = texto.split("/")
    if len(partes) != 3:
        return False
    dia, mes, anio = partes
    if len(dia) != 2 or len(mes) != 2 or len(anio) != 4:
        return False
    if not (es_solo_digitos(dia) and es_solo_digitos(mes) and es_solo_digitos(anio)):
        return False
    dia, mes, anio = int(dia), int(mes), int(anio)
    if anio < 2000 or anio > 2100:
        return False
    if mes < 1 or mes > 12:
        return False
    return 1 <= dia <= dias_del_mes(mes, anio)
