"""Prueba de eficiencia con 1,000 pacientes INVENTADOS.  Ejecutar:  python tests/prueba_eficiencia.py

Mide cuantas comparaciones y cuanto tiempo toman las operaciones principales cuando hay
1,000 pacientes (el volumen de unos 3 anios de registro segun la entrevista).
Todos los datos son inventados: no se usa ningun paciente real.
"""

import os
import random
import tempfile
import time

from utilidades_prueba import verificar, titulo, resumen
import busqueda
import datos
import ordenamiento
import persistencia
import registro

CANTIDAD = 1000
LIMITE_SEGUNDOS = 1.0   # tiempo maximo aceptable para una busqueda
LIMITE_LARGO = 5.0      # tiempo maximo aceptable para registrar u ordenar los 1,000 pacientes

APELLIDOS = ["Alva", "Bazan", "Castro", "Diaz", "Espinoza", "Flores", "Gil", "Huaman", "Iparraguirre", "Julca",
             "Lopez", "Mendoza", "Narro", "Ortiz", "Perez", "Quispe", "Rojas", "Salas", "Torres", "Urbina",
             "Vega", "Yupanqui", "Zavala", "Abanto", "Becerra", "Cueva", "Delgado", "Estela", "Fernandez", "Guevara",
             "Hoyos", "Infante", "Jara", "Leon", "Mori", "Nunez", "Olano", "Pajares", "Ramos", "Sanchez"]
NOMBRES = ["Ana", "Luis", "Rosa", "Jose", "Marta", "Pedro", "Lucia", "Carlos", "Elena", "Juan",
           "Sofia", "Diego", "Carla", "Mario", "Nora", "Raul", "Alicia", "Hugo", "Irma", "Ivan",
           "Julia", "Oscar", "Paula", "Sergio", "Teresa"]


def medir(funcion, *argumentos):
    """Ejecuta la funcion y devuelve (resultado, segundos)."""
    inicio = time.perf_counter()
    resultado = funcion(*argumentos)
    return resultado, time.perf_counter() - inicio


def segundos_a_texto(segundos):
    return str(round(segundos * 1000, 2)) + " ms"


random.seed(2026)   # mismos datos inventados en cada ejecucion

# ---------------------------------------------------------------
titulo("Registrar " + str(CANTIDAD) + " pacientes inventados")
datos.limpiar_pacientes()
combinaciones = [(a, n) for a in APELLIDOS for n in NOMBRES]
random.shuffle(combinaciones)
aceptados = 0
inicio = time.perf_counter()
for i in range(CANTIDAD):
    apellido, nombre = combinaciones[i]
    dni = str(10000000 + i * 7)
    esfera = random.choice(["-3.50", "-1.25", "0.75", "2.00", "-5.00"])
    cilindro = random.choice(["0", "-0.75", "-1.50", "-2.50", "-4.50"])
    eje = str(random.randint(0, 180)) if cilindro != "0" else "0"
    medida = esfera + "/" + cilindro + "/" + eje
    ok, _ = registro.registrar_paciente(dni, apellido + ", " + nombre, str(random.randint(8, 80)),
                                        "9" + str(10000000 + i), medida, medida, str(random.randint(54, 70)),
                                        "CR-39", "15/10/2026")
    if ok:
        aceptados = aceptados + 1
tiempo_registro = time.perf_counter() - inicio
print("   Tiempo para registrar y validar " + str(CANTIDAD) + " pacientes: " + segundos_a_texto(tiempo_registro))
verificar("se registraron los " + str(CANTIDAD) + " pacientes", aceptados == CANTIDAD and datos.cantidad() == CANTIDAD)
verificar("registrar " + str(CANTIDAD) + " pacientes tarda menos de 5 segundos", tiempo_registro < LIMITE_LARGO)

# ---------------------------------------------------------------
titulo("Busqueda secuencial por DNI (peor caso)")
dni_ultimo = datos.dnis[CANTIDAD - 1]
posicion, t = medir(busqueda.buscar_por_dni, dni_ultimo)
print("   Paciente en la ultima posicion: " + str(posicion + 1) + " comparaciones, " + segundos_a_texto(t))
verificar("encuentra al ultimo paciente tras " + str(CANTIDAD) + " comparaciones", posicion == CANTIDAD - 1)
posicion, t = medir(busqueda.buscar_por_dni, "99999999")
print("   DNI que no existe: " + str(CANTIDAD) + " comparaciones, " + segundos_a_texto(t))
verificar("un DNI inexistente devuelve -1", posicion == -1)
verificar("la busqueda por DNI tarda menos de 1 segundo", t < LIMITE_SEGUNDOS)
posicion, t = medir(busqueda.buscar_por_dni, datos.dnis[0])
print("   Paciente en la primera posicion: 1 comparacion, " + segundos_a_texto(t))
verificar("encuentra al primer paciente", posicion == 0)

# ---------------------------------------------------------------
titulo("Busqueda secuencial por apellido")
coincidencias, t = medir(busqueda.buscar_por_apellido, "Quispe")
print("   Apellido Quispe: " + str(len(coincidencias)) + " coincidencias, " + segundos_a_texto(t))
verificar("encuentra los " + str(len(NOMBRES)) + " pacientes con apellido Quispe que se registraron",
          len([i for i in range(CANTIDAD) if datos.nombres[i].startswith("Quispe,")]) == len(coincidencias))
verificar("la busqueda por apellido tarda menos de 1 segundo", t < LIMITE_SEGUNDOS)

# ---------------------------------------------------------------
titulo("Ordenamiento por burbuja")
maximo = CANTIDAD * (CANTIDAD - 1) // 2
comparaciones, t = medir(ordenamiento.ordenar_por_nombre)
print("   Orden desordenado: " + str(comparaciones) + " comparaciones (maximo posible " + str(maximo) + "), " + segundos_a_texto(t))
verificar("no supera el maximo n(n-1)/2 = " + str(maximo), comparaciones <= maximo)
verificar("quedan ordenados A-Z", datos.nombres == sorted(datos.nombres))
verificar("los 9 arreglos siguen del mismo largo", len({len(a) for a in datos.todos_los_arreglos()}) == 1)
verificar("ordenar " + str(CANTIDAD) + " pacientes tarda menos de 5 segundos", t < LIMITE_LARGO)
comparaciones, t = medir(ordenamiento.ordenar_por_nombre)
print("   Ya ordenado: " + str(comparaciones) + " comparaciones, " + segundos_a_texto(t))
verificar("si ya estaba ordenado, termina en una sola pasada (" + str(CANTIDAD - 1) + " comparaciones)",
          comparaciones == CANTIDAD - 1)

# ---------------------------------------------------------------
titulo("Guardar y cargar el archivo")
carpeta = tempfile.mkdtemp()
ruta = os.path.join(carpeta, "pacientes_prueba.txt")
guardados, t_guardar = medir(persistencia.guardar_en_archivo, ruta)
tamano = os.path.getsize(ruta)
print("   Guardar: " + segundos_a_texto(t_guardar) + ", archivo de " + str(round(tamano / 1024, 1)) + " KB")
verificar("guarda los " + str(CANTIDAD) + " pacientes", guardados == CANTIDAD)
verificar("el archivo pesa menos de 1 MB", tamano < 1024 * 1024)
dnis_antes = list(datos.dnis)
omitidas, t_cargar = medir(persistencia.cargar_desde_archivo, ruta)
print("   Cargar: " + segundos_a_texto(t_cargar))
verificar("al cargar recupera los mismos " + str(CANTIDAD) + " pacientes sin omitir lineas",
          omitidas == 0 and datos.dnis == dnis_antes)
os.remove(ruta)
os.rmdir(carpeta)
datos.limpiar_pacientes()

resumen()
