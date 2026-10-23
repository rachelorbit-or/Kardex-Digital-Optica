"""Pruebas de ordenamiento.py.  Ejecutar:  python tests/test_ordenamiento.py"""

from utilidades_prueba import verificar, titulo, resumen
import datos
import ordenamiento
import registro


def cargar(lista):
    datos.limpiar_pacientes()
    for dni, nombre, edad in lista:
        registro.registrar_paciente(dni, nombre, edad, "987654321", "-1/0/0", "-1/0/0", "62", "CR-39", "05/10/2026")


titulo("Ordenar pacientes desordenados")
cargar([("45871236", "Torres Diaz, Luis", "52"), ("70123456", "Quispe Rojas, Ana", "34"),
        ("71239854", "Vega Salas, Marta", "19"), ("73345512", "Alva Ruiz, Rosa", "29"),
        ("42003317", "Castro Lima, Jose", "61")])
comparaciones = ordenamiento.ordenar_por_nombre()
verificar("quedan ordenados A-Z por apellido",
          datos.nombres == ["Alva Ruiz, Rosa", "Castro Lima, Jose", "Quispe Rojas, Ana",
                            "Torres Diaz, Luis", "Vega Salas, Marta"])
verificar("el DNI se movio junto con su nombre", datos.dnis == ["73345512", "42003317", "70123456", "45871236", "71239854"])
verificar("la edad se movio junto con su nombre", datos.edades == [29, 61, 34, 52, 19])
verificar("los 9 arreglos siguen del mismo largo", len({len(a) for a in datos.todos_los_arreglos()}) == 1)
verificar("hizo 10 comparaciones (n(n-1)/2 con n=5)", comparaciones == 10)

titulo("Casos especiales")
cargar([("70123456", "Quispe Rojas, Ana", "34"), ("45871236", "Alva Ruiz, Rosa", "52")])
ordenamiento.ordenar_por_nombre()
verificar("con 2 pacientes los ordena", datos.nombres == ["Alva Ruiz, Rosa", "Quispe Rojas, Ana"])

ordenamiento.ordenar_por_nombre()
verificar("ordenar algo ya ordenado no cambia nada", datos.nombres == ["Alva Ruiz, Rosa", "Quispe Rojas, Ana"])
cargar([("42003317", "Alva Ruiz, Rosa", "34"), ("45871236", "Castro Lima, Jose", "52"),
        ("70123456", "Quispe Rojas, Ana", "34")])
verificar("si ya esta ordenado, corta en la primera pasada (2 comparaciones)", ordenamiento.ordenar_por_nombre() == 2)

cargar([("45871236", "alvarado Paz, Ines", "40"), ("70123456", "Álvarez Soto, Pedro", "33"),
        ("71239854", "Alva Ruiz, Rosa", "29")])
ordenamiento.ordenar_por_nombre()
verificar("no distingue mayusculas ni tildes al ordenar", datos.nombres[0] == "Alva Ruiz, Rosa")

datos.limpiar_pacientes()
verificar("con la base vacia no falla (0 comparaciones)", ordenamiento.ordenar_por_nombre() == 0)
cargar([("70123456", "Quispe Rojas, Ana", "34")])
verificar("con 1 paciente no falla (0 comparaciones)", ordenamiento.ordenar_por_nombre() == 0)

titulo("intercambiar")
cargar([("45871236", "Torres Diaz, Luis", "52"), ("70123456", "Quispe Rojas, Ana", "34")])
ordenamiento.intercambiar(0, 1)
verificar("intercambia nombres y DNI a la vez", datos.nombres[0].startswith("Quispe") and datos.dnis[0] == "70123456")

resumen()
