import pandas as pd
from numpy import NaN, nan, NAN
# 1번------------------------
data = pd.read_csv('data\\alcol.csv', sep=',')
data = data['State'].head(5)
print(data, type(data))

# 2번---------------------
data = pd.read_csv('data\\alcol.csv', sep=',')
print(data)
data_wine = data.pivot_table(index='Year', columns='State', values='Wine')
print(data_wine)

# 3번-----------------------------
data2009 = data[data['Year'] == 2009]
print(data2009)

# 4번-----------------------------
data2009 = data2009.drop('Year', axis=1)
data2009 = data2009.reset_index()
print(data2009)

# 5번----------------------------
print(data2009['State'].isna())
print(data2009['Beer'].isna())
print(data2009['Wine'].isna())
print(data2009['Spirits'].isna())
data2009 = data2009.fillna(0)
print(data2009)

# 6번-----------------------------
data2009['total'] = data2009['Beer']+data2009['Wine']+data2009['Spirits']
print(data2009)

# 7번--------------------------
usa = pd.read_csv('data\\usa.csv',sep=',')
usa['country'] = '미국'
print(usa, type(usa))

# 8번-----------------------
df = pd.concat([usa,data2009], axis=1).set_index('State')
print(df)

# 9번------------------------
canada = pd.read_csv('data\\canada.csv',sep=',')
canada['country'] = '캐나다'
print(canada, type(canada))

# 10번-----------------------
pop = pd.concat([usa,canada], ignore_index=True).set_index(['country', 'State'])
print(pop.sort_index())