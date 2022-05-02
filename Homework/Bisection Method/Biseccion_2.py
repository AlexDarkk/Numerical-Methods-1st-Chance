# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 12:14:23 2021

@author: alexi
"""

#from math import e

#Ecuacion con la que se va a trabajar return devuelve el valor cuando se le llama a la función
def f(x):
    return x**2-3

#Definir el metodo de biseccion con sus intervalos y tolerancia

def biseccion(a,b,tol):
    m1=a;
    m=b;
    n=0;
    
    #Determinar si nos garantiza una raiz en el intervalo
    if (f(a)*f(b)>0):
        print("La Funcion no cambia de signo")
    else:
    #Inicia el ciclo
        while (abs(m1-m)>tol):
            m1=m;
            m=(a+b)/2;
            if(f(a)*f(m)<0): #Signos opuestos en los puntos a,m
                b=m;
            if(f(m)*f(b)<0): #Signos opuestos en los puntos m,b 
                a=m;
            print("Intervalo: [",a,",",b,"]")
            n+=1;
        print("Numero de iteraciones",n,"=",m," es aceptable")
    
biseccion(0,4,10**(-4))