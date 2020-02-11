import pandas as pd
data = pd.read_csv("data\\gap.tsv", sep="\t")
# print(data)
# print(data.head())
# print(data.shape)
# print(data['country'] == "Afghanistan") # boolean 추출
# print(data[data['country'] == "Afghanistan"])
d1 = data[data['country'] == "Afghanistan"]
# 브로드캐스팅 : 데이터 프레임 또는 시리즈의 모든 데이터에 대해 한꺼번에 연산
# print(d1['lifeExp']+d1['lifeExp'])
# print(d1['lifeExp']+100)
s1 = pd.Series([100,200,300])
# print(s1)
# print(d1['lifeExp']+s1) # 길이가 다른 벡터 연산
# ----------------------------------
# print(d1.sort_values(by='gdpPercap'))
# print(d1.sort_values(by='pop', ascending=False))
d1 = d1.set_index('year')
# print(d1)
# print(d1.shape)
print(d1.sort_index(ascending=False))
# ---set_index(), reset_index(), re_index()
d1 = d1.set_index('pop') # 기존 인덱스 삭제, 지정된 컬럼을 인덱스 지정
print(d1)
d1 = d1.reset_index() # 기존 인덱스가 열이되고 일련번호 생성
print(d1)
d1 = d1.reindex([0,1,10,11,2,3,4,5,6,7,8,9]) # 인덱스 순서가 변경된다.
print(d1)
# 열의 추가, 열삭제
d1['total'] = d1['lifeExp']+d1['gdpPercap']
print(d1)
d1 = d1.drop('total', axis=1) # axis=0 행방향삭제
print(d1)
d1 = d1.drop(['lifeExp','gdpPercap'], axis=1)
print(d1)
# d1.to_csv('data\\d1.csv')
# d1.to_csv('data\\d1.csv', index=False)
# d1.to_csv('data\\d1.csv', index=False, header=False, sep=';')
# d1.to_clipboard()
# d1.to_json('data\\d1.json')
# d1.to_excel('data\\dq.xlsx', index=False)
d1.to_pickle('data\\d1.pickle')
d2 = pd.read_pickle('data\\d1.pickle')
print(d2)