from math import *
from mpmath import *
#아래능 일단 임의의 값 입력함
alpha=42.0
beta=31.0
AB=10.0

gamma=0.0
AC=0.0
BC=0.0
RC=0.0
MR=0.0
MC=0.0

gamma=180-(alpha+beta)
AC=AB*sin(pi*beta/180.0)/sin(pi*gamma/180.0)
BC=AB*sin(pi*beta/180.0)/sin(pi*gamma/180.0)
RC=AC*sin(pi*alpha/180.0)

MR=(AB/2)-(BC*cos(pi*beta/180.0))
MC=sqrt((MR*MR)+(RC*RC))

print("MC : ", MC)