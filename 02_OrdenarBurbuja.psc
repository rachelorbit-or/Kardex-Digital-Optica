Algoritmo OrdenarBurbuja
	// Ordena los pacientes por apellido con el metodo de burbuja.
	// Como son arreglos paralelos, al intercambiar hay que mover los DOS arreglos.
	// OJO: PSeInt cuenta los arreglos desde 1 (en Python se cuenta desde 0).
	
	Definir dnis, nombres, auxDni, auxNombre Como Caracter
	Definir n, i, j, comparaciones, intercambios Como Entero
	Definir huboCambio Como Logico
	Dimension dnis[5], nombres[5]
	
	// Datos inventados, a proposito en desorden
	n <- 5
	nombres[1] <- "Torres Diaz, Luis"
	dnis[1] <- "45871236"
	nombres[2] <- "Quispe Rojas, Ana"
	dnis[2] <- "70123456"
	nombres[3] <- "Vega Salas, Marta"
	dnis[3] <- "71239854"
	nombres[4] <- "Alva Ruiz, Rosa"
	dnis[4] <- "73345512"
	nombres[5] <- "Castro Lima, Jose"
	dnis[5] <- "42003317"
	
	Escribir "ANTES de ordenar:"
	Para i <- 1 Hasta n Con Paso 1 Hacer
		Escribir nombres[i], " - ", dnis[i]
	FinPara
	
	comparaciones <- 0
	intercambios <- 0
	huboCambio <- Verdadero
	i <- 1
	// Si en una pasada no hubo cambios, ya esta ordenado y se termina antes
	Mientras i <= n - 1 Y huboCambio Hacer
		huboCambio <- Falso
		Para j <- 1 Hasta n - i Con Paso 1 Hacer
			comparaciones <- comparaciones + 1
			Si Minusculas(nombres[j]) > Minusculas(nombres[j + 1]) Entonces
				// Intercambiar la posicion j y j+1 en los dos arreglos
				auxNombre <- nombres[j]
				nombres[j] <- nombres[j + 1]
				nombres[j + 1] <- auxNombre
				auxDni <- dnis[j]
				dnis[j] <- dnis[j + 1]
				dnis[j + 1] <- auxDni
				intercambios <- intercambios + 1
				huboCambio <- Verdadero
			FinSi
		FinPara
		i <- i + 1
	FinMientras
	
	Escribir ""
	Escribir "DESPUES de ordenar:"
	Para i <- 1 Hasta n Con Paso 1 Hacer
		Escribir nombres[i], " - ", dnis[i]
	FinPara
	Escribir ""
	Escribir "Comparaciones: ", comparaciones
	Escribir "Intercambios: ", intercambios
FinAlgoritmo
