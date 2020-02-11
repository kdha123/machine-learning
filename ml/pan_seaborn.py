import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)
# data = sns.load_dataset('anscombe')
# # print(data)
# # # d1에 dataset이 I인것만 추출
# # d1 = data[data['dataset'] == 'I']
# # # d1에 dataset이 II인것만 추출
# # d2 = data[data['dataset'] == 'II']
# # # d1에 dataset이 III인것만 추출
# # d3 = data[data['dataset'] == 'III']
# # # d1에 dataset이 IV인것만 추출
# # d4 = data[data['dataset'] == 'IV']
# # fig = plt.figure()
# # area1 = fig.add_subplot(2,2,1)
# # area2 = fig.add_subplot(2,2,2)
# # area3 = fig.add_subplot(2,2,3)
# # area4 = fig.add_subplot(2,2,4)
# #
# # area1.plot(d1['x'],d1['y'], 'rs')
# # area2.plot(d2['x'],d2['y'], 'o--')
# # area3.plot(d3['x'],d3['y'], 'o-')
# # area4.plot(d4['x'],d4['y'], 'o')
# #
# # area1.set_title('영역1')
# # area2.set_title('영역2')
# # area3.set_title('영역3')
# # area4.set_title('영역4')
# #
# # fig.tight_layout()
# # plt.show()
# ----------------------
tips = sns.load_dataset('tips')
# print(tips)
# # 1)
# fig = plt.figure()
# # area1 = fig.add_subplot(1,1,1)
# area1 = fig.add_subplot(111)
# area1.scatter(tips['total_bill'],tips['tip']) # 산점도(x 축, y축)
# area1.set_title('식비와 팁과의 산점도')
# area1.set_xlabel('식비')
# area1.set_ylabel('팁')
# 2)
# plt.scatter(tips['total_bill'],tips['tip'])
# plt.title('식비와 팁과의 산점도')
# plt.xlabel('식비')
# plt.ylabel('팁')
# plt.show()

# 3)
# plt.scatter(tips['total_bill'],tips['tip'], s=tips['size']*10)
# plt.title('식비와 팁과의 산점도')
# plt.xlabel('식비')
# plt.ylabel('팁')
# plt.show()

# 4)
# def sex_to_int(sex):
#     if sex == 'Female':
#         return 0
#     else:
#         return 1
# tips['sex2'] = tips['sex'].apply(sex_to_int)
# print(tips)
# plt.scatter(tips['total_bill'],tips['tip'], s=tips['size']*15, c=tips['sex2'], alpha=0.5)
# plt.title('식비와 팁과의 산점도')
# plt.xlabel('식비')
# plt.ylabel('팁')
# plt.show()
# ------------
# plt.hist(tips['total_bill'])
# plt.show()
# ------------boxplot
# plt.boxplot(tips['total_bill'])
# plt.show()
# 여자가 계산한 식대를 그래프로
# print(tips['sex'] == 'Female')
# print(tips[tips['sex'] == 'Female']['total_bill'])
# print(tips[)
# plt.boxplot)
# plt.show()
# 여자, 남자가 계산한 식대를 그래프로
# plt.boxplot([tips[tips['sex'] == 'Female'].total_bill, tips[tips['sex'] == 'Male'].total_bill], labels=['여','남'])
# plt.show()
# 요일별 교통사고 사상자 합계(사상자 3명이상인 데이터에 대해서)