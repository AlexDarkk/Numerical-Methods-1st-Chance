# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:45:17 2021

@author: alexi
"""

import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(0,0.5)
y= (2*x)*np.cos(2*x)-(x-2)**2
y_d=-2.0026-(3.44564*(x-0.4))-(5*(x-0.4)**2)
y_t=-2.0026-(3.44564*(x-0.4))-(5*(x-0.4)**2)-(2.021*(x-0.4)**3)

plt.plot(x,y,"k:", label="2xCos(2x)-(x-2)^2")
plt.plot(x,y_d,"r",label="-2-3.44(x-0.4)-5(x-0.4)^2")
plt.plot(x,y_t,"b",label="-2-3.44(x-0.4)-5(x-0.4)^2-2.02(x-0.4)^2")
plt.grid()
plt.title("Polinomio de Taylor Grado 2 y 3 alrededor de 0.4") 

plt.legend(loc=3)