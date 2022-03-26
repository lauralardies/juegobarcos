from itertools import repeat, product
from random import choice

#!LRL: Corrige los comandos de importacion de clases  
# from clases.Tablero import Tablero
from clases.Case import *
from clases.Conventions import *

#Cambiamos de nombre al contenedor de todos los barcos
instances_barcos =[]

class Barco:
    
    #!LRL: las variables instances y casillas_ocupasas se pasan por parametro     
    def __init__(self, longitud,instances,casillas_ocupadas):
            self.longitud = longitud
            from juego import ORIENTACIONES
            self.orientacion = choice(ORIENTACIONES)
            self.tocado = False
            self.hundido = False
            self.casillas = []
            self.casillas_jugadas=[]
            
            # performance / legibilidad:
            num_lineas = Conventions.tablero_num_lineas
            num_columnas = Conventions.tablero_num_columnas
            num2l = Conventions.generar_num_linea
            num2c = Conventions.generar_num_columna

            while True:
                #LRG: Eliminar el import
                from juego import HORIZONTAL
                if self.orientacion == HORIZONTAL:
                    rang = choice(range(num_lineas))
                    primero = choice(range(num_columnas + 1 - longitud))
                    letra = num2l(rang)
                    cifras = [num2c(x) for x in range(primero, primero + longitud)]
                    #!LRL: Guarda las casillas ocupadas por el barco en la variable casillas 
                    self.casillas=({l + c
                                      for l, c in product(repeat(letra, longitud), cifras)})
                else:
                    rang = choice(range(num_columnas))
                    primero = choice(range(num_lineas + 1 - longitud))
                    cifra = num2c(rang)
                    letras = [num2l(x) for x in range(primero, primero + longitud)]
                    # Crear el barco
                    #!LRL: El barco se guarda en casillas 
                    self.casillas=({l + c
                                      for l, c in product(letras, repeat(cifra, longitud))})
                
                for existente in instances_barcos:
                    if self.casillas.intersection(existente):
                        break  # break relativo al "for existente in barcos:"
                else:                
                    # Agregar el barco en el contenedor de barcos            
                    # !LRL: instances es el diccionario de casillas. ¿tenemos contenedor de barco? 
                    instances_barcos.append(self.casillas)
                    
                    #!LRL Se modifica la llamada a instances por el nombre de la casilla
                    # Informar la casilla que contiene un barco.
                    for casilla in self.casillas:
                        instances[casilla].barco = self
                        
                    # Agregar estas casillas a las casillas ocupadas :
                    casillas_ocupadas |= self.casillas
                    #casillas_ocupadas.append( self.casillas)
                    break  # break relativo al "while True:"

    #!LRL: las variables instances y casillas_ocupadas se pasan por parametro     
    def generar_barcos(instances,casillas_ocupadas):
        for longitud in Conventions.barcos_longitud:
            Barco(longitud,instances,casillas_ocupadas)
                




