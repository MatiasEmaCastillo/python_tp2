#construccion del sandpile
def validar_diccionario(diccionario):
	"Funcion que devuelve True si en los valores del diccionario hay un numero mayor o igual a 4 en caso contrario devuelve False"
	valores=list(diccionario.values())
	for elemento in valores:
		if elemento>=4:
			return True
	return False

def distribuir_granos(dimension,diccionario,posicion,cant):
	"Funcion que distribuye los granos que se van rompiendo en una posicion del fractal"

	ancho,alto=dimension
	columna,fila=posicion
	distribucion=cant//4
	sobrante=cant%4
	fila_anterior=fila-1
	fila_posterior=fila+2
	columna_anterior=columna-1
	columna_posterior=columna+2
	for fila_actual in range(fila_anterior,fila_posterior):
		if (fila_actual>=0 and fila_actual<alto) and fila_actual!=fila:
			diccionario[columna,fila_actual]=diccionario.get((columna,fila_actual),0)+distribucion
	for columna_actual in range(columna_anterior,columna_posterior):
		if (columna_actual >= 0 and columna_actual < ancho) and columna_actual != columna:
			diccionario[columna_actual,fila]=diccionario.get((columna_actual,fila),0)+distribucion
	diccionario[columna,fila]=sobrante
	return diccionario

def sumar_diccionarios(diccionario1,diccionario2):
	"Funcion que recibe 2 diccionarios y suma los valores de cada de uno"
	for clave in diccionario2:
		diccionario1[clave]=diccionario1.get(clave,0)+diccionario2[clave]
	return diccionario1

def recorrer_fractal(tablero,dimension):
	"Funcion que reparte todos los granos de todas las posiciones del fractal"
	while validar_diccionario(tablero):
		diccionario_aux={}
		for clave in tablero:
			cant_granos=tablero[clave]
			if cant_granos < 4:
				continue
			diccionario_aux=distribuir_granos(dimension,diccionario_aux,clave,cant_granos)
			tablero[clave]=0
		tablero=sumar_diccionarios(tablero,diccionario_aux)
	return tablero


def aumentar_fractal(diccionario,celdas):
	"Funcion que aumenta la resolucion de fractal"
	tablero_nuevo={}
	for clave in diccionario:
		posicion=clave
		cant=diccionario[clave]
		inicio_columnas=posicion[0]*celdas[0]
		final_columnas=(posicion[0]*celdas[0])+celdas[0]
		inicio_filas=posicion[1]*celdas[1]
		final_filas=(posicion[1]*celdas[1])+celdas[1]
		for x in range(inicio_columnas,final_columnas):
			for j in range(inicio_filas,final_filas):
				tablero_nuevo[x,j]=cant

	return tablero_nuevo


def espejado_vertical(diccionario,dimension,vecesaespejar):
	"Funcion que espeja verticalmente el fractal"

	if vecesaespejar==1:
		return diccionario,dimension
	contador=1
	altura_inicial=dimension[1]
	while contador<vecesaespejar:
		diccionario_aux={}
		altura_final=altura_inicial*2
		for clave in diccionario:
			fila_a_espejar=clave[1]
			fila_espejada=altura_final-(1+fila_a_espejar)
			diccionario_aux[clave[0],fila_espejada]=diccionario[clave]
		diccionario=sumar_diccionarios(diccionario,diccionario_aux)
		altura_inicial=altura_final
		contador+=1
	dimension_nueva=dimension[0],altura_final
	return diccionario,dimension_nueva


def espejado_horizontal(diccionario,dimension,vecesaespejar):
	"Funcion que espeja horizontalmente el fractal"
	if vecesaespejar==1:
		return diccionario,dimension
	contador=1
	altura_inicial=dimension[0]
	while contador<vecesaespejar:
		diccionario_aux={}
		altura_final=altura_inicial*2
		for clave in diccionario:
			columna_a_espejar=clave[0]
			columna_espejada=altura_final-(1+columna_a_espejar)
			diccionario_aux[columna_espejada,clave[1]]=diccionario[clave]
		diccionario=sumar_diccionarios(diccionario,diccionario_aux)
		altura_inicial=altura_final
		contador+=1
	dimension_nueva=altura_final,dimension[1]
	return diccionario,dimension_nueva

def construccion_final(diccionario,dimension,espejado):
	"Funcion que espeja vertical y horizontalmente el fractal"
	diccionario,dimension=espejado_vertical(diccionario,dimension,espejado[0])
	diccionario,dimension=espejado_horizontal(diccionario,dimension,espejado[1])
	return diccionario,dimension
