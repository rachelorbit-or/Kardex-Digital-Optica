Algoritmo BuscarPorDNI
	// Busqueda secuencial de un paciente por su DNI.
	// Arreglos paralelos: la misma posicion = la misma persona.
	// OJO: PSeInt cuenta los arreglos desde 1 (en Python se cuenta desde 0).
	
	Definir dnis, nombres, dniBuscado Como Caracter
	Definir cantidad, i, posicion Como Entero
	Dimension dnis[5], nombres[5]
	
	// Datos inventados
	cantidad <- 5
	dnis[1] <- "70123456"
	nombres[1] <- "Quispe Rojas, Ana"
	dnis[2] <- "45871236"
	nombres[2] <- "Torres Diaz, Luis"
	dnis[3] <- "71239854"
	nombres[3] <- "Vega Salas, Marta"
	dnis[4] <- "42003317"
	nombres[4] <- "Castro Lima, Jose"
	dnis[5] <- "73345512"
	nombres[5] <- "Alva Ruiz, Rosa"
	
	Escribir "Ingrese el DNI a buscar:"
	Leer dniBuscado
	
	// posicion = 0 significa "todavia no encontrado"
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
		Escribir "Paciente encontrado: ", nombres[posicion]
	FinSi
FinAlgoritmo
