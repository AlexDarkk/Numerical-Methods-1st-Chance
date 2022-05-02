# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:20:46 2021

@author: alexi
"""

from numpy import sign
from numpy.lib.scimath import sqrt

def muller(f,x0,x1,x2,tol):
    error=1*10**3
    x3=0
    while error > tol:
        c=f(x2)
        b=((x0-x2)**2*(f(x1)-f(x2))-(x1-x2)**2*(f(x0)-f(x2)))/((x0-x2)*(x1-x2)*(x0-x1))
        a=((x1-x2)*(f(x0)-f(x2))-(x0-x2)*(f(x1)-f(x2)))/((x0-x2)*(x1-x2)*(x0-x1))
        x3=x2-(2*c)/(b+sign(b)*sqrt(b**2-4*a*c))
        error = abs(x3-x2)
        x0 = x1; x1 = x2; x2 = x3;
    return print(x3)

f = lambda x: 600*x**4-550*x**3+200*x**2-20*x-1
muller(f,0.1,0.2,1,(1*10**-4))    