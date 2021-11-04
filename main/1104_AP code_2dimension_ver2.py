# STA 이동하는 버전
'''
좌표 x,y 2차원으로 수정한 버전
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import matplotlib.patches as mpatches

AP_num = 2  # AP의 개수
range_list = list()

# 반지름
radius = random.randrange(5, 15)
print("반지름: ", radius)

# AP1의 좌표
AP1 = [random.randrange(10, 40), random.randrange(10, 40)]

# AP 1을 기점으로 이후 AP들 좌표 범위 설정(최소 1개 이상의 AP가 존재한다는 가정)
for i in range(1,AP_num+1):
    globals()['AP{}'.format(i+1)] = [random.randrange(10, 40), random.randrange(10, 40)]
    # print(globals()['AP{}'.format(i)])
for i in range(AP_num):
    for j in range(3):
        globals()['AP_range{}'.format(i + 1)] = [globals()['AP{}'.format(i + 1)][0] + radius, globals()['AP{}'.format(i + 1)][1] + radius]

# 중점 출력용
for i in range(AP_num):
     print("AP",i+1,"의 중점: ", globals()['AP{}'.format(i+1)])


# STA의 위치 설정
STA = list()
STA_list = list()
STA = [random.randrange(0, 40), random.randrange(0, 40)]

STA_list.append(STA)
for i in range(20):
    STA2 = [STA[0] + i + 1, STA[1] + i + 1]
    if (STA[0] + i + 1 > 50) or (STA[1] + i + 1 > 50):
        break
    STA_list.append(STA2)
print("단말 STA의 좌표: ", STA_list)

# 각 Phase의 좌표가 각 AP에 속하는지 판단
for i in range(10):
    for j in range(AP_num):
        if(STA_list[i][0]>=globals()['AP{}'.format(j+1)][0]-radius) and (STA_list[i][0]<=globals()['AP{}'.format(j+1)][0]+radius) and (STA_list[i][1]>=globals()['AP{}'.format(j+1)][1]-radius) and (STA_list[i][1]<=globals()['AP{}'.format(j+1)][1]+radius):
            print("Phase",i,". 단말이 AP",j+1, "좌표 내에 있습니다.")

        else:
            print("Phase",i,". 단말이 AP",j+1, "좌표 내에 속하지 않습니다.")


figure, axes = plt.subplots()
x_values = list()
y_values = list()

for i in range(len(STA_list)):
    x_values.append(STA_list[i][0])
    y_values.append(STA_list[i][1])
#print(x_values)
plt.xlim([0,50])
plt.ylim([0,50])
plt.plot(x_values, y_values, 'bo', label='STA', markersize = 3, color='blue')
color=list()
color_list = list()

color = random.sample(['r', 'g', 'b', 'y', 'm', 'k', 'c'], AP_num)

for r in range(AP_num):
    globals()['draw_circle{}'.format(r + 1)] = mpatches.Circle((globals()['AP{}'.format(r+1)][0], globals()['AP{}'.format(r+1)][1]), radius, color=color[r], fill=False, label=['AP{}'.format(r+1)])
    axes.legend([globals()['draw_circle{}'.format(r + 1)]], ['Stress State'])
    axes.add_patch(globals()['draw_circle{}'.format(r + 1)])

axes.set_aspect('equal')
# axes.set_xlabel('ih')
# axes.set_ylabel('id')

plt.legend()
plt.show()