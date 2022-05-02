# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 11:52:12 2021

@author: alexi
"""
print("¿Cuantos puntos inciales desea agregar?")
xb=int(input())
#print(type(xb))
xs=[0]*xb

for k in range(xb):
    ab=float(input("Ingrese el valor de x_%d" %k +" ="))
    xs[k]=ab
#print(xs[1])


Q=[]
for i in range(xb):
    Q.append([0]*xb)
    #print(Q[i])


for g in range(xb):
    Q[g][0]=float(input("Ingrese el valor de Q_%d," %g + "0 ="))

x=3
for i in range(1,xb):
    for j in range(1,xb):
       # print(i,j)
        a=(x-(xs[i-j]))
        b=Q[i][j-1]
        c=a*b
        d=(x-(xs[i]))
        e=(Q[i-1][j-1])
        f=d*e
        h=c-f
        l=(xs[i]-xs[i-j])
        Q[i][j]=h/l

for i in range(1,xb):
    for j in range(1,xb):
        print("Q_%d" %i +",%d" %j +"=",Q[i][j])
