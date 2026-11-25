Algoritmo BuscarPorFecha
	// Busca TODOS los pacientes cuya visita fue en una fecha (dd/mm/aaaa).
	// Puede haber varios el mismo dia, por eso recorre todos los pacientes (busqueda secuencial)
	// y guarda cada coincidencia en una lista.
	// OJO: PSeInt cuenta los arreglos desde 1 (en Python se cuenta desde 0).
	
	Definir nombres, fechas, fechaBuscada Como Caracter
	Definir coincidencias Como Entero
	Definir cantidad, i, cuantos Como Entero
	Dimension nombres[5], fechas[5], coincidencias[5]
	
	// Datos inventados
	cantidad <- 4
	nombres[1] <- "Quispe Rojas, Ana"
	fechas[1] <- "05/10/2026"
	nombres[2] <- "Torres Diaz, Luis"
	fechas[2] <- "06/10/2026"
	nombres[3] <- "Vega Salas, Marta"
	fechas[3] <- "06/10/2026"
	nombres[4] <- "Nunez Castro, Jose"
	fechas[4] <- "08/10/2026"
	
	Escribir "Fecha de visita a buscar (dd/mm/aaaa):"
	Leer fechaBuscada
	
	cuantos <- 0
	Para i <- 1 Hasta cantidad Con Paso 1 Hacer
		Si fechas[i] = fechaBuscada Entonces
			cuantos <- cuantos + 1
			coincidencias[cuantos] <- i
		FinSi
	FinPara
	
	Si cuantos = 0 Entonces
		Escribir "No hubo visitas registradas en esa fecha."
	SiNo
		Escribir "Se encontraron ", cuantos, " paciente(s):"
		Para i <- 1 Hasta cuantos Con Paso 1 Hacer
			Escribir nombres[coincidencias[i]], " | visita ", fechas[coincidencias[i]]
		FinPara
	FinSi
FinAlgoritmo
