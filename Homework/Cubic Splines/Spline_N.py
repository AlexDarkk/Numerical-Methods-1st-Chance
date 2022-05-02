# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:22:12 2021

@author: alexi
"""

x=[-0.5,-0.25,0]
n=len(x)-1
a=[-0.0247500,0.3349375,1.1010000]
b=[0,0,0]
c=[0,0,0]
d=[0,0,0]


h=[0,0]
for i in range(0,n):
    h[i]=x[i+1]-x[i]




#alpha i, el tamaño del vector se determina por n
alp=[0,0,0]  
for i in range(1,n):
    alp[i]=((3/h[i])*(a[i+1]-a[i])) - ((3/h[i-1])*(a[i]-a[i-1]))

  
l=[0,0,0]
mu=[0,0,0]
z=[0,0,0]

l[0]=1
mu[0]=0
z[0]=0


for i in range(1,n):
    l[i]=(2*(x[i+1]-x[i-1])-h[i-1]*mu[i-1])
    mu[i]=(h[i]/l[i])
    z[i]=(alp[i]-h[i-1]*z[i-1])/l[i]


l[n]=1
z[n]=0
c[n]=0


j=n-1
while(j>=0):
  c[j]=z[j]-mu[j]*c[j+1]
  b[j]=(a[j+1]-a[j])/h[j]-h[j]*(c[j+1]+2*c[j])/3
  d[j]=(c[j+1]-c[j])/(3*h[j])
  j=j-1

print(d)
