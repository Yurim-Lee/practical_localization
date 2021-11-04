from sympy import *
import scipy.integrate as integrate
import scipy.special as special
import time
import math

t=4 #임의의 시간
a=[0.01, 0.0003, -0.0848, -0.0022, 0.0012, -0.0344]
#가속도 센서의 값 논문에서는 단순히 센서 값이라고 나오는데 데이터는 x,y,z임.무엇으로 해야 할지?
gyroX=[0, -0.005, -0.046, -0.002, -0.002, -0.002, 0.01]
gyroY=[0, 0.028, 0.018, 0.029, 0.029, 0.05, 0.049]
gyroZ=[0, 0.009, -0.009, -0.009, -0.009, -0.03, -0.004]
#gyro=[0.032, 0.0343, 0.0848, 0.0322, 0.0432, 0.0334]#회전 센서로 구해진 각도값
magX=[-1.024, -1.024, -3.468, -3.084, -1.379, -1.379]
magY=[3.676, 3.676, 3.946, 2.995, 3.03, 3.03]
magZ=[-46.664, -46.664, -45.906, -45.23, -45.88, -45.88]
#mag=[0.002, 0.0003, 0.0848, 0.0022, 0.0012, 0.5654]#자기장 센서로 구해진 각도값

#1-1. 회전센서 각도값 계산
radian_to_degree=180/3.14159
deg_per_sec=32767/250
now=0
past=0
dt=0
millis = int(round(time.time() * 1000))

sumGyroX=0
sumGyroY=0
sumGyroZ=0
angleGX=0
angleGY=0
angleGZ=0
angleGyX=list()
angleGyY=list()
angleGyZ=list()

for o in range(7):
    sumGyroX+=gyroX[o]
    averGyroX=sumGyroX/6
    sumGyroY+=gyroY[o]
    averGyroY=sumGyroY/6
    sumGyroZ+=gyroZ[o]
    averGyroZ=sumGyroZ/6

print("GyroX 평균 :", averGyroX)
print("GyroY 평균 :", averGyroY)
print("GyroZ 평균 :", averGyroZ)

past = int(round(time.time() * 1000))

for p in range(7):
    now = int(round(time.time() * 1000))
    dt = (now - past) / 1000.0
    past = now
    angleGX+= ((gyroX[p] - averGyroX) / deg_per_sec) * dt
    angleGY+= ((gyroY[p] - averGyroY) / deg_per_sec) * dt
    angleGZ+= ((gyroZ[p] - averGyroZ) / deg_per_sec) * dt

    print("Gyro X 각도:", angleGX)
    print("Gyro Y 각도:", angleGY)
    print("Gyro Z 각도:", angleGZ)

    time.sleep(20)
    angleGyX.append(angleGX)
    angleGyY.append(angleGY)
    angleGyZ.append(angleGZ)
    #지난번에 Y축 기준으로 하자고 함. 일단 3개 다 적용. 3가지 중 하나를 gyro에 적용하면 됨.

print(angleGyX)
print(angleGyY)
print(angleGyZ)

#1-2. 회전센서 각도값 계산
anglemag=0
for q in range(7):
    anglemag=math.tan(math.pi*((Y-magY/X-magX)/180)#X,Y는 어떤 수를 넣어야 할지 모르겠음. 축?
    print(f"{anglemag:.6f}"))

#2-1.이동거리
for i in a:
    #1차 적분 가속도->속도
    f = integrate.quad(lambda x: exp(i), t-1, t)
    print("속도 : ", f)
    #2차 적분 속도->이동거리
    #distance = integrate(exp(f), (f-0, t - 1, t))
    distance = integrate.quad(lambda x: f[1] - 1 + 1, t - 1, t)
    print("이동거리 : ", distance)

#2-2.이동방향
for k in gyro:
    for l in mag:
        #아래 4개는 임의의 값
        l_gyro=2#회전 센서 임계값
        l_mag=3#자기장 센서 임계값
        for m in range(5):
            mag_C=mag[m+1]-mag[m]#자기장센서 각도 차이(변화율)
            print("자기장 변화율 : ",mag_C)

        th_tm=0.1#시간이 t-1일 때 이동방향(임의의 값)

        if k>float(2):
            if mag_C>float(3):
                th_t=((l+(th_tm+k))/2)
                print("이동방향 : ", th_t)
            elif mag_C<=float(3):
                th_t=(th_tm+k)
                print("이동방향 : ", th_t)
        elif k<=float(2):
            th_t=th_tm
            print("이동방향 : ", th_t)

