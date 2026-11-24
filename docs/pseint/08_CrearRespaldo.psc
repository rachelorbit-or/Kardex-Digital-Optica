Algoritmo CrearRespaldo
	// Copia de respaldo (por ejemplo en una USB).
	// Si la carpeta no existe, avisa y el programa sigue; si existe, guarda la copia con fecha y hora.
	// PSeInt no maneja carpetas, asi que se simula con una lista de carpetas que "existen".
	
	Definir carpetas, carpetaDestino, nombreArchivo Como Caracter
	Definir i Como Entero
	Definir existe Como Logico
	Dimension carpetas[3]
	
	carpetas[1] <- "C:/respaldos"
	carpetas[2] <- "E:/"
	carpetas[3] <- "D:/datos"
	
	Escribir "Carpeta donde guardar la copia (ej. E:/ o C:/respaldos):"
	Leer carpetaDestino
	
	// 1) comprobar si la carpeta existe
	existe <- Falso
	Para i <- 1 Hasta 3 Con Paso 1 Hacer
		Si carpetas[i] = carpetaDestino Entonces
			existe <- Verdadero
		FinSi
	FinPara
	
	// 2) si no existe, avisar y terminar (el programa principal sigue funcionando)
	Si existe = Falso Entonces
		Escribir "[ERROR] La carpeta ", carpetaDestino, " no existe."
	SiNo
		// 3) si existe, armar el nombre con la fecha y hora y guardar
		nombreArchivo <- "respaldo_pacientes_AAAAMMDD_HHMMSS.txt"
		Escribir "[RESPALDO] Copia creada en: ", carpetaDestino, "/", nombreArchivo
	FinSi
FinAlgoritmo
