from itertools import product

from clases.Tablero import *
# from .Barco import *
from clases.Conventions import *


jugadas = set()

class Case:
        
    
    def __init__(self, x, y, instances):
      # Adición de las coordenadas
      self.x = x
      self.y = y
      # Queremos poder acceder a una casilla a partir de sus coordenadas
      instances[x, y] = self

      # Generación del nombre de la casilla
      self._generar_nombre()
      # Queremos poder acceder a una casilla a partir de su nombre
      instances[self.nombre] = self

      # Evolución de la casilla
      self.jugada = False
      self.barco = None  # No toca a un barco de momento.

    def _generar_nombre(self):
      """Este método puede ser sobrecargado fácilmente"""
      #LRL: Llama el metodo de COnventions
      self.nombre = Conventions.generar_nombre_casilla(Conventions,self.x, self.y)

    def jugar(self):
      """Describe qué pasa cuando jugamos una casilla"""
      self.jugada = True
      jugadas.add(self)

      if self.barco is not None:
          self.barco.casillas_jugadas.append(self._generar_nombre())     
          #LRL: Controlamos si el barco esta Tocado u Hundido por la diferencia entre casillas jugadas y ocupadas
          if len(self.barco.casillas_jugadas) - len(self.barco.casillas) == 0:
               print("Hundido !!")
          else:
               print("Tocado !")
      else:
           print("Agua !")

    @classmethod
    def generar_casillas(self, instances):
        # !LRL: Llama la clase correctamente
      for x, y in product(range(Conventions.tablero_num_lineas),
                          range(Conventions.tablero_num_columnas)):
          Case(x, y,instances)

    def __str__(self):
      """Sobrecarga del método de transformación en cadena"""
      if not self.jugada:
          from juego import CASO_NO_JUGADO
          return CASO_NO_JUGADO
      elif self.barco is None:
          from juego import CASO_AGUA
          return CASO_AGUA
      from juego import CASO_TOCADO
      return CASO_TOCADO
