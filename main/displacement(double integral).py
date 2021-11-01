from sympy import *
import scipy.integrate as integrate
import scipy.special as special

t=4 #time
a = [1,0.0015,0.0012] #Accelerometer

#1차 적분
f = integrate.quad(lambda x: exp(a[0]), t-1, t)
print(f)

#2차 적분
distance = integrate.quad(lambda x: f[1]+0, t-1, t)
print(distance)
