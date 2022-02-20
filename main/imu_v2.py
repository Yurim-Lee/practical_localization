from sympy import *
import scipy.integrate as integrate
import scipy.special as special
import time
import math
from math import *
from mpmath import *


t=4 #임의의 시간
#가속도 센서의 값 논문에서는 단순히 센서 값=>X값을 기준으로 작성
#가속도 센서, 회전 센서, 자기장 센서 초기값은 모두 0
accel=[0.001, 6.125, 5.632, 6.69, 5.993, 6.618, 5.68]
#회전 센서값
gyroX=[0.001, 0.012, -0.118, 0.064, -0.505, -0.086, -0.533]
#gyroY=[0, 0.028, 0.018, 0.029, 0.029, 0.05, 0.049]
#gyroZ=[0, 0.009, -0.009, -0.009, -0.009, -0.03, -0.004]
#자기장 센서값
magX=[0.001, -30.341, -31.151, -31.86, -29.842, -17.612, -4.884]
magY=[0.001, 4.182, 7.655, 7.199, 6.572, 7.802, 26.855]
#magZ=[-46.664, -46.664, -45.906, -45.23, -45.88, -45.88]

#1. 회전센서 각도값과 자기장 센서 각도값 필요
#1-1. 회전센서 각도값 계산
radian_to_degree=180/3.14159
deg_per_sec=32767/250
now=0
past=0
dt=0
millis = int(round(time.time() * 1000))

sumGyroX=0
#sumGyroY=0sumGyroZ=0
angleGX=0
#angleGY=0angleGZ=0
angleGyX=list()
#angleGyY=list()angleGyZ=list()

for i in range(len(gyroX)):
    sumGyroX+=gyroX[i]
    averGyroX=sumGyroX/len(gyroX)
    #sumGyroY+=gyroY[i]averGyroY=sumGyroY/6
    #sumGyroZ+=gyroZ[i]averGyroZ=sumGyroZ/6

print("회전센서 GyroX 평균 :", averGyroX)
#print("GyroY 평균 :", averGyroY)print("GyroZ 평균 :", averGyroZ)

past = int(round(time.time() * 1000))

mag=[]

for j in range(len(gyroX)):
    now = int(round(time.time() * 1000))
    dt = (now - past) / 1000.0
    print("dt:", dt)
    past = now
    #print(past)
    #print(now)
    angleGX+= ((gyroX[j] - averGyroX) / deg_per_sec) * dt
    #angleGY+= ((gyroY[j] - averGyroY) / deg_per_sec) * dt
    #angleGZ+= ((gyroZ[j] - averGyroZ) / deg_per_sec) * dt

    #print("Gyro X 각도:", angleGX)
    #print("Gyro Y 각도:", angleGY)
    #print("Gyro Z 각도:", angleGZ)

    time.sleep(20)
    angleGyX.append(angleGX)
    #angleGyY.append(angleGY)angleGyZ.append(angleGZ)

# 1-2.자기장센서 각도값 계산
    az = 90 - atan(magY[j]/magX[j])*180/3
    mag.append(az)

print("회전센서 GyroX 각도:", angleGyX)
print("자기장센서 각도:", mag)


#2. 위치 계산을 위한 이동거리, 이동방향 구하기
#2-1.이동거리
distance=[]
for k in accel:
    dist = []
    #1차 적분 가속도->속도
    f = integrate.quad(lambda x: exp(k), t-1, t)
    print("속도: ", f)
    f=list(f)
    for s in f:
        #2차 적분 속도->이동거리
        #distance = integrate(exp(f), (f-0, t - 1, t))
        d = integrate.quad(lambda x: exp(s), t-1, t)
        d=list(d)
        dist.append(d[0])
    print("이동거리 : ", dist[0])
    distance.append(dist[0])
    t=t+1
print("이동거리 결과 값 : ", distance)#튜플로 나오는 것 중 뒤에 값만 들어가게 어떻게 할지...


#2-2.이동방향
th_tm=3#시간이 t-1일 때 이동방향(임의의 값)
th=[]
for m in range(len(mag)):
    l_gyro=2#1.회전 센서 임계값 논문 그대로 적음(임의의 값)
    l_mag=3#2.자기장 센서 임계값 논문 그대로 적음(임의의 값)
    #for m in range(len(mag)-1):
    mag_C=mag[m]-mag[m-1]#자기장센서 각도 차이(변화율)
    print("자기장 각도 변화율 : ",mag_C)

    if m>float(2): #회전센서 각도 값이 회전 센서 임계값 2보다 클 경우(식 2의 1, 2)
        if mag_C>float(3): #자기장 각도 변화율이 자기장 센서 임계값 3보다 클 경우(식 2의 1)
            th_t=((mag[m]+(th_tm+angleGyX[m]))/2)
            th_tm=th_t
            th.append(th_t)
            print("이동방향 : ", th_t)
        elif mag_C<=float(3):#자기장 각도 변화율이 자기장 센서 임계값 3보다 작거나 같을 경우(식 2의 2)
            th_t=(th_tm+angleGyX[m])
            th_tm = th_t
            th.append(th_t)
            print("이동방향 : ", th_t)
    elif m<=float(2): #회전센서 각도 값이 회전 센서 임계값 2보다 작거나 같을 경우(식 2의 3)
        th_t=th_tm
        th_tm = th_t
        th.append(th_t)
        print("이동방향 : ", th_t)
print("이동방향들 :",th)
print(len(th))


#3 사용자 위치 계산
# t-1일때 STA 좌표(x,y) 임의의 값 (1,1)
bx=[1]
by=[1]
xafter = []  #t일때 좌표. output
yafter = []  #t일때 좌표. output

for n in range(len(th)):
    xplus = bx[n] + distance[n]*cos(th[n])
    yplus = by[n] + distance[n]*sin(th[n])

    bx.append(xplus)
    by.append(yplus)
    xafter.append(xplus)
    yafter.append(yplus)

print(xafter)
print(yafter)
