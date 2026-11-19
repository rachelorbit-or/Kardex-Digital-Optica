Algoritmo BuscarPorApellido
	// Busca TODOS los pacientes cuyo apellido empieza con el texto escrito.
	// Puede haber varios con el mismo apellido, por eso se recorren todos los pacientes.
	// OJO: PSeInt cuenta los arreglos desde 1 (en Python se cuenta desde 0).
	
	Definir nombres, buscado, apellido Como Caracter
	Definir cantidad, i, k, posComa, encontrados Como Entero
	Dimension nombres[5]
	
	// Datos inventados
	cantidad <- 5
	nombres[1] <- "Quispe Rojas, Ana"
	nombres[2] <- "Torres Diaz, Luis"
	nombres[3] <- "Quispe Vega, Marta"
	nombres[4] <- "Castro Lima, Jose"
	nombres[5] <- "Alva Ruiz, Rosa"
	
	Escribir "Apellido (o el inicio del apellido):"
	Leer buscado
	buscado <- Minusculas(buscado)
	
	encontrados <- 0
	Si Longitud(buscado) > 0 Entonces
		Para i <- 1 Hasta cantidad Con Paso 1 Hacer
			// El apellido es lo que esta antes de la coma
			posComa <- 0
			Para k <- 1 Hasta Longitud(nombres[i]) Con Paso 1 Hacer
				Si Subcadena(nombres[i], k, k) = "," Y posComa = 0 Entonces
					posComa <- k
				FinSi
			FinPara
			apellido <- Minusculas(Subcadena(nombres[i], 1, posComa - 1))
			
			// Coincide si el apellido empieza con el texto buscado
			Si Longitud(apellido) >= Longitud(buscado) Entonces
				Si Subcadena(apellido, 1, Longitud(buscado)) = buscado Entonces
					Escribir "Encontrado: ", nombres[i]
					encontrados <- encontrados + 1
				FinSi
			FinSi
		FinPara
	FinSi
	
	Si encontrados = 0 Entonces
		Escribir "No se encontro ningun paciente con ese apellido."
	SiNo
		Escribir "Se encontraron ", encontrados, " paciente(s)."
	FinSi
FinAlgoritmo
