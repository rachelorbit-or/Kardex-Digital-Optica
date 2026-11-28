Algoritmo ProgramaPrincipal
	// Menu principal del kardex digital de la Optica Giem.
	// Cada opcion llama al algoritmo que se explica en su propio archivo.
	
	Definir opcion Como Entero
	
	Escribir "Cargando los pacientes desde el archivo..."
	
	Repetir
		Escribir ""
		Escribir "===== KARDEX DIGITAL - OPTICA GIEM ====="
		Escribir "1. Registrar paciente"
		Escribir "2. Buscar por DNI"
		Escribir "3. Buscar por apellido"
		Escribir "4. Buscar por fecha de visita"
		Escribir "5. Listar ordenados por apellido"
		Escribir "6. Actualizar medidas de un paciente"
		Escribir "7. Corregir datos personales de un paciente"
		Escribir "8. Crear copia de respaldo"
		Escribir "9. Guardar y salir"
		Escribir "Elija una opcion:"
		Leer opcion
		
		Segun opcion Hacer
			1:
				Escribir "Registrar paciente: validar los datos y agregarlos (algoritmo RegistroPaciente)."
			2:
				Escribir "Buscar por DNI: busqueda secuencial (algoritmo BuscarPorDNI)."
			3:
				Escribir "Buscar por apellido: todas las coincidencias (algoritmo BuscarPorApellido)."
			4:
				Escribir "Buscar por fecha de visita: todas las coincidencias (algoritmo BuscarPorFecha)."
			5:
				Escribir "Listar ordenados por apellido: metodo de burbuja (algoritmo OrdenarBurbuja)."
			6:
				Escribir "Actualizar medidas de un paciente que vuelve (algoritmo ActualizarMedidas)."
			7:
				Escribir "Corregir DNI, nombre, edad o telefono (algoritmo CorregirDatosPersonales)."
			8:
				Escribir "Crear copia de respaldo en la carpeta indicada (algoritmo CrearRespaldo)."
			9:
				Escribir "Guardando los pacientes en el archivo..."
			De Otro Modo:
				Escribir "Opcion invalida. Elija un numero del 1 al 9."
		FinSegun
	Hasta Que opcion = 9
	
	Escribir "Datos guardados. Hasta luego."
FinAlgoritmo
