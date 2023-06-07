import numpy as np
from sympy import *

#Declaro simbolos 
x, y, z = symbols('x y z',real=True)

def calcular_df_dx(funcion):
    #Calcular la derivada parcial de f con respecto a x
    
    df_dx = diff(funcion,x)
    
    return df_dx

def calcular_df_dy(funcion):
    #Calcular la derivada parcial de f con respecto a y
    df_dy = diff(funcion,y)
    
    return df_dy

def calcular_df_dz(funcion):
    #Calcular la derivada parcial de f con respecto a z
    df_dz = diff(funcion,z)
    
    return df_dz
    
