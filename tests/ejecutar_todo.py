"""Corre todos los archivos de prueba y muestra un resumen.  Ejecutar:  python tests/ejecutar_todo.py"""

import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ARCHIVOS = ["test_validaciones.py", "test_registro.py", "test_busqueda.py",
            "test_ordenamiento.py", "test_persistencia.py", "test_menu.py"]

hubo_fallos = False
for archivo in ARCHIVOS:
    print("\n##### " + archivo + " #####")
    entorno = dict(os.environ, PYTHONIOENCODING="utf-8")
    resultado = subprocess.run([sys.executable, os.path.join(AQUI, archivo)], env=entorno)
    if resultado.returncode != 0:
        hubo_fallos = True

print("\n" + ("HAY PRUEBAS QUE FALLAN" if hubo_fallos else "TODAS LAS PRUEBAS PASARON"))
sys.exit(1 if hubo_fallos else 0)
