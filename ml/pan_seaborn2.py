# 요일별 교통사고 사상자 합계(사상자 3명이상인 데이터에 대해서)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

data = pd.read_csv('data\\accidentdata.csv')
# print(data.shape)
# d1 = data[data['사상자수'] >= 3]
# print(d1)
# s1 = d1.groupby('요일')['사상자수'].sum()
# print(s1)
# s1 = s1.reindex(['월','화','수','목','금','토','일'])
# plt.plot(s1)
# plt.title("요일별 교통사고 사상자 수")
# plt.show()
# 2. 경기도 내 교통사망사고가 높은 5지역 분석하여 그래프
d2 = data[data['발생지시도'] == '경기']
# print(d2)
s2 = d2.groupby('발생지시군구')['사망자수'].sum()
# print(s2)
# print(type(s2))
s2 = s2.sort_values(ascending=False)
print(s2)
s2 = s2.head()
print(s2)
plt.pie(s2, labels=['화성시','평택시','용인시','수원시','고양시'],
        colors=['red','brown','purple','orange','blue'],
        autopct='%.2f%%')
plt.title('2012-2014 경기도 교통사고 사망자수 top5')
plt.show()
