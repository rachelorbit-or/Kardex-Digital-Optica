"""Ayuda comun para los archivos de prueba (no hace falta instalar nada)."""

import os
import sys

# Permite importar los modulos de la carpeta src
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

total = 0
fallos = 0


def verificar(descripcion, condicion):
    """Imprime [OK] o [FALLA] segun si la condicion se cumple."""
    global total, fallos
    total = total + 1
    if condicion:
        print("[OK]    " + descripcion)
    else:
        fallos = fallos + 1
        print("[FALLA] " + descripcion)


def titulo(texto):
    print()
    print("=== " + texto + " ===")


def resumen():
    """Imprime el resumen y termina con codigo 1 si hubo fallos."""
    print()
    print("RESUMEN: " + str(total - fallos) + " de " + str(total) + " pruebas OK")
    if fallos > 0:
        sys.exit(1)
