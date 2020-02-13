import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
fontname=font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font',family=fontname)

# --------
data=pd.read_csv('data\\accidentdata.csv')
print(data)

# 1.요일별 교통사고 사상자 합계(사상자 3명이상인 데이터에 대해)
# d1=data[data['사상자수']>=3]
# print(d1.shape)
# s1=d1.groupby('요일')['사상자수'].sum()
# print(s1)
# s1=s1.reindex(['월','화','수','목','금','토','일'])
# print(s1)
# plt.plot(s1)
# plt.title('2012-2014 요일별 교통사고 사상자수')
# plt.show()
# 2. 경기도내 교통사망사고가 높은 5지역 분석하여 그래프
# d2=data[data['발생지시도']=='경기']
# # print(d2.shape)
# s2=d2.groupby('발생지시군구')['사망자수'].sum()
# # print(s2)
# # print(type(s2))
# s2=s2.sort_values(ascending=False)
# # print(s2)
# s2=s2.head()
# print(s2)
# plt.pie(s2,labels=['화성시','평택시','용인시','수원시','고양시'],
#         colors=['red','brown','purple','orange','green'],
#         autopct='%.2f%%')
# plt.title('2012-2014 경기도 교통사고 사망자수 top5')
# plt.show()
# -----------------------------------------------
# --3. 요일별/ 발생지시도별 교통사고 분석
print(data.info())
p1 = data.pivot_table(index='요일', columns='발생지시도', values='사망자수', aggfunc='sum')
print(p1)
p1 = p1.reindex(['월','화','수','목','금','토','일'])
plt.plot(p1)
plt.title('요일별/ 발생지시도별 사망자수')
plt.legend(p1.columns)
plt.show()

