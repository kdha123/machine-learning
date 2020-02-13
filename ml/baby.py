import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)
# baby = pd.read_csv('data\\baby\\yob1880.txt',
#                    names=['name', 'sex', 'birth'])
# print(baby)
# yobxxxx.txt
temp = []
for year in range(1880,2011):
    filename = 'data\\baby\\yob{}.txt'.format(year)
    # print(filename)
    df = pd.read_csv(filename, names=['name', 'sex', 'birth'])
    df['year'] = year
    temp.append(df)
data = pd.concat(temp, ignore_index=True)
print(data)
# print(data[data['name']=='Mary'])
total_births = data.pivot_table(index="year", columns='sex', values='birth', aggfunc='sum')
print(total_births)
plt.title('연도별 신생아 성별비율')
plt.plot(total_births)
plt.legend(['여자','남자'])
plt.show()
