Algoritmo CorregirDatosPersonales
	// Corrige el DNI, el nombre y la edad de un paciente ya registrado.
	// Primero busca al paciente por su DNI actual; luego VALIDA los datos nuevos y solo si todo
	// esta bien cambia los datos. Si hay un error, el paciente queda como estaba.
	// El DNI nuevo no puede ser el de OTRO paciente.
	// (En el programa real tambien se corrige el telefono; aqui se omite para que el diagrama sea corto.)
	// OJO: PSeInt cuenta los arreglos desde 1 (en Python se cuenta desde 0).
	
	Definir dnis, nombres, dniActual, dniNuevo, nombreNuevo, motivo Como Caracter
	Definir edades, cantidad, i, posicion, otraPosicion, edadNueva Como Entero
	Definir valido Como Logico
	Dimension dnis[5], nombres[5], edades[5]
	
	// Datos inventados
	cantidad <- 3
	dnis[1] <- "70123456"
	nombres[1] <- "Quispe Rojas, Ana"
	edades[1] <- 34
	dnis[2] <- "45871236"
	nombres[2] <- "Torres Diaz, Luis"
	edades[2] <- 52
	dnis[3] <- "71239854"
	nombres[3] <- "Vega Salas, Marta"
	edades[3] <- 19
	
	Escribir "DNI actual del paciente:"
	Leer dniActual
	
	// 1) Busqueda secuencial del paciente (posicion = 0 significa "no encontrado")
	posicion <- 0
	i <- 1
	Mientras i <= cantidad Y posicion = 0 Hacer
		Si dnis[i] = dniActual Entonces
			posicion <- i
		FinSi
		i <- i + 1
	FinMientras
	
	Si posicion = 0 Entonces
		Escribir "No se encontro ningun paciente con ese DNI."
	SiNo
		Escribir "Datos actuales: ", dnis[posicion], " | ", nombres[posicion], " | ", edades[posicion], " anios"
		Escribir "Nuevo DNI:"
		Leer dniNuevo
		Escribir "Nuevo nombre (Apellidos, Nombres):"
		Leer nombreNuevo
		Escribir "Nueva edad:"
		Leer edadNueva
		
		// 2) Validar los datos nuevos (se informa el PRIMER error)
		valido <- Verdadero
		motivo <- ""
		Si Longitud(dniNuevo) <> 8 Entonces
			valido <- Falso
			motivo <- "El DNI debe tener 8 digitos."
		SiNo
			Si Longitud(nombreNuevo) = 0 Entonces
				valido <- Falso
				motivo <- "El nombre debe tener el formato: Apellidos, Nombres."
			SiNo
				Si edadNueva < 1 O edadNueva > 110 Entonces
					valido <- Falso
					motivo <- "La edad debe estar entre 1 y 110."
				SiNo
					// 3) El DNI nuevo no puede pertenecer a OTRO paciente
					otraPosicion <- 0
					Para i <- 1 Hasta cantidad Con Paso 1 Hacer
						Si dnis[i] = dniNuevo Y i <> posicion Entonces
							otraPosicion <- i
						FinSi
					FinPara
					Si otraPosicion <> 0 Entonces
						valido <- Falso
						motivo <- "Ese DNI ya esta registrado en otro paciente."
					FinSi
				FinSi
			FinSi
		FinSi
		
		// 4) Solo si todo es valido se cambian los datos
		Si valido Entonces
			dnis[posicion] <- dniNuevo
			nombres[posicion] <- nombreNuevo
			edades[posicion] <- edadNueva
			Escribir "[ACTUALIZADO] Datos personales actualizados."
		SiNo
			Escribir "[RECHAZADO] ", motivo
		FinSi
	FinSi
FinAlgoritmo
