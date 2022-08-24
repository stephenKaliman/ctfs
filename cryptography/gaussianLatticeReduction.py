import numpy as np
import math as m

u = np.array([846835985, 9834798552])
v = np.array([87502093, 123094980])
print(u)
print(v)
while(1==1):
    if(np.dot(v,v) < np.dot(u,u)):
        v = v-u
        u = v+u
        v = u-v
    fact = m.floor(np.dot(u,v)/np.dot(u,u))
    if(fact==0):
        break
    v = v-fact*u
flag = np.dot(u,v)
print(flag)
print(u)
print(v)
