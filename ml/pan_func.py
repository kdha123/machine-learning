import pandas as pd
import seaborn as sns
from numpy import NAN, nan, NaN
# def double(x):
#     print('**')
#     return x*2

# def nth(x, n):
#     return x*n
#
# def selfprint(x):
#     print('**')
#     print(x)
#
# def hap(x):
#     h=0
#     for i in x:
#         h=h+i
#     return h
#
# def avg(x):
#     h=0
#     # print('x의 shape', x.shape)
#     for i in x:
#         h=h+i
#     return h/x.shape[0]
# df = pd.DataFrame({'a':[10,20,30,40,50], 'b':[100,200,300,400,500]})
# print(df)
# print(df.a.sum())
# apply()
# print(df['a'].apply(double))
# 두 개 이상의 매개변수를 넘길 때는 apply 안에 변수를 선언해줘야한다.
# print(df['a'].apply(nth,n=5))
# 데이터 프레임에 적용
# 1은 행방향
# df.apply(selfprint, axis=1)
# print(df.apply(hap))
# print(df.apply(avg))
# print(df.apply(avg, axis=1))
#


# 누락값의 갯수
def cnt_null(x):
    return x.shape[0]-x.count()

# 누락값의 비율
def rate_null(x):
    cnt = cnt_null(x)
    return cnt/x.shape[0]


titanic = sns.load_dataset("titanic")
# print(titanic.count())
# print(titanic.info())
print(titanic.apply(cnt_null))
titanic['null_rate'] = titanic.apply(rate_null, axis=1)
print(titanic)

# --------------
print("--"*30)
def cnt_null2(x):
    return x.shape[0] - x.count()

def rate_null2(x):
    cnt = cnt_null2(x)
    return cnt/x.shape[0]

df = pd.DataFrame({'a':[10,20,NAN,40,50], 'b':[100,200,300,NAN,NAN]})
# print(df)
# print(df.apply(cnt_null2))
print(df.apply(rate_null2, axis=1))
df['new'] = df.apply(rate_null2, axis=1)
print(df)