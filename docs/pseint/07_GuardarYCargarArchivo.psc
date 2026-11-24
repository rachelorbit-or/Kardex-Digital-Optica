Algoritmo GuardarYCargarArchivo
	// Guardar y cargar los pacientes en un archivo de texto: una linea por paciente, datos separados por ;
	// PSeInt no maneja archivos, asi que el "archivo" se simula con un arreglo de lineas.
	// OJO: PSeInt cuenta los arreglos desde 1 (en Python se cuenta desde 0).
	
	Definir dnis, nombres, edades, archivo, linea, dniLinea Como Caracter
	Definir cantidad, i, j, k, puntoComa, cargados, omitidas, lineasArchivo Como Entero
	Definir repetido Como Logico
	Dimension dnis[3], nombres[3], edades[3], archivo[4]
	
	// Datos inventados (solo 3 campos para que el diagrama sea legible; en el programa real son 9)
	cantidad <- 3
	dnis[1] <- "70123456"
	nombres[1] <- "Quispe Rojas, Ana"
	edades[1] <- "34"
	dnis[2] <- "45871236"
	nombres[2] <- "Torres Diaz, Luis"
	edades[2] <- "52"
	dnis[3] <- "71239854"
	nombres[3] <- "Vega Salas, Marta"
	edades[3] <- "28"
	
	// ---------- GUARDAR: se arma una linea por paciente ----------
	Para i <- 1 Hasta cantidad Con Paso 1 Hacer
		archivo[i] <- Concatenar(dnis[i], Concatenar(";", Concatenar(nombres[i], Concatenar(";", edades[i]))))
	FinPara
	lineasArchivo <- cantidad
	// Una linea dañada y una repetida, para probar la carga
	lineasArchivo <- lineasArchivo + 1
	archivo[4] <- "70123456;Quispe Rojas, Ana;34"
	Escribir "Se guardaron ", cantidad, " paciente(s)."
	
	// ---------- CARGAR: se leen las lineas y se omiten las malas ----------
	cantidad <- 0
	omitidas <- 0
	Para i <- 1 Hasta lineasArchivo Con Paso 1 Hacer
		linea <- archivo[i]
		// una linea buena tiene exactamente 2 signos ";"
		puntoComa <- 0
		Para j <- 1 Hasta Longitud(linea) Con Paso 1 Hacer
			Si Subcadena(linea, j, j) = ";" Entonces
				puntoComa <- puntoComa + 1
			FinSi
		FinPara
		// el DNI son los primeros 8 caracteres
		dniLinea <- Subcadena(linea, 1, 8)
		// ¿ya esta cargado ese DNI?
		repetido <- Falso
		Para k <- 1 Hasta cantidad Con Paso 1 Hacer
			Si dnis[k] = dniLinea Entonces
				repetido <- Verdadero
			FinSi
		FinPara
		Si puntoComa <> 2 O repetido Entonces
			omitidas <- omitidas + 1
		SiNo
			cantidad <- cantidad + 1
			dnis[cantidad] <- dniLinea
		FinSi
	FinPara
	Escribir "Pacientes cargados: ", cantidad
	Escribir "Lineas omitidas (dañadas o repetidas): ", omitidas
FinAlgoritmo
