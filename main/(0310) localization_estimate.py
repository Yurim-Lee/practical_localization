# 위치 추정용 코드
# 소은 코드에서 위치 받아서 진민 코드의 초기 위치로 입력
# STA가 실제로 이동한 위치(정답 코드)
# AP 위치, 신호 범위 고정 시킴

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import matplotlib.patches as mpatches

range_list = list()

AP_num = 3  # AP의 개수

# AP의 신호 범위(반지름)
# radius = random.uniform(0, 1)
radius = 2
print("반지름: ", radius)

AP1 = [3.5,4.5]
AP2 = [6.5,4.5]
AP3 = [5,7]
# AP 좌표 선정
# for i in range(0,AP_num):
#     globals()['AP{}'.format(i + 1)] = [random.uniform(1, 2.5), random.uniform(1, 2.5)]

# for j in range(0,AP_num):
#
#
#
# # AP 1을 기점으로 이후 AP들 좌표 범위 설정(최소 1개 이상의 AP가 존재한다는 가정)
# for i in range(1,AP_num+1):
#     globals()['AP{}'.format(i+1)] = [random.randrange(1, 3), random.randrange(1, 3)]
#     # print(globals()['AP{}'.format(i)])
# for i in range(AP_num):
#     for j in range(3):
#         globals()['AP_range{}'.format(i + 1)] = [globals()['AP{}'.format(i + 1)][0] + radius, globals()['AP{}'.format(i + 1)][1] + radius]

# 중점 출력용
for i in range(AP_num):
     print("AP",i+1,"의 중점: ", globals()['AP{}'.format(i+1)])


# STA의 위치 설정
STA = list()
STA_list = list()
X=[0, 1, 2, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 6, 7, 8, 8, 8, 8, 8, 8, 9, 10]
Y=[4, 4, 4, 5, 6, 7, 8, 8, 8, 8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 3, 4, 5, 6, 7, 7, 7]
# [0, 0] -> [2.4, 2.4] -> [2.4, 1.8] -> [1.8, 1.8]
for i in range(len(X)):
    STA = [X[i], Y[i]]
    STA_list.append(STA)
print("단말 STA의 좌표: ", STA_list)

# STA가 이동할 때마다 각각 AP에 속하는지 판단
for i in range(len(X)):
    for j in range(AP_num):
        if(STA_list[i][0]>=globals()['AP{}'.format(j+1)][0]-radius) and (STA_list[i][0]<=globals()['AP{}'.format(j+1)][0]+radius) and \
                (STA_list[i][1]>=globals()['AP{}'.format(j+1)][1]-radius) and (STA_list[i][1]<=globals()['AP{}'.format(j+1)][1]+radius):
            print("현재 좌표: ", STA_list[i], "단말이 AP",j+1, "좌표 내에 있습니다.")

        else:
            print("현재 좌표: ", STA_list[i], "단말이 AP",j+1, "좌표 내에 있지 않습니다.")

print(X[0], Y[0])
# -------------------------------------------------------------------------------------------------------------------------------------------------------
from sympy import *
import scipy.integrate as integrate
import scipy.special as special
import time
import math
from math import *
from mpmath import *

accel=[]
gyroX=[]
magX=[]
magY=[]

t=4 #임의의 시간
#가속도 센서의 값 논문에서는 단순히 센서 값=>X값을 기준으로 작성
#가속도 센서, 회전 센서, 자기장 센서 초기값은 모두 0
for a in range(10): # 일단 5번 돌면서 랜덤 추출
    accel.append(random.uniform(0, 10))
# accel=[0.001, 6.125, 5.632, 6.69, 5.993, 6.618, 5.68]
#회전 센서값
for b in range(10): # 일단 5번 돌면서 랜덤 추출
    gyroX.append(random.uniform(-1, 1))
# gyroX=[0.001, 0.012, -0.118, 0.064, -0.505, -0.086, -0.533]

#자기장 센서값
for c in range(10): # 일단 5번 돌면서 랜덤 추출
    magX.append(random.uniform(-30, 1))
    magY.append(random.uniform(-1, 30))
# magX=[0.001, -30.341, -31.151, -31.86, -29.842, -17.612, -4.884]
# magY=[0.001, 4.182, 7.655, 7.199, 6.572, 7.802, 26.855]

print("가속도 센서값", accel)
print("회전 센서값", gyroX)
print("자기장 센서값", magX, magY)

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
    x=lambda x: k
    f = integrate.quad(x, t-1, t)
    print("속도: ", f)
    f=list(f)
    for s in f:
        #2차 적분 속도->이동거리
        #distance = integrate(exp(f), (f-0, t - 1, t))
        y = lambda y: s
        d = integrate.quad(y, t-1, t)
        d=list(d)
        dist.append(d[0])
    print("이동거리 : ", dist[0])
    distance.append(dist[0])
    t=t+1
"""    
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
"""
print("이동거리 결과 값 : ", distance)

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

bx=[X[0]]
by=[Y[0]]
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

