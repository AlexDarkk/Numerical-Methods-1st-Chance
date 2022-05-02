# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 18:13:12 2021

@author: alexi
"""
x=[0,2,5,8,13]
y=[69,117,190,303]
y_=[23,23,24,23,22]
Q=[]

for i in range(0,10):
    Q.append([0]*10)
#print("Matriz Q")
for i in range(0,10):
    print(Q[i])

#print("Matriz z")
z=[]
for i in range(8):
    z.append(0)
        
 
for i in range(4):
    z[2*i]=x[i]
    z[(2*i)+1]=x[i]
    Q[2*i][0]=y[i]
    Q[(2*i)+1][0]=y[i]
    Q[(2*i)+1][1]=y_[i]
    if i != 0:
        a=(Q[2*1][0]-Q[(2*i)-1][0])
        b=(z[2*i]-z[(2*1)-1])
        Q[2*i][1]=a/b



for i in range(2,8):
    for j in range(2,i):
        a=Q[i][j-1]
        b=Q[i-1][j-1]
        c=z[i]
        d=z[i-j]
        e=a-b
        f=c-d
        Q[i][j]=e/f

for i in range(0,10):
    for j in range(0,10):
         print("Q_%d" %i +",%d" %j +"=",Q[i][j])