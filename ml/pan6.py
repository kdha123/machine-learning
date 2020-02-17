import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
fontname=font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font',family=fontname)
tips=sns.load_dataset("tips")
# print(tips)
# tips10=tips.head(10)
# tips10=tips.sample(10,random_state=42)
# print(tips10)
# g1=tips10.groupby('sex')
# print(g1) #그룹객체
# # 그룹객체의 속성 groups,
# # 그룹객체의 메서드 get_group
# print(g1.groups)
# avg=g1.mean()
# print(avg)
# male=g1.get_group('Male')
# female=g1.get_group('Female')
# print(female)
# print(type(female))    #dataframe
# print(female.index)
# print(female.columns)
# -----------
# g2=tips10.groupby(['sex','time'])    #그룹객체
# print(g2.mean())
# print(type(g2)) #그룹객체
# print(type(g2.mean())) #데이터프레임
# # print(g2.index)
# # print(g2.columns)
# df2=g2.mean()
# print(df2.index)
# print(df2.columns)
# 현재 인덱스를 일반컬럼으로 변경
# 1)reset_index()
# df2=df2.reset_index()
# print(df2)
# 2)set_index()
# df3=df2.set_index('tip')
# print(df3)
# ---------------------
gap=pd.read_csv('data\\gap.tsv',sep='\t')
print(gap.head())
# 연도별로 수명의 평균을 출력
# print(gap.groupby('year').lifeExp.mean())
# 그룹객체와 agg메서드,apply메서드
def avg(x):
    # print('*',x,'[',len(x),']')
    hap=0
    for i in x:
        hap=hap+i
    return hap/len(x)
# print(gap.groupby('year').lifeExp.agg(avg))
# print(gap.groupby('year').lifeExp.apply(avg))
globalavg=gap.lifeExp.mean()
# print(globalavg)
def avg2(x,globalavg):
    hap=0
    for i in x:
        hap=hap+i
    return globalavg-hap/len(x)
# print(gap.groupby('year').lifeExp.agg(avg2,globalavg=globalavg))
# agg:여러개 집계 메서드를 한번에 사용
# print(gap.groupby('year').agg({'lifeExp':'mean','pop':'median','gdpPercap':'max'}))
# apply 와 agg
# def f1(x):
#     return 1
# iris=pd.read_csv('data\\iris3.csv',sep=' ')
# print(iris.head())
# g=iris.groupby('Species')
# print('='*30)
# print(g.apply(f1))
# print('&'*30)
# print(g.agg(f1))
# 람다-------------------
# def ff1(x):
#     return x*2
#
# lambda x:x*2
def hap(x):
    return x.sum()
# df = pd.DataFrame({"name":["Foo", "Baar", "Foo", "Baar"],
#                    "score_1":[5,10,15,10],
#                    "score_2" :[10,15,10,25],
#                    "score_3" : [10,20,30,40]})
# print(df)
# # print(df.groupby(['name','score_1']).score_2.apply(hap))
# print(df.groupby(['name','score_1']).score_2.apply(lambda x:x.sum()))
# print(df.groupby(['name','score_1']).agg({'score_2':lambda x:x.sum(),
#                                           'score_3':lambda x:x.mean()}))
#-식사대비 팁의 비율---
print(tips.head())
tips['tip_rate']=tips['tip']/tips['total_bill']
print(tips)
# 성별, 흡연여부에 따른 팁비율의 평균
# print(tips.groupby(['sex', 'smoker']).tip_rate.agg('mean'))
# 요일별 평균
import numpy as np
# print(tips.groupby('day').mean())
# print(tips.groupby('day').apply(np.mean))
# print('-'*30)
# print(tips.groupby('day').transform(np.mean))
# print('\n\n\n\n\n')

# tips10 = tips.head(10)
# print(tips10)
# tips10.loc[[1,3,7],'total_bill']=np.NAN
# print(tips10)
# print(tips10['total_bill'].mean())   #18.067
# print(tips10['total_bill'].fillna(0))
# def f3(x):
#     avg=x.mean()
#     return x.fillna(avg)
# print(tips10.groupby('sex').total_bill.transform(f3))  #성별의 평균
# print(tips10.total_bill.transform(f3))  #평균
# -----------------------
ebola=pd.read_csv('data\\timeseries.csv')
# print(ebola)
# print(list(range(5)))
# # print(pd.date_range(start='2020-02-14',end='2020-04-30'))
# print(pd.date_range(start='2020-02-14',end='2020-04-30',freq='w'))
# print(pd.date_range(start='2020-02-14',end='2020-04-30',freq='B'))
# d1=ebola.head()
# print(d1)
# print(d1.info())
# d1['Date']=pd.to_datetime(d1['Date'])
# d1=d1.set_index('Date')
# print(d1)
# d1=d1.reindex(pd.date_range(start='2014-12-31',end='2015-01-05'))
# print(d1)
# d2의 날짜가 빠짐 없도록 하세요
d2=ebola.tail(10)
d2['Date']=pd.to_datetime(d2['Date'])
d2=d2.set_index(('Date'))
print(d2)
d2=d2.reindex(pd.date_range(start='2014-03-22',end='2014-04-04'))
print(d2)
d2=d2.reset_index()
print(d2)