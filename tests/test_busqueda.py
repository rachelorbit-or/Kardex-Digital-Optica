"""Pruebas de busqueda.py.  Ejecutar:  python tests/test_busqueda.py"""

from utilidades_prueba import verificar, titulo, resumen
import datos
import busqueda
import registro

datos.limpiar_pacientes()
registro.registrar_paciente("70123456", "Quispe Rojas, Ana", "34", "987654321", "-2/-1/90", "-1.75/0/0", "62", "Policarbonato", "05/10/2026")
registro.registrar_paciente("45871236", "Torres Díaz, Luis", "52", "956781234", "1.5/0/0", "1.25/0/0", "64", "CR-39", "06/10/2026")
registro.registrar_paciente("71239854", "Quispe Vega, Marta", "19", "912345678", "-3/-2.5/180", "-3/-2/175", "58", "Policarbonato", "07/10/2026")
registro.registrar_paciente("42003317", "Núñez Castro, José", "61", "934567890", "2/0/0", "2.25/-0.5/10", "66", "Alto índice", "08/10/2026")

titulo("Buscar por DNI")
verificar("encuentra el primero (posicion 0)", busqueda.buscar_por_dni("70123456") == 0)
verificar("encuentra el ultimo (posicion 3)", busqueda.buscar_por_dni("42003317") == 3)
verificar("devuelve -1 si el DNI no existe", busqueda.buscar_por_dni("11111111") == -1)
verificar("ignora espacios alrededor", busqueda.buscar_por_dni("  45871236 ") == 1)
verificar("DNI vacio devuelve -1", busqueda.buscar_por_dni("") == -1)

titulo("Buscar por apellido")
verificar("'Quispe' devuelve 2 pacientes", busqueda.buscar_por_apellido("Quispe") == [0, 2])
verificar("no importan las mayusculas ('QUISPE')", busqueda.buscar_por_apellido("QUISPE") == [0, 2])
verificar("el inicio del apellido sirve ('Quis')", busqueda.buscar_por_apellido("Quis") == [0, 2])
verificar("no importan las tildes ('torres', 'Diaz' no es apellido)", busqueda.buscar_por_apellido("torres") == [1])
verificar("'nunez' encuentra 'Núñez'", busqueda.buscar_por_apellido("nunez") == [3])
verificar("busca por apellido y NO por nombre ('Ana' no aparece)", busqueda.buscar_por_apellido("Ana") == [])
verificar("apellido que no existe devuelve lista vacia", busqueda.buscar_por_apellido("Zapata") == [])
verificar("texto vacio devuelve lista vacia", busqueda.buscar_por_apellido("   ") == [])

titulo("Con la base vacia")
datos.limpiar_pacientes()
verificar("buscar por DNI en base vacia devuelve -1", busqueda.buscar_por_dni("70123456") == -1)
verificar("buscar por apellido en base vacia devuelve []", busqueda.buscar_por_apellido("Quispe") == [])

resumen()
