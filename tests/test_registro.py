"""Pruebas de registro.py.  Ejecutar:  python tests/test_registro.py"""

from utilidades_prueba import verificar, titulo, resumen
import datos
import registro

VALIDO = ("70123456", "Quispe Rojas, Ana", "34", "987654321", "-2.00/-1.00/90",
          "-1.75/0/0", "62", "Policarbonato", "05/10/2026")


def con(**cambios):
    """Devuelve el paciente valido cambiando solo los campos indicados por posicion (c0..c8)."""
    datos_paciente = list(VALIDO)
    for clave, valor in cambios.items():
        datos_paciente[int(clave[1:])] = valor
    return tuple(datos_paciente)


datos.limpiar_pacientes()

titulo("Registro valido")
ok, msg = registro.registrar_paciente(*VALIDO)
verificar("el paciente valido se registra", ok)
verificar("el mensaje incluye la serie de precio", "Primera serie" in msg)
verificar("hay 1 paciente", datos.cantidad() == 1)
verificar("los 9 arreglos tienen la misma longitud",
          len({len(a) for a in datos.todos_los_arreglos()}) == 1)
verificar("la edad se guarda como numero", datos.edades[0] == 34)
verificar("la DIP se guarda como numero", datos.dips[0] == 62)
verificar("los espacios sobrantes se quitan",
          registro.registrar_paciente(*[x + "  " for x in con(c0="45871236", c1="Torres Diaz, Luis")])[0]
          and datos.nombres[1] == "Torres Diaz, Luis")

titulo("Rechazos: cada campo invalido")
casos = [
    ("DNI de 7 digitos", con(c0="7012345")),
    ("nombre sin coma", con(c0="11111111", c1="Alva Rosa")),
    ("edad 150", con(c0="11111111", c2="150")),
    ("telefono de 5 digitos", con(c0="11111111", c3="98765")),
    ("medida OD con cilindro 7", con(c0="11111111", c4="0/7/0")),
    ("medida OI con eje 200", con(c0="11111111", c5="0/-1/200")),
    ("DIP 20", con(c0="11111111", c6="20")),
    ("material vacio", con(c0="11111111", c7="")),
    ("fecha 31/04/2026", con(c0="11111111", c8="31/04/2026")),
]
for descripcion, paciente in casos:
    ok, msg = registro.registrar_paciente(*paciente)
    verificar("rechaza " + descripcion, not ok)
verificar("ningun rechazado quedo guardado (siguen 2 pacientes)", datos.cantidad() == 2)

titulo("DNI repetido")
ok, msg = registro.registrar_paciente(*con(c1="Otra Persona, Maria"))
verificar("rechaza un DNI que ya existe", not ok and "ya está registrado" in msg)
verificar("sigue habiendo 2 pacientes", datos.cantidad() == 2)

titulo("Orden de las validaciones (solo se informa el primer error)")
ok, msg = registro.registrar_paciente(*con(c0="123", c2="999"))
verificar("con DNI y edad invalidos, el mensaje es el del DNI", not ok and "DNI" in msg)

titulo("Series de precio")
verificar("cilindro 2.00 es Primera serie", registro.calcular_serie("0/-2/0", "0/0/0") == "Primera serie")
verificar("cilindro 2.25 es Segunda serie", registro.calcular_serie("0/-2.25/0", "0/0/0") == "Segunda serie")
verificar("cilindro 4.00 es Segunda serie", registro.calcular_serie("0/-4/0", "0/0/0") == "Segunda serie")
verificar("cilindro 4.25 es Tercera serie", registro.calcular_serie("0/-4.25/0", "0/0/0") == "Tercera serie")
verificar("cilindro 6.00 es Tercera serie", registro.calcular_serie("0/-6/0", "0/0/0") == "Tercera serie")
verificar("manda el ojo con mayor cilindro", registro.calcular_serie("0/-0.5/0", "0/-3/90") == "Segunda serie")
verificar("el signo del cilindro no importa", registro.calcular_serie("0/3/0", "0/0/0") == "Segunda serie")
verificar("la miopia no cambia la serie", registro.calcular_serie("-5/0/0", "-4.5/0/0") == "Primera serie")

titulo("buscar_indice")
verificar("encuentra un valor existente", registro.buscar_indice([5, 7, 9], 7) == 1)
verificar("devuelve -1 si no existe", registro.buscar_indice([5, 7, 9], 4) == -1)
verificar("devuelve -1 en un arreglo vacio", registro.buscar_indice([], 1) == -1)

resumen()
