# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 21:40:24 2021

[-0.62049958, -0.28398668, 0.00660095, 0.2484244] a
[3.455086933333334, 3.1852131333333342, 2.617076433333333, 0] b
[0.0, -2.6987380000000014, -2.9826290000000095, 0] c
[-8.995793333333337, -0.9463033333333606, 9.942096666666695, 0] d
x=[0.1, 0.2, 0.3, 0.4]



[-0.62049958, -0.28398668, 0.00660095, 0.2484244] a
[3.5850208199999996, 3.140329438666668, 2.6666773253333327, 0] b
[-2.149840786666651, -2.29707302666667, -2.439448106666683, -2.5743885466666385] c
[-0.49077413333339587, -0.4745836000000441, -0.44980146666651794, 0] d



"""
import matplotlib.pyplot as plt
import numpy as np

def s0(x):
   return  -0.62049958 + 3.455086933333334*(x-0.1) + 0.0*((x-0.1)**2) - 8.995793333333337*((x-0.1)**3)
    

def s1(x):
    return -0.28398668 + 3.1852131333333342*(x-0.2) - 2.6987380000000014*((x-0.2)**2) - 0.9463033333333606*((x-0.2)**3)

def s2(x):
    return  0.00660095 + 2.617076433333333*(x-0.3)  - 2.9826290000000095*((x-0.3)**2) + 9.942096666666695*((x-0.3)**3)

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
plt.title('Spline Cubico Natural')
plt.legend()


