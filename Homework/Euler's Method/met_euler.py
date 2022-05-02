# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:50:48 2021

@author: alexi
"""
from math import e
from math import cos
from math import sin

def w_a(t,w):
    return t*e**(3*t)-2*w

def w_b(t,w):
    return 1+(t-w)**2

def w_c(t,w):
    return 1+(w/t)

def w_d(t,w):
    return cos(2*t) + sin(3*t)


def o(t,w):
    return t**2 - 2*w
def met_euler(a,b,N):
    """a=int(input("Introduzca el extremo a: "))
    b=int(input("Introduzca el extremo b: "))
    N=int(input("Introduzca el entero N: "))
    """
    h=(b-a)/N
    t=a
    print(h)
    w=int(input("Introduzca el valor inicial para y: "))

    for i  in range(1,N+1):
        w=w+h*(o(t,w))
        print("w_1= ", w)
        t=a + i*h
        print("t_1= ",t)
    return

met_euler(1,5,2)


