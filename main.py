import derivada
import numpy as np
from sympy import *

x, y, z = symbols('x y z',real=True)


#Pido al usuario que ingrese la función en términos de x,y,z
f = cos(x)


#Obtengo derivada respecto de x
derivada_x = derivada.calcular_df_dx(f)

#Obtengo derivada respecto de y
derivada_y = derivada.calcular_df_dy(f)

print(derivada_x)
print(derivada_y)