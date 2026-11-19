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
		Escribir "4. Listar ordenados por apellido"
		Escribir "5. Actualizar medidas de un paciente"
		Escribir "6. Crear copia de respaldo"
		Escribir "7. Guardar y salir"
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
				Escribir "Listar ordenados por apellido: metodo de burbuja (algoritmo OrdenarBurbuja)."
			5:
				Escribir "Actualizar medidas de un paciente que vuelve (algoritmo ActualizarMedidas)."
			6:
				Escribir "Crear copia de respaldo en la carpeta indicada (por ejemplo, una USB)."
			7:
				Escribir "Guardando los pacientes en el archivo..."
			De Otro Modo:
				Escribir "Opcion invalida. Elija un numero del 1 al 7."
		FinSegun
	Hasta Que opcion = 7
	
	Escribir "Datos guardados. Hasta luego."
FinAlgoritmo
