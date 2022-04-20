#escritura del archivo
def escribir_archivo(nombrearchivo,diccionario,dimension,colores):
	"Funcion que crea y escribe la imagen ppm"
	ancho,alto=dimension
	salto_de_linea="\n"
	color1,color2,color3,color4=list(colores.keys())
	with open(nombrearchivo,"w") as archivo:
		archivo.write("P3"+salto_de_linea)
		archivo.write(str(ancho)+" "+str(alto)+salto_de_linea)
		archivo.write("255"+salto_de_linea)
		archivo.write(colores[color1]+salto_de_linea)
		archivo.write(colores[color2]+salto_de_linea)
		archivo.write(colores[color3]+salto_de_linea)
		archivo.write(colores[color4]+salto_de_linea)

		for fila in range(alto):
			for columna in range(ancho):
				if ((columna,fila) not in diccionario) or diccionario[columna,fila]==0:
					archivo.write(colores[color1]+salto_de_linea)
					continue
				if diccionario[columna,fila]==1:
					archivo.write(colores[color2]+salto_de_linea)
					continue
				if diccionario[columna,fila]==2:
					archivo.write(colores[color3]+salto_de_linea)
					continue
				if diccionario[columna,fila]==3:
					archivo.write(colores[color4]+salto_de_linea)
					continue

