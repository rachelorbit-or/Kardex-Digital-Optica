"""Prueba completa del programa (main.py) simulando a una persona que escribe. 
Ejecutar:  python tests/test_menu.py"""

import os
import subprocess
import sys
import tempfile

from utilidades_prueba import verificar, titulo, resumen

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
MAIN = os.path.join(RAIZ, "src", "main.py")


def ejecutar(entradas, carpeta_datos):
    """Corre main.py con las entradas indicadas. Usa una copia del programa con su propia carpeta data."""
    entorno = dict(os.environ, PYTHONIOENCODING="utf-8")
    resultado = subprocess.run([sys.executable, MAIN], input="\n".join(entradas) + "\n",
                               capture_output=True, text=True, encoding="utf-8", env=entorno,
                               cwd=carpeta_datos, timeout=30)
    return resultado.stdout


# main.py guarda en data/pacientes.txt: hacemos una copia temporal del proyecto para no tocar los datos reales
import shutil
temporal = tempfile.mkdtemp(prefix="kardex_menu_")
shutil.copytree(os.path.join(RAIZ, "src"), os.path.join(temporal, "src"))
os.makedirs(os.path.join(temporal, "data"))
MAIN = os.path.join(temporal, "src", "main.py")

registrar = ["1", "70123456", "Quispe Rojas, Ana", "34", "987654321", "-2.00/-1.00/90",
             "-1.75/0/0", "62", "Policarbonato", "05/10/2026"]
registrar2 = ["1", "45871236", "Alva Ruiz, Rosa", "52", "956781234", "1.5/0/0", "1.25/0/0",
              "64", "CR-39", "06/10/2026"]

titulo("Una sesion completa")
salida = ejecutar(registrar + registrar2 + ["1", "123", "", "", "", "", "", "", "", "",
                  "2", "70123456", "2", "11111111", "3", "alva", "3", "zapata",
                  "4", "9", "5"], temporal)
verificar("muestra el menu", "KARDEX DIGITAL" in salida)
verificar("registra el primer paciente", salida.count("[REGISTRADO]") == 2)
verificar("rechaza el DNI invalido", "[RECHAZADO] El DNI debe tener 8 dígitos." in salida)
verificar("busca por DNI y muestra al paciente", "Quispe Rojas, Ana" in salida)
verificar("avisa cuando el DNI no existe", "No se encontró ningún paciente con ese DNI." in salida)
verificar("busca por apellido 'alva'", "Se encontraron 1 paciente(s):" in salida)
verificar("avisa cuando el apellido no existe", "No se encontró ningún paciente con ese apellido." in salida)
verificar("lista ordenados por apellido (Alva antes que Quispe)",
          salida.find("Alva Ruiz, Rosa", salida.find("ordenados por apellido (")) < salida.rfind("Quispe Rojas, Ana"))
verificar("opcion invalida muestra aviso", "Opción inválida" in salida)
verificar("al salir guarda los 2 pacientes", "Se guardaron 2 paciente(s)" in salida)

titulo("Los datos se recuerdan en la siguiente ejecucion")
salida = ejecutar(["2", "70123456", "5"], temporal)
verificar("al abrir carga los 2 pacientes guardados", "Pacientes cargados: 2" in salida)
verificar("el paciente buscado aparece", "Quispe Rojas, Ana" in salida)

titulo("Cierre inesperado (se acaba la entrada)")
salida = ejecutar(["1", "70123456"], temporal)
verificar("no se cae y guarda los datos", "Se guardaron 2 paciente(s)" in salida)

resumen()
