Algoritmo RegistroPaciente
	// Registro de un paciente con validaciones.
	// En el programa real son 9 arreglos; aqui usamos 6 para que el diagrama sea legible.
	// OJO: PSeInt cuenta los arreglos desde 1 (en Python se cuenta desde 0).
	
	Definir dnis, nombres, telefonos, dni, nombre, telefono, motivo, serie Como Caracter
	Definir edades, ejes, cantidad, edad, eje, i Como Entero
	Definir cilindros, esfera, cilindro Como Real
	Definir duplicado Como Logico
	Dimension dnis[20], nombres[20], telefonos[20], edades[20], cilindros[20], ejes[20]
	
	// Pacientes que ya estaban registrados (datos inventados)
	cantidad <- 3
	dnis[1] <- "70123456"
	nombres[1] <- "Quispe Rojas, Ana"
	telefonos[1] <- "987654321"
	edades[1] <- 34
	cilindros[1] <- -1
	ejes[1] <- 90
	dnis[2] <- "45871236"
	nombres[2] <- "Torres Diaz, Luis"
	telefonos[2] <- "956781234"
	edades[2] <- 52
	cilindros[2] <- 0
	ejes[2] <- 0
	dnis[3] <- "71239854"
	nombres[3] <- "Vega Salas, Marta"
	telefonos[3] <- "912345678"
	edades[3] <- 19
	cilindros[3] <- -2.5
	ejes[3] <- 180
	
	// ---- Entrada de datos ----
	Escribir "DNI (8 digitos):"
	Leer dni
	Escribir "Apellidos y nombres (ej. Perez Luna, Juan):"
	Leer nombre
	Escribir "Edad:"
	Leer edad
	Escribir "Telefono (9 digitos):"
	Leer telefono
	Escribir "Esfera del ojo derecho (-20 a 20):"
	Leer esfera
	Escribir "Cilindro del ojo derecho (-6 a 6):"
	Leer cilindro
	Escribir "Eje del ojo derecho (0 a 180):"
	Leer eje
	
	// ---- Validaciones: solo se revisa la siguiente si no hubo error antes ----
	motivo <- ""
	Si motivo = "" Y NO ValidarDNI(dni) Entonces
		motivo <- "El DNI debe tener 8 digitos."
	FinSi
	Si motivo = "" Y NO ValidarNombre(nombre) Entonces
		motivo <- "El nombre debe tener el formato: Apellidos, Nombres."
	FinSi
	Si motivo = "" Y (edad < 1 O edad > 110) Entonces
		motivo <- "La edad debe estar entre 1 y 110."
	FinSi
	Si motivo = "" Y NO ValidarTelefono(telefono) Entonces
		motivo <- "El telefono debe tener 9 digitos."
	FinSi
	Si motivo = "" Y (esfera < -20 O esfera > 20) Entonces
		motivo <- "La esfera debe estar entre -20 y 20."
	FinSi
	Si motivo = "" Y Abs(cilindro) > 6 Entonces
		motivo <- "El cilindro no puede pasar de 6 (en valor absoluto)."
	FinSi
	Si motivo = "" Y (eje < 0 O eje > 180) Entonces
		motivo <- "El eje debe estar entre 0 y 180."
	FinSi
	
	// ---- DNI repetido: busqueda secuencial en el arreglo ----
	duplicado <- Falso
	i <- 1
	Mientras i <= cantidad Y NO duplicado Hacer
		Si dnis[i] = dni Entonces
			duplicado <- Verdadero
		FinSi
		i <- i + 1
	FinMientras
	Si motivo = "" Y duplicado Entonces
		motivo <- "Ese DNI ya esta registrado."
	FinSi
	
	// ---- Resultado ----
	Si motivo <> "" Entonces
		Escribir "RECHAZADO: ", motivo
	SiNo
		cantidad <- cantidad + 1
		dnis[cantidad] <- dni
		nombres[cantidad] <- nombre
		telefonos[cantidad] <- telefono
		edades[cantidad] <- edad
		cilindros[cantidad] <- cilindro
		ejes[cantidad] <- eje
		
		// Serie de precio segun el cilindro (astigmatismo)
		Si Abs(cilindro) <= 2 Entonces
			serie <- "Primera serie"
		SiNo
			Si Abs(cilindro) <= 4 Entonces
				serie <- "Segunda serie"
			SiNo
				serie <- "Tercera serie"
			FinSi
		FinSi
		Escribir "REGISTRADO: ", nombre, " - ", serie
		Escribir "Pacientes registrados: ", cantidad
	FinSi
FinAlgoritmo

// ---------- Funciones de validacion ----------

Funcion r <- SoloDigitos(texto)
	Definir r Como Logico
	Definir i Como Entero
	Definir c Como Caracter
	r <- Longitud(texto) > 0
	Para i <- 1 Hasta Longitud(texto) Con Paso 1 Hacer
		c <- Subcadena(texto, i, i)
		Si c < "0" O c > "9" Entonces
			r <- Falso
		FinSi
	FinPara
FinFuncion

Funcion r <- ValidarDNI(texto)
	Definir r Como Logico
	r <- Longitud(texto) = 8 Y SoloDigitos(texto)
FinFuncion

Funcion r <- ValidarTelefono(texto)
	Definir r Como Logico
	r <- Longitud(texto) = 9 Y SoloDigitos(texto)
FinFuncion

Funcion r <- ValidarNombre(texto)
	// Debe tener una coma, con texto antes y despues (Apellidos, Nombres)
	Definir r Como Logico
	Definir i, posComa Como Entero
	posComa <- 0
	Para i <- 1 Hasta Longitud(texto) Con Paso 1 Hacer
		Si Subcadena(texto, i, i) = "," Y posComa = 0 Entonces
			posComa <- i
		FinSi
	FinPara
	r <- posComa > 1 Y posComa < Longitud(texto)
FinFuncion
