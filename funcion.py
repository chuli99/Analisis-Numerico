import numpy as np
from sympy.parsing.sympy_parser import parse_expr

#Funcion.py convierte la funcion expresada en un objeto Simpy y asigna los valores x,y
def funcion(funcion):
    
    #Convierte la expresion en un objeto sympy
    f = parse_expr(funcion)

    return (f)
