import derivada
import numpy as np
import os
from sympy import *
import tkinter


x, y, z = symbols('x y z',real=True)

def main():
    
    clear_screen()
    print_menu()
    choice = input("Selecciona una opción: ")
    process_choice(choice)
        
        

def print_menu():
    menu = """
        ╔════════════════════════════════════════════════════════════╗
        ║                  Propagación del error                     ║
        ║             en la evaluación de funciones                  ║
        ║                                                            ║
        ║    ①   Calcular error de la funcion                        ║
        ║    ②   Calcular error en variables                         ║
        ║    ③   Mostrar que variable tiene                          ║
        ║        mayor incidencia de error en la funcion             ║
        ║    ④   Salir                                               ║
        ║                                                            ║
        ╚════════════════════════════════════════════════════════════╝
    """
    print(menu)


def process_choice(choice):
    if choice == '1':
        print("Has seleccionado la Opción 1.")
        opcion1()
    elif choice == '2':
        print("Has seleccionado la Opción 2.")
    elif choice == '3':
        print("Has seleccionado la Opción 3.")
    elif choice == '4':
        print("Saliendo del programa...")
        exit()
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")


    

def opcion1():

    #Pido al usuario que ingrese la función en términos de x,y,z
    
    x, y, z = symbols('x y z',real=True)
    print("Ingrese la funcion en terminos de x,y,z:")
    f = input()
    #f = x*y**2/z
    #f = 5*x*y - x*cos(z) + x**2 + z**8*y**2
    #Implementar regex para validar la funcion en un futuro
    print(f)

    #Valores de x,y,z y errores relativos (cotas)
    print("Ingrese el valor de x:")
    x1 = float(input())
    #x1 = 2
    print("Ingrese el valor de y:")
    x2 = float(input())
    #x2 = 3

    print("Ingrese el valor de z:")
    x3 = float(input())

    print("Ingrese la cota de  error de x:")
    dx = float(input())
    #dx = 0.1
    print("Ingrese la cota de  error de y:")
    dy = float(input())
    #dy = 0.2
    print("Ingrese la cota de  error de z:")
    dz = float(input())
    #dz = 0.1
    print("a")
    print(f"Los valores ingresados son: ")
    print(f"Funcion: {f}")
    print(f"Valor de x: {x1} +- {dx}")
    print(f"Valor de y: {x2} +- {dy}")
    print(f"Valor de z: {x3} +- {dz}")
    print("Confirma los valores? (s/n)")
    confirm = input()
    if confirm == 's':
        print("Calculando...")
        #Obtengo derivada respecto de x
        derivada_x = derivada.calcular_df_dx(f)
        print(derivada_x)
        #Obtengo derivada respecto de y
        derivada_y = derivada.calcular_df_dy(f)
        print(derivada_y)
        #Obtengo derivada respecto de z
        derivada_z = derivada.calcular_df_dz(f)
        print(derivada_z)

        #Lambdify permite convierte a las derivadas para poder ser remplazadas por los puntos
        fun_x = lambdify([x,y,z],derivada_x)
        fun_y = lambdify([x,y,z],derivada_y)
        fun_z = lambdify([x,y,z],derivada_z)

        print("La funcion tiene un error de:")
        print(fun_x(x1,x2,x3)+fun_y(x1,x2,x3)+fun_z(x1,x2,x3))
    
        print(f"{derivada_x} y en el punto {x1}, {x2}, {x3} es: {fun_x(x1,x2,x3)}")
        print(f"{derivada_y} y en el punto {x1}, {x2}, {x3} es: {fun_y(x1,x2,x3)}")
        print(f"{derivada_z} y en el punto {x1}, {x2}, {x3} es: {fun_z(x1,x2,x3)}")
    else:
        print("Ingrese los valores nuevamente")
        opcion1()
    


#if (abs(fun_x(x1,x2,x3))*dx) > (abs(fun_y(x1,x2,x3))*dy):
#    if (abs(fun_x(x1,x2,x3))*dx) > (abs(fun_z(x1,x2,x3))*dz):
#        mayor = 'X'
#    else:
#        mayor = 'Z'
#else:
#    if (abs(fun_y(x1,x2,x3))*dy) > (abs(fun_z(x1,x2,x3))*dz):
#        mayor = 'Y'
#    else:
#        mayor = 'Z'



#print(f"{mayor} tiene mayor incidencia en el error en w.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



if __name__ == '__main__':
    main()
