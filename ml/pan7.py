import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
from matplotlib import font_manager,rc
fontname=font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font',family=fontname)

# d1 = json.load(open("data\\foods.json", 'r'))
# print(type(d1))
# print(len(d1))
# print(d1[0])
# print(d1[0].keys())
# print(d1[0]['nutrients'])
# nutrients = pd.DataFrame(d1[0]['nutrients'])
# print(nutrients)
# col = ["id","description","manufacturer","group"]
# data = pd.DataFrame(d1, columns=col)
# print(data)
# temp = []
# for i in d1:
#     n = pd.DataFrame(i['nutrients'])
#     n['id'] = i['id']
#     temp.append(n)
# nutrients = pd.concat(temp, ignore_index=True)
# print(nutrients)
# print(nutrients.shape)
# nutrients = nutrients.drop_duplicates()
# print(nutrients.shape)
# print(nutrients.columns)
# 컬럼명 변경
# col = ["id","description","manufacturer","group"]
# 1) 컬럼명 전체 변경
# data = ["id","food","manufacturer","fgroup"]
# print(data)

# 2) 컬럼명 부분변경
# data = data.rename(columns={"description":"food","group":"fgroup"})
# print(data)
# print(data.columns)
# print(nutrients.columns)
# df = data.merge(nutrients, on='id')
# print(df.info)

# --------중복 데이터
# data = {'key1':['a', 'b', 'b', 'c', 'c'],
#     'key2':['v', 'w', 'w', 'x', 'y'],
#     'col':[1, 3, 3, 4, 5]}
# df = pd.DataFrame(data)
# print(df)
# print(df.duplicated('key1'))
# print(df.duplicated(['key1','key2']))
# print(df.drop_duplicates(['key1'], keep='first'))
# print(df.drop_duplicates(['key1'], keep='last'))
# print(df.drop_duplicates())

# -------- 네이버개발자센터에서 "파이썬이랑 단어로 책을 검색하여 나온 json 문서를
# 데이터 프레임으로 변환
# 책제목, 출판사, 가격, 출간일
# import urllib.request
# client_id = "9eYRtkGNmEzbrUhDYxym"
# client_secret = "QFU3tG14u2"
# encText = urllib.parse.quote("파이썬")
# url = "https://openapi.naver.com/v1/search/book.json?display=100&query=" + encText # json 결과
#
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     result = response_body.decode('utf-8')
# else:
#     print("Error Code:" + rescode)
# tojson = json.loads(result)
# # print(tojson)
# col = ['title', 'publisher','price','pubdate']
# df = pd.DataFrame(tojson['items'], columns=col)
# print(df)
# df.to_csv('data\\book.csv', index=False)

# --------------------
from datetime import datetime
# t1 = datetime.now()
# t2 = datetime(1995, 12, 18)
# print(t2)
# print(t1-t2)

# ebola = pd.read_csv('data\\timeseries.csv')
# print(ebola.info())
# ebola['Date'] = pd.to_datetime(ebola['Date'])
# print(ebola.info())
# ebola = pd.read_csv('data\\timeseries.csv', parse_dates=[0])
# print(ebola.info())
# ebola['yy'] = ebola['Date'].dt.year
# ebola['mm'] = ebola['Date'].dt.month
# ebola['dd'] = ebola['Date'].dt.day
# print(ebola)
# 에볼라 최소 발생일
# print()
# ebola['new'] = ebola['Date'] - ebola['Date'].min()
# print(ebola)
bank = pd.read_csv('data\\bank.csv', parse_dates=['Closing Date','Updated Date'])

# 연도별 파산한 은행수 그래프
# 파산한 연도 컬럼 추가
bank['year'] = bank['Closing Date'].dt.year
bank['quarter'] = bank['Closing Date'].dt.quarter # 파산한 분기
# print(bank)
# print(bank.info())
# closingyear = bank.groupby('year').size()
# print(closingyear)
# plt.plot(closingyear)
# plt.bar(closingyear.index, closingyear.values)
# plt.title('년도별 파산한 은행수')
# plt.xticks(range(2000,2018))
# plt.show()
# -- 연도별 분기별 파산한 은행수 그래프
closingyq = bank.groupby(['year','quarter']).size()
# plt.plot(closingyq)
# plt.show()
closingyq = closingyq.reset_index()
# print(closingyq)
# print(closingyq.info())
closingyq['yq']= closingyq['year'].astype(str)+'-'+closingyq['quarter'].astype(str)
# print(closingyq)
closingyq= closingyq.set_index('yq')
print(closingyq)
plt.plot(closingyq.index, closingyq[0])
plt.show()