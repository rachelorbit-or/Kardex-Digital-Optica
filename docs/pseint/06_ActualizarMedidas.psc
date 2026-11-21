Algoritmo ActualizarMedidas
	// Actualiza las medidas de un paciente que ya esta registrado (paciente que vuelve).
	// Primero busca al paciente por su DNI; luego VALIDA los datos nuevos y solo si todo
	// esta bien cambia los datos. Si hay un error, el paciente queda como estaba.
	// OJO: PSeInt cuenta los arreglos desde 1 (en Python se cuenta desde 0).
	
	Definir dnis, nombres, dniBuscado, material, materiales, motivo, serie Como Caracter
	Definir cantidad, i, posicion, eje, ejes Como Entero
	Definir cilindro, cilindros Como Real
	Dimension dnis[5], nombres[5], materiales[5], cilindros[5], ejes[5]
	
	// Datos inventados
	cantidad <- 3
	dnis[1] <- "70123456"
	nombres[1] <- "Quispe Rojas, Ana"
	materiales[1] <- "Policarbonato"
	cilindros[1] <- -1
	ejes[1] <- 90
	dnis[2] <- "45871236"
	nombres[2] <- "Torres Diaz, Luis"
	materiales[2] <- "CR-39"
	cilindros[2] <- 0
	ejes[2] <- 0
	dnis[3] <- "71239854"
	nombres[3] <- "Vega Salas, Marta"
	materiales[3] <- "CR-39"
	cilindros[3] <- -2.5
	ejes[3] <- 180
	
	Escribir "DNI del paciente:"
	Leer dniBuscado
	
	// Busqueda secuencial (posicion = 0 significa "todavia no encontrado")
	posicion <- 0
	i <- 1
	Mientras i <= cantidad Y posicion = 0 Hacer
		Si dnis[i] = dniBuscado Entonces
			posicion <- i
		FinSi
		i <- i + 1
	FinMientras
	
	Si posicion = 0 Entonces
		Escribir "No se encontro ningun paciente con ese DNI."
	SiNo
		Escribir "Datos actuales: ", nombres[posicion], " - cilindro ", cilindros[posicion], " eje ", ejes[posicion], " - ", materiales[posicion]
		Escribir "Nuevo cilindro (-6 a 6):"
		Leer cilindro
		Escribir "Nuevo eje (0 a 180):"
		Leer eje
		Escribir "Nuevo material:"
		Leer material
		
		// Se revisa cada dato; solo se guarda el primer error
		motivo <- ""
		Si Abs(cilindro) > 6 Entonces
			motivo <- "El cilindro no puede pasar de 6 (en valor absoluto)."
		FinSi
		Si motivo = "" Y (eje < 0 O eje > 180) Entonces
			motivo <- "El eje debe estar entre 0 y 180."
		FinSi
		Si motivo = "" Y Longitud(material) = 0 Entonces
			motivo <- "El material no puede estar vacio."
		FinSi
		
		Si motivo <> "" Entonces
			Escribir "RECHAZADO: ", motivo, " (el paciente queda como estaba)"
		SiNo
			// Todo es valido: recien ahora se cambian los datos
			cilindros[posicion] <- cilindro
			ejes[posicion] <- eje
			materiales[posicion] <- material
			Si Abs(cilindro) <= 2 Entonces
				serie <- "Primera serie"
			SiNo
				Si Abs(cilindro) <= 4 Entonces
					serie <- "Segunda serie"
				SiNo
					serie <- "Tercera serie"
				FinSi
			FinSi
			Escribir "ACTUALIZADO: ", nombres[posicion], " - ", serie
		FinSi
	FinSi
FinAlgoritmo
