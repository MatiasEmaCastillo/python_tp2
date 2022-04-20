#CONSTANTES
NEGRO="0 0 0"
AMARILLO="255 255 0"
ROJO="255 0 0"
AZUL="0 0 255"
VERDE="0 255 0"
VIOLETA="255 0 255"

#configuracion x defecto-------------------------------------------------------
CELDAS=10,10
ESPEJADO=1,1
COLORES={}
COLORES["negro"]=NEGRO
COLORES["amarillo"]=AMARILLO
COLORES["rojo"]=ROJO
COLORES["azul"]=AZUL


#parametros obligatoriors----------------------------------------------------
def pedir_fractal():
	"Funcion que pide el ancho y alto del fractal"

	while True:
		try:
			ancho_fractal=int(input("Ingrese el ancho del fractal: "))
			alto_fractal=int(input("Ingrese el alto del fractal: "))
			if ancho_fractal<=0 or alto_fractal<=0:
				print("Ha ingresado numeros no positivo vuelva a ingresar.")
				continue
			return ancho_fractal,alto_fractal
		except ValueError:
			print("Ha ingresado un valor incorrecto para el fractal")

def pedir_fractal_monticulo():
	"Funcion que pide posicion y cantidad de arena que desea agregar al fractal"
	ancho_fractal,alto_fractal=pedir_fractal()
	dimension_fractal=ancho_fractal,alto_fractal
	mensaje="¿Desea agregar otro monticulo?('no' para terminar): "
	advertencia="Ha ingresado un valor incorrecto, ingrese numeros positivos y menor al ancho y alto del fractal"
	msj_prim_coord="ingrese 1ra coordenada de la posicion donde desea agregar: "
	msj_segunda_coord="ingrese 2da coordenada de la posicion de donde desea agregar: "
	msj_cant_granos="Ingrese la cantidad de granos de arena a colocar: "
	msj_advertencia_continuar="Respuesta invalida, ingrese si para continuar o no para temrinar"
	posicion_granos={}

	while True:
		try:
			columna_monticulo,fila_monticulo=int(input(msj_prim_coord)),int(input(msj_segunda_coord))
			cant_granos=int(input(msj_cant_granos))
			if columna_monticulo<0 or columna_monticulo>=ancho_fractal:
				print(advertencia)
				continue
			if fila_monticulo<0 or fila_monticulo>=alto_fractal:
				print(advertencia)
				continue
			if cant_granos<=0:
				print(advertencia)
				continue
			posicion_granos[columna_monticulo,fila_monticulo]=posicion_granos.get((columna_monticulo,fila_monticulo),0)+cant_granos
			continuar=input(mensaje)
			continuar=continuar.lower()
			while continuar!="si" and continuar!="no":
				print(msj_advertencia_continuar)
				continuar=input(mensaje)
				continuar=continuar.lower()
			
			if continuar=="si":
				continue
			if continuar=="no":
				return dimension_fractal,posicion_granos


		except ValueError:
			print(advertencia)


def pedir_nombre_archivo():
	"Funcion que le pide al usuario el nombre que del archivo a crear"
	nombre_archivo=input("Ingrese el nombre deseado del archivo: ")+".ppm"
	return nombre_archivo

#parametros elegidos por el usuario-------------------------------------------
def pedir_celda():
	"Funcion que pide el tamaña de cada del fractal"
	while True:
		try:
			celda_horizontal,celda_vertical=int(input("ingrese el tamaño de la celda horizontal: ")),int(input("ingrese el tamaño de la celda vertical: "))
			return celda_horizontal,celda_vertical
		except ValueError:
			print("Ha ingresado un valor incorrecto")

def pedir_colores():
	"Funcion que le pide al usuario la seleccion de 4 colores distintos a usar en el fractal"

	print("A continuacion debe elegir 4 colores distintos")
	paleta_de_colores={}
	paleta_de_colores["azul"]=AZUL
	paleta_de_colores["rojo"]=ROJO
	paleta_de_colores["amarillo"]=AMARILLO
	paleta_de_colores["verde"]=VERDE
	paleta_de_colores["violeta"]=VIOLETA
	paleta_de_colores["negro"]=NEGRO
	contador=0
	lista_colores=list(paleta_de_colores.keys())
	colores_seleccionados={}
	while contador != 4:
		print(lista_colores)
		color=input("Seleccione un color disponible de los colores mostrados: ")
		color=color.lower()
		if color in lista_colores:
			colores_seleccionados[color]=paleta_de_colores[color]
			lista_colores.remove(color)
			contador+=1
			continue
		print("Seleccion de color incorrecto, vuelva a elegir otro color")
	return colores_seleccionados

def pedir_espejado():
	"La funcion le pide al usuario el espejado deseado"
	while True:
		try:
			espejado_vertical,espejado_horizontal=int(input("Ingrese espejado vertical: ")),int(input("Ingrese espejado horizontal: "))
			if espejado_horizontal<=0 or espejado_horizontal<=0:
				print("Ingrese numeros positivos")
				continue
			return espejado_vertical,espejado_horizontal
		except ValueError:
			print("Ha ingresado un valor incorrecto")



def pedir_configuracion():
	"La funcion le pregunta al usuario si desea usar la configuracion por defecto o si desea personalizarla"
	while True:
		consulta=input("¿Desea personalizar la configuracion?(si-no): ")
		consulta=consulta.lower()
		if consulta=="si" or consulta=="no":
			return consulta
		print("Respuesta incorrecta, vuelva a responder por favor.")


def definir_parametros():
	"Funcion que devuelve los parametros que se van a usar para la construccion del fractal"
	dimension_fractal,fractal_inicial=pedir_fractal_monticulo()
	nombre_archivo=pedir_nombre_archivo()
	opcion=pedir_configuracion()
	if opcion=="si":
		tamaño_celdas=pedir_celda()
		colores_elegidos=pedir_colores()
		espejado_elegido=pedir_espejado()
		return dimension_fractal,fractal_inicial,nombre_archivo,tamaño_celdas,colores_elegidos,espejado_elegido
	return dimension_fractal,fractal_inicial,nombre_archivo,CELDAS,COLORES,ESPEJADO

#parametros a usar------------------------------------------------------------

