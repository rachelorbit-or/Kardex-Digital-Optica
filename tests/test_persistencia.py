"""Pruebas de persistencia.py.  Ejecutar:  python tests/test_persistencia.py"""

import os
import tempfile

from utilidades_prueba import verificar, titulo, resumen
import datos
import persistencia
import registro

carpeta = tempfile.mkdtemp(prefix="kardex_prueba_")
ruta = os.path.join(carpeta, "pacientes.txt")

datos.limpiar_pacientes()
registro.registrar_paciente("70123456", "Quispe Rojas, Ana", "34", "987654321", "-2.00/-1.00/90", "-1.75/0/0", "62", "Policarbonato", "05/10/2026")
registro.registrar_paciente("45871236", "Torres Díaz, Luis", "52", "956781234", "+1.50/0/0", "+1.25/0/0", "64", "CR-39", "06/10/2026")

titulo("Guardar y cargar")
cantidad = persistencia.guardar_en_archivo(ruta)
verificar("guarda 2 pacientes", cantidad == 2)
verificar("el archivo existe", os.path.exists(ruta))
verificar("no queda el archivo temporal", not os.path.exists(ruta + ".tmp"))
with open(ruta, encoding="utf-8") as f:
    lineas = f.read().splitlines()
verificar("hay una linea por paciente", len(lineas) == 2)
verificar("cada linea tiene 9 datos separados por ;", all(len(l.split(";")) == 9 for l in lineas))

copia_dnis = list(datos.dnis)
copia_nombres = list(datos.nombres)
copia_edades = list(datos.edades)
datos.limpiar_pacientes()
verificar("antes de cargar, los arreglos estan vacios", datos.cantidad() == 0)
omitidas = persistencia.cargar_desde_archivo(ruta)
verificar("recupera los mismos DNI", datos.dnis == copia_dnis)
verificar("recupera los mismos nombres (con tilde)", datos.nombres == copia_nombres)
verificar("recupera las edades como numeros", datos.edades == copia_edades)
verificar("no omitio ninguna linea", omitidas == 0)

titulo("Lineas dañadas")
with open(ruta, "a", encoding="utf-8") as f:
    f.write("LINEA;DAÑADA\n")
    f.write("123;Sin Coma;34;987654321;0/0/0;0/0/0;62;CR-39;05/10/2026\n")
    f.write("70123456;Quispe Rojas, Ana;34;987654321;-2/-1/90;-1/0/0;62;CR-39;05/10/2026\n")
    f.write("\n")
omitidas = persistencia.cargar_desde_archivo(ruta)
verificar("omite las 2 lineas dañadas y el DNI repetido (3 en total)", omitidas == 3)
verificar("los pacientes buenos se cargan igual (2)", datos.cantidad() == 2)

titulo("Archivo que no existe")
omitidas = persistencia.cargar_desde_archivo(os.path.join(carpeta, "no_existe.txt"))
verificar("si no existe, no falla y deja la base vacia", omitidas == 0 and datos.cantidad() == 0)

titulo("Respaldo")
persistencia.cargar_desde_archivo(ruta)
ok, ruta_respaldo = persistencia.crear_respaldo(carpeta)
verificar("crea el respaldo en una carpeta que existe", ok and os.path.exists(ruta_respaldo))
verificar("el respaldo se llama respaldo_pacientes_*.txt", os.path.basename(ruta_respaldo).startswith("respaldo_pacientes_"))
with open(ruta_respaldo, encoding="utf-8") as f:
    verificar("el respaldo tiene los 2 pacientes", len(f.read().splitlines()) == 2)
ok, msg = persistencia.crear_respaldo(os.path.join(carpeta, "carpeta_inexistente"))
verificar("si la carpeta no existe, avisa y no falla", not ok and "no existe" in msg)

resumen()
