from array import *
import math

#임의의 고정 AP 4개의 좌표
wifiNum=4
ap1=[1,1,0]
ap2=[100,5,0]
ap3=[0,90,0]
ap4=[90,100,-15]

APPoint=[ap1, ap2, ap3, ap4]
a=[]
#A행렬
i=0
for i in range(wifiNum):
    j=0
    for j in range(3):
        a=2*(APPoint[i][j]-APPoint[wifiNum-1][j])
        j=j+1
    i=i+1

print(a)

#실제 거리 행렬 입력
distance1=0
distance2=0
distance3=0
distance4=0

#각 노드와 현재 위치까지의 거리를 배열에 저장
#실제 측위로 현재 위치 계산하는 distance 행렬
distance=[[distance1],[distance2],[distance3],[distance4]]

#B행렬
b=[]
i=0
for i in range(wifiNum):
    j=0
    for j in range(1):
        b=(
            (math.pow(APPoint[i][0],2) - math.pow(APPoint[wifiNum-1][0],2))
            +(math.pow(APPoint[i][1],2) + math.pow(APPoint[wifiNum-1][1],2))
            +(math.pow(APPoint[i][2], 2) + math.pow(APPoint[wifiNum - 1][2], 2))
            +(math.pow(distance[i][j], 2) + math.pow(distance[wifiNum - 1][j], 2))
        )
        j=j+1
    i=i+1

print(b)