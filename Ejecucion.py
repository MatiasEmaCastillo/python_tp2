from Contruccion import *
from Archivo import *
from Parametros import *

#EJECUCION DEL PROGRAMA
def main():
    "Funcion principal que relaciona todas las funciones anteriores y crea el fractal"
    fractal,nombre_de_archivo,fractal_inicial,celdas,colores,espejado=definir_parametros()
    fractal_inicial=recorrer_fractal(fractal_inicial,fractal)
    fractal_ampliado=aumentar_fractal(fractal_inicial,celdas)
    ANCHO=0
    ALTO=1
    dimension=fractal[ANCHO]*celdas[ANCHO],fractal[ALTO]*celdas[ALTO]
    fractal_ampliado,dimension=construccion_final(fractal_ampliado,dimension,espejado)
    escribir_archivo(nombre_de_archivo,fractal_ampliado,dimension,colores)


main()
