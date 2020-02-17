import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
fontname=font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font',family=fontname)
tips=sns.load_dataset('tips')
# print(tips)
# tips2=tips.head(10)
# print(tips2)
# # 1,3,5,7,9행의 total_bill 출력
# # print(tips2.loc[[1,3,5,7,9],'total_bill'])
# tips2.loc[[1,3,5,7,9],'total_bill']='notvalue'
# # print(tips2)
# # print(tips2.info())
# # tips2['total_bill']=tips2['total_bill'].astype(float)
# # 잘못입력된 문자열처리(to_numeric)
# # tips2['total_bill']=pd.to_numeric(tips2['total_bill'])
# # tips2['total_bill']=pd.to_numeric(tips2['total_bill'],errors='ignore')
# # print(tips2.info())
# # print(tips2)
# # tips2['total_bill']=pd.to_numeric(tips2['total_bill'],errors='coerce')
# # print(tips2.info())
# # print(tips2)
# # tips2['total_bill']=pd.to_numeric(tips2['total_bill'],errors='coerce',
# #                                   downcast='float')
# # print(tips2.info())
# # print(tips2)
# print(tips.info())
# tips['sex']=tips['sex'].astype(str)
# print(tips.info())
# ---함수
# def double(x):
#     return 2*x
# def nth(x,n):
#     return x*n
# def selfprint(x):
#     print('**')
#     print(type(x))
#     print(x)
# def hap(x):
#     h=0
#     for i in x:
#        h=h+i
#     return h
# def avg(x):
#     h=0
#     # print('x의 shape',x.shape)
#     for i in x:
#        h=h+i
#     return h/x.shape[0]
# df=pd.DataFrame({'a':[10,20,30,40,50],
#                  'b':[100,200,300,400,500]})
# print(df)
# # print(df.a.sum())
# # apply(함수명)
# # print(df['a'].apply(double))
# # print(df['a'].apply(nth,n=5))
# # 데이터 프레임에 적용
# # df.apply(selfprint)
# # df.apply(selfprint,axis=1)  #행방향
# # print(df.apply(hap))
# print(df.apply(avg))
# print(df.apply(avg,axis=1))
#누락값의 갯수
def cnt_null(x):
    # print(x.shape)  #(891,)
    return x.shape[0]-x.count()
# 누락값의 비율
def rate_null(x):
    cnt=cnt_null(x)
    return cnt/x.shape[0]
titanic=sns.load_dataset("titanic")
# print(titanic)
print(titanic.info())
# print(titanic.apply(cnt_null))
print(titanic.apply(rate_null))
titanic['null_rate']=titanic.apply(rate_null,axis=1)
print(titanic)

# ---------
# from numpy import NAN
# # def double(x):
# #     print('**')
# #     return 2*x
# #
# print('-'*30)
# def cnt_null2(x):
#     # print(x.shape,x.count())
#     return x.shape[0]-x.count()
# def rate_null2(x):
#     cnt=cnt_null2(x)
#     return cnt/x.shape[0]
# df=pd.DataFrame({'a':[10,20,NAN,40,50],
#                  'b':[100,200,300,NAN,NAN]})
# print(df)
# # print(df['a'].apply(double))
# # print(df.apply(cnt_null2))
# print(df.apply(rate_null2))
# print(df.apply(rate_null2,axis=1))
# df['new']=df.apply(rate_null2,axis=1)
# print(df)








