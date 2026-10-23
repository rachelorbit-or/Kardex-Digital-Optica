"""Programa principal: menu del kardex digital de la Optica Giem."""

import busqueda
import datos
import ordenamiento
import persistencia
import registro
import reportes


def mostrar_menu():
    print()
    print("===== KARDEX DIGITAL - ÓPTICA GIEM =====")
    print("1. Registrar paciente")
    print("2. Buscar por DNI")
    print("3. Buscar por apellido")
    print("4. Listar ordenados por apellido")
    print("5. Guardar y salir")


def opcion_registrar():
    print("--- Registrar paciente (todos los datos son obligatorios) ---")
    dni = input("DNI (8 dígitos): ")
    nombre = input("Apellidos y nombres (ej. Pérez Luna, Juan): ")
    edad = input("Edad: ")
    telefono = input("Teléfono (9 dígitos): ")
    medida_od = input("Medida ojo derecho (esfera/cilindro/eje, ej. -2.00/-1.00/90): ")
    medida_oi = input("Medida ojo izquierdo (esfera/cilindro/eje, ej. -1.75/0/0): ")
    dip = input("Distancia interpupilar en mm (ej. 62): ")
    material = input("Material del lente: ")
    fecha = input("Fecha de la visita (dd/mm/aaaa): ")
    aceptado, mensaje = registro.registrar_paciente(dni, nombre, edad, telefono, medida_od,
                                                    medida_oi, dip, material, fecha)
    if aceptado:
        print("[REGISTRADO] " + mensaje)
    else:
        print("[RECHAZADO] " + mensaje)


def opcion_buscar_dni():
    dni = input("DNI a buscar: ")
    posicion = busqueda.buscar_por_dni(dni)
    if posicion == -1:
        print("No se encontró ningún paciente con ese DNI.")
    else:
        print(reportes.formatear_paciente(posicion))


def opcion_buscar_apellido():
    texto = input("Apellido (o el inicio del apellido): ")
    posiciones = busqueda.buscar_por_apellido(texto)
    if len(posiciones) == 0:
        print("No se encontró ningún paciente con ese apellido.")
    else:
        print("Se encontraron", len(posiciones), "paciente(s):")
        reportes.listar_pacientes(posiciones)


def opcion_listar_ordenado():
    comparaciones = ordenamiento.ordenar_por_nombre()
    print("Pacientes ordenados por apellido (" + str(comparaciones) + " comparaciones):")
    reportes.listar_pacientes()


def main():
    omitidas = persistencia.cargar_desde_archivo()
    print("Pacientes cargados:", datos.cantidad())
    if omitidas > 0:
        print("Aviso: se omitieron", omitidas, "línea(s) dañada(s) o repetida(s) del archivo.")

    opcion = ""
    try:
        while opcion != "5":
            mostrar_menu()
            opcion = input("Elija una opción: ").strip()
            if opcion == "1":
                opcion_registrar()
            elif opcion == "2":
                opcion_buscar_dni()
            elif opcion == "3":
                opcion_buscar_apellido()
            elif opcion == "4":
                opcion_listar_ordenado()
            elif opcion == "5":
                pass
            else:
                print("Opción inválida. Elija un número del 1 al 5.")
    except (EOFError, KeyboardInterrupt):
        print("\nSe interrumpió el programa. Se guardarán los datos antes de salir.")
    cantidad = persistencia.guardar_en_archivo()
    print("Se guardaron", cantidad, "paciente(s). Hasta luego.")


if __name__ == "__main__":
    main()
