# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 16:01:50 2021

@author: alexi


[-0.62049958, -0.28398668, 0.00660095, 0.2484244] a
[3.5850208199999996, 3.140329438666668, 2.6666773253333327, 0] b
[-2.149840786666651, -2.29707302666667, -2.439448106666683, -2.5743885466666385] c
[-0.49077413333339587, -0.4745836000000441, -0.44980146666651794, 0] d



"""
import matplotlib.pyplot as plt
import numpy as np

def s0(x):
   return  -0.62049958 + 3.5850208199999996*(x-0.1) - 2.149840786666651*((x-0.1)**2) - 0.49077413333339587*((x-0.1)**3)
    

def s1(x):
    return -0.28398668 + 3.140329438666668*(x-0.2) - 2.29707302666667*((x-0.2)**2) - 0.4745836000000441*((x-0.2)**3)

def s2(x):
    return  0.00660095 + 2.6666773253333327*(x-0.3)  - 2.439448106666683*((x-0.3)**2) - 0.44980146666651794*((x-0.3)**3)

a = 0.1
b = 0.2
c = 0.3
d = 0.4

x=np.linspace(a,d,100)
y=np.piecewise(x,[(a<=x) & (x<b), (b<=x) & (x<=c), (c<=x) & (x<=d)], [lambda x:s0(x), lambda x:s1(x), lambda x:s2(x)])

plt.plot(x[x<b],s0(x[x<b]), label='spline 0', c='r')
plt.plot(x[(b<=x) & (x<=c)],s1(x[(b<=x) & (x<=c)]), label='spline 1', c='g')
plt.plot(x[(c<=x) & (x<=d)],s2(x[(c<=x) & (x<=d)]), label='spline 2', c='y')
plt.grid(True)
plt.title('Spline Cubico Condicionado')
plt.legend()