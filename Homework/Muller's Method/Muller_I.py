# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:55:38 2021

@author: alexi
"""
from numpy.lib.scimath import sqrt

f = lambda x: 600*x**4-550*x**3+200*x**2-20*x-1

def muller(f,p0,p1,p2,tol,n):
    h1=p1-p0
    h2=p2-p1
    d_1=(f(p1)-f(p0))/h1
    d_2=(f(p2)-f(p1))/h2
    d=(d_2-d_1)/(h2+h1)
    i=3
    while i<=n:
        b=d_2+h2*d
        D= sqrt(b**2-4*f(p2)*d)
        if abs(b-D) < abs(b+D):
            E=b+D
        else:
            E=b-D
        h=-2*f(p2)/E
        p=p2+h
        if abs(h) < tol:
         return print(p,i)
        p0=p1
        p1=p2
        p2=p
        h1=p1-p0
        h2=p2-p1
        d_1=(f(p1)-f(p0))/h1
        d_2=(f(p2)-f(p1))/h2
        d=(d_2-d_1)/(h2+h1)
        i=i+1
     
muller(f,0.1,0.11,0.2,1*10**-4,100)

     
    