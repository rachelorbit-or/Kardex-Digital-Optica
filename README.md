# Kardex digital – Óptica Giem

Programa en Python (consola) para registrar los datos de los pacientes de una óptica
(DNI, nombres, edad, teléfono, medidas de cada ojo, DIP, material y fecha), buscarlos
y listarlos ordenados. Reemplaza el cuaderno de papel (kardex) por un archivo digital.

Proyecto del curso **Fundamentos de Programación (CIIN1205P)** – UPN Cajamarca.
Docente: Ing. Díaz Cabellos Frank.

## Integrantes
- Bacon Hilario José
- Bardales Vílchez Daryem Anthony
- Escobar Huamán Evelin Noemi
- Figueroa Chaupe Brayan Erick
- Olortegui Rodríguez Ana Raquel

## Cómo ejecutarlo
Solo necesita Python 3.8 o más. No hay que instalar nada.

    python src/main.py

Para ver el programa con datos de ejemplo (inventados), copiar
`data/ejemplo_pacientes.txt` como `data/pacientes.txt` antes de ejecutar.

## Cómo correr las pruebas

    python tests/ejecutar_todo.py

También se puede correr una sola: `python tests/test_registro.py`.

## Estructura (un módulo por algoritmo)

| Archivo | Qué hace |
|---|---|
| `src/datos.py` | Los 9 arreglos paralelos donde viven los datos en memoria |
| `src/validaciones.py` | Revisa cada dato antes de guardarlo (DNI, nombre, edad, medidas, fecha...) |
| `src/registro.py` | Algoritmo 3: registrar paciente + cálculo de la serie de precio |
| `src/busqueda.py` | Algoritmo 1: búsqueda secuencial por DNI y por apellido |
| `src/ordenamiento.py` | Algoritmo 2: ordenamiento burbuja por apellido |
| `src/reportes.py` | Cómo se muestra un paciente en pantalla |
| `src/persistencia.py` | Guardar y cargar el archivo de texto (con escritura segura) y respaldo |
| `src/main.py` | Menú principal |
| `tests/` | Pruebas automáticas de cada módulo |
| `data/ejemplo_pacientes.txt` | 5 pacientes **inventados** para probar |
| `docs/PLAN_COMMITS.md` | Reparto del trabajo y orden de commits |

## Formato del archivo de datos
Una línea por paciente, 9 datos separados por `;`:

    DNI;Apellidos, Nombres;edad;teléfono;medida OD;medida OI;DIP;material;fecha

Cada medida es `esfera/cilindro/eje` (ejemplo `-2.00/-1.00/90`).

## Reglas de validación (propuesta del equipo, por confirmar con el dueño)
DNI de 8 dígitos · nombre con formato `Apellidos, Nombres` · edad 1–110 · teléfono de 9 dígitos ·
esfera −20 a +20 · |cilindro| hasta 6 · eje 0–180 · DIP 40–80 mm · fecha real dd/mm/aaaa (2000–2100) ·
todos los datos obligatorios · DNI no repetido.

## Serie de precio
Se calcula con el mayor |cilindro| entre los dos ojos: hasta 2.00 → primera serie,
hasta 4.00 → segunda, hasta 6.00 → tercera.

## Privacidad
Las medidas de los lentes son datos de salud. **Nunca subir `data/pacientes.txt`**
(está en `.gitignore`). Para pruebas y capturas usar solo datos inventados.
