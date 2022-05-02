# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:59:48 2021

@author: alexi
"""

from math import e

#Ecuacion con la que se va a trabajar return devuelve el valor cuando se le llama a la función
def f(t):
    return ((9.81+(0.01*70.71067812))/(9.81*0.01)-(1-e**(-0.01*t))-t)

#Definir el metodo de biseccion con sus intervalos y tolerancia

def biseccion(a,b,tol):
    m1=a;
    m=b;
    n=0;
    
    #Determinar si nos garantiza una raiz en el intervalo
    if (f(a)*f(b)>0):
        print("La Funcion no cambia de signo")
    
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
    
biseccion(0,107,10**(-6))
        
        