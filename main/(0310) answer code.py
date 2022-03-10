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


# 시각화
figure, axes = plt.subplots()
x_values = list()
y_values = list()

for i in range(len(STA_list)):
    x_values.append(STA_list[i][0])
    y_values.append(STA_list[i][1])
#print(x_values)
plt.xlim([0,10])
plt.ylim([0,10])
plt.plot(x_values, y_values, 'bo', label='STA', markersize = 4, color='gray')
color=list()
color_list = list()

color = ['r', 'g', 'b']
# color = random.sample(['r', 'g', 'b'], AP_num)

for r in range(AP_num):
    globals()['draw_circle{}'.format(r + 1)] = mpatches.Circle((globals()['AP{}'.format(r+1)][0], globals()['AP{}'.format(r+1)][1]), radius, color=color[r], fill=False, label=['AP{}'.format(r+1)])
    axes.legend([globals()['draw_circle{}'.format(r + 1)]], ['Stress State'])
    axes.add_patch(globals()['draw_circle{}'.format(r + 1)])

axes.set_aspect('equal')

plt.legend()
plt.show()