import derivada
import numpy as np
from sympy import *

x, y, z = symbols('x y z',real=True)


#Pido al usuario que ingrese la función en términos de x,y,z
f = x*y**2/z

x1 = 2
x2 = 3
x3 = 1

dx = 0.1
dy = 0.2
dz = 0.1


#Obtengo derivada respecto de x
derivada_x = derivada.calcular_df_dx(f)

#Obtengo derivada respecto de y
derivada_y = derivada.calcular_df_dy(f)

#Obtengo derivada respecto de z
derivada_z = derivada.calcular_df_dz(f)


#Lambdify permite convierte a las derivadas para poder ser remplazadas por los puntos
fun_x = lambdify([x,y,z],derivada_x)
fun_y = lambdify([x,y,z],derivada_y)
fun_z = lambdify([x,y,z],derivada_z)

print(f"{derivada_x} y en el punto {x1}, {x2}, {x3} es: {fun_x(x1,x2,x3)}")
print(f"{derivada_y} y en el punto {x1}, {x2}, {x3} es: {fun_y(x1,x2,x3)}")
print(f"{derivada_z} y en el punto {x1}, {x2}, {x3} es: {fun_z(x1,x2,x3)}")