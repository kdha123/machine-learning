import pandas as pd
from numpy import NaN, nan, NAN
import seaborn as sns

# print(NaN==True)
# print(NaN==False)
# print(NaN==0)
# print(NaN=='')
# print(pd.isnull(nan))
# print(pd.isnull(NaN))
# print(pd.notnull(NAN))
# print(pd.notnull(3))

ebola = pd.read_csv('data\\timeseries.csv')
# print(ebola)

# 누락값 처리(fillna(), interpolate())

d1 = ebola.iloc[:10,:5]
# print(d1.fillna(0))
# print(d1.fillna(method='ffill'))
# print(d1.fillna(method='bfill'))
# print(d1.interpolate())
# 누락값의 처리(삭제)
# print(d1.dropna())
d1['total'] = d1['Cases_Guinea']+d1['Cases_Liberia']+d1['Cases_SierraLeone']
d1['total'] = d1['Cases_Guinea'].fillna(0)+d1.Cases_Liberia.fillna(0)+d1['Cases_SierraLeone'].fillna(0)
# print(d1)
# print(d1['Cases_Liberia'].sum())
# print(d1['Cases_Liberia'].sum(skipna=False))
# print(d1.Cases_Liberia.sum(skipna=False))

# 피벗 ------------
data = {
    "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천" ],
    "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010" ],
    "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 2632035],
    "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
}
df = pd.DataFrame(data)
# print(df)
# pivot(행인덱스, 열인덱스, 데이터)
# print(df.pivot(index='도시',columns='연도',values='인구'))

# pivot_table(행인덱스, 열인덱스, 데이터)
# p1 = df.pivot_table(index='도시',columns='연도',values='인구')
# print(p1)
# print(p1.index)
# print(p1.columns)
# print(p1.reset_index())
# p2 = p1.reset_index()
# print(p2)
# print(p2.index)
# print(p2.columns)
data = pd.read_excel('data\\판매현황.xlsx')
# print(data)
# print(data.pivot_table(index='분류', values='금액'))
# print(data.pivot_table(index='분류', values='금액', aggfunc='sum'))
# print(data.pivot_table(index=['분류','상품코드','상품명'], values='금액', aggfunc='sum'))
# print(data.pivot(index='분류', values='금액')) X

# -melt(id_vars: 위치를 유지할 열이름, var_name: 위치를 변경한 열의 이름, value_name: 위치를 변경한 데이터의 열이름)
pew = pd.read_csv('data\\pew.csv')
# print(pew)
# print(pew.shape)
d1 = pew.iloc[:6,:4]
# print(d1.melt(id_vars='religion', var_name='income', value_name='inwon'))
# print(ebola)
# print(ebola.columns)
# ebola2 = ebola.melt(id_vars=['Date','Day'])
# print(ebola2.variable)
# print('-'*30)
# print(ebola2.variable[0])
# print(ebola2.variable[0].split('_'))
# print(ebola2.variable[1947].split('_')[1])
# 문자열 처리시 str접근자 사용, 날짜형 처리시 datetype 접근자를 사용한다.
# ebola3 = ebola2.variable.str.split('_')
# print(ebola3)
# print(ebola3.str.get(1))
# ebola2['status'] = ebola3.str.get(0)
# ebola2['country'] = ebola3.str.get(1)
# print(ebola2)
# ebola2['new'] = ebola2['status']+ebola2['country']
# print(ebola2)
# --------------------------
# print(ebola.info())
# print(ebola.head())
# ebola['Date'] = pd.to_datetime(ebola['Date'])
# print(ebola.info())
# print(ebola.head())
# print(ebola['Date'][0])
# print(ebola['Date'][0].year)
# print(ebola['Date'][0].month)
# print(ebola['Date'][0].day)
# ebola['year'] = ebola['Date'].dt.year
# ebola['month'] = ebola['Date'].dt.month
# ebola['day'] = ebola['Date'].dt.day
# print(ebola)
tips = sns.load_dataset('tips')
print(tips)
print(tips.info())
tips['sex'] = tips['sex'].astype(str)
tips['total_bill'] = tips['total_bill'].astype(str)
print(tips.info())