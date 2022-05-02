# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(-0.5,1.57,500)
y= (2*x)*np.cos(2*x)-(x-2)**2
y_d=-4+(6*x)-(x**2)
y_t=-4+(6*x)-(x**2)-(4*x**3)

plt.plot(x,y,"k:", label="2xCos(2x)-(x-2)^2")
plt.plot(x,y_d,label="-4+6x-x^2")
plt.plot(x,y_t,label="-4+6x-x^2-4x^3")
plt.grid()
plt.title("Polinomio de Taylor Grado 2 y 3 alrededor de 0") 

plt.legend(loc=3)