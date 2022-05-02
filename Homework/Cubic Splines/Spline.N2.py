# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 13:51:05 2021

@author: alexi
"""

x=[0.1, 0.2, 0.3, 0.4]
n=len(x)-1
a=[-0.62049958,-0.28398668,0.00660095,0.24842440]
b=[0,0,0,0]
c=[0,0,0,0]
d=[0,0,0,0]


h=[0,0,0]
for i in range(0,n):
    h[i]=float(x[i+1]-x[i])




alp=[0,0,0,0]  
for i in range(1,n):
    alp[i]=float(((3/h[i])*(a[i+1]-a[i])) - ((3/h[i-1])*(a[i]-a[i-1])))

  
l=[0,0,0,0]
mu=[0,0,0,0]
z=[0,0,0,0]

l[0]=1
mu[0]=0
z[0]=0


for i in range(1,n):
    l[i]=float((2*(x[i+1]-x[i-1])-h[i-1]*mu[i-1]))
    mu[i]=float((h[i]/l[i]))
    z[i]=float((alp[i]-h[i-1]*z[i-1])/l[i])


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
