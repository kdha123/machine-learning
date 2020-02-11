import pandas as pd
# data=pd.read_csv('data/gap.tsv',sep='\t')
# # print(data)
# # print(type(data))   #데이터프레임
# # print(data.head())
# # print(data.tail(7))
# # print(data.shape)    #행과 열
# # print(data.shape[0]) #행의 수
# # print(data.shape[1]) #열의 수
# # print(data.columns)   #열이름
# # print(data.dtypes)   #자료형
# # print(data['country'].head(3))
# # print(data[['country', 'continent']].tail())
# # print(type(data['country']))   #1개의 열추출시 시리즈
# # print(type(data[['country', 'continent']]))  #2개이상의 열 추출시 데이터프레임
# # data1=data[['country', 'continent',  'year']]  #열단위 데이터 추출
# # print(data1)
# #행단위 데이터추출
# # loc:인덱스를 기준으로 행 데이터 추출
# # iloc:행번호를 기준으로 데이터 추출
# # https://grouplens.org/datasets/movielens/
# # baby=pd.read_csv('data\\baby\\yob1880.txt',header=None)
# # baby=pd.read_csv('data\\baby\\yob1880.txt',names=['name','sex','births'],
# #                  index_col='name')
# # print(baby)
# # print(baby.shape)
# # print(baby.iloc[2])
# # print(baby.iloc[100])
# # print(baby.iloc[[1,3,5,7,9]])
# # print(baby.iloc[[-1]])
# # print(baby.loc['Mary'])
# # print(baby.loc[['Mary','Margaret']])
# # baby=pd.read_csv('data\\baby\\yob1880.txt',names=['name','sex','births'])
# # print(baby)
# # print(baby.iloc[[1,3,5,7,9]])
# # print(baby.iloc[[-1]])
# # print(baby.loc[[1,3,5,7,9]])
# # # print(baby.loc[[-1]])
# # ----------
# data = pd.read_csv('data/gap.tsv', sep='\t')
# print(data.head())
# # print(data[['continent' , 'year']])
# # print(data.loc[[100,200]])
# # print(data.iloc[[100,200,-1]])
# # print(data.loc[[500,1000,1500],['country','year','lifeExp']])
# # # print(data.iloc[[500,1000,1500],['country','year','lifeExp']])  X
# # print(data.iloc[[500,1000,1500,-1],[0,2,3,-1]])
# # 슬라이싱을 활용한 데이터 추출
# # print(data.loc[:,['year','lifeExp']])
# # print(data[['year','lifeExp']])
# # print(data.iloc[:,[0,1,2,3]])
# # print(data.iloc[:,:4])
# print(data.head())
# # 연도별 수명계산
# print(data.groupby('year')['lifeExp'].mean())
#시리즈--------------------------
# s1=pd.Series(['banana',3000])
# print(s1)
# s2=pd.Series(['둘리','희동이','고길동'])
# print(s2)
# #데이터프레임-------------------------
# d1=pd.DataFrame({'이름':['둘리','희동이','고길동'],
#                  '나이':[7,2,40],
#                  '생일':['2014-01-01','2019-12-30','1980-01-30']})
# print(d1)
# 시리즈의 메서드---
data=pd.read_csv('data/gap.tsv',sep='\t')
s1=data['year']
# print(s1)
# print(type(s1))
# print(s1.min())
# print(s1.mean())
# print(s1.sum())
# print(s1.max())
# 불린추출
# d1=data[data['country']=='Afghanistan']
# print(d1)
# test=[False,False,False,False,False,True,False,False,False,True,False,False]
# print(d1[test])
# print(d1['pop'] % 2==0)
# print(d1[d1['pop'] % 2==0])
# #d1에서 gdpPercap의 평균보다 큰 행만 출력
# print(d1['gdpPercap'].mean())  #802.6745984249998
# print(d1['gdpPercap']>d1['gdpPercap'].mean())
# print(d1[d1['gdpPercap']>d1['gdpPercap'].mean()])
baby=pd.read_csv('data\\baby\\yob1880.txt',header=None,
                 names=['name','sex','births'])
#남자아기들만 위에서 20명출력
# print(baby['sex']=='M')
# print(baby[baby['sex']=='M'].head(20))
# 여자아기중 출생아수가 10명 미만인 것들만 출력 &:and ,|:or
# print((baby['sex']=='F') & (baby['births']<10 ))
# print(baby[(baby['sex']=='F') & (baby['births']<10 )])
#출생아수의 평균보다 작은 이름을 가진 남자아기 출력
print(baby['births'].mean())   #100.743
print(baby['births']<baby['births'].mean())
print((baby['births']<baby['births'].mean()) & (baby['sex']=='M'))
print(baby[(baby['births']<baby['births'].mean()) & (baby['sex']=='M')])