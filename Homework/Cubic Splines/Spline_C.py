# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 18:17:36 2021

@author: alexi
"""

x=[0.1, 0.2, 0.3, 0.4]
n=3
a=[-0.62049958,-0.28398668,0.00660095,0.24842440]
b=[0,0,0,0]
c=[0,0,0,0]
d=[0,0,0,0]
FPO=3.58502082
FPN=2.16529366

h=[0,0,0]
for i in range(0,n):
    h[i]=x[i+1]-x[i]
    
alp=[0,0,0,0]

alp[0]=(3*(a[1]-a[0]))/h[0]-3*FPO
alp[n]=3*FPN-3*(a[n]-a[n-1])/h[n-1]


for i in range(1,n):
    alp[i]=(3*(a[i+1]-a[i])/h[i])-(3*(a[i]-a[i-1])/h[i-1])
    #print(alp[i])
    
l=[0,0,0,0]
mu=[0,0,0,0]
z=[0,0,0,0]

l[0]=2*h[0]
mu[0]=0.5
z[0]=alp[0]/l[0]


for i in range(1,n):
    l[i] = 2*(x[i+1]-x[i-1])-h[i-1]*mu[i-1]
    mu[i]= h[i]/l[i]
    z[i]= (alp[i]-h[i-1]*z[i-1])/l[i]

l[n]=h[n-1]*(2-mu[n-1])
z[n]=(alp[n]-h[n-1]*z[n-1])/l[n]
c[n]=z[n]



j=n-1
while(j>=0):
  c[j]=z[j]-mu[j]*c[j+1]
  b[j]=(a[j+1]-a[j])/h[j]-h[j]*(c[j+1]+2*c[j])/3
  d[j]=(c[j+1]-c[j])/(3*h[j])
  j=j-1


print(d)