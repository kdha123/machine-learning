import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

# 1번-------------------
report = pd.read_csv('data\\report.csv',sep=',')
print(report.head(10), type(report))
print(report.tail(10))

# 2번------------------
fig = plt.figure()
plt.scatter(report[report['State']=='New Hampshire'].Beer,report[report['State']=='New Hampshire'].Wine)
plt.show()
plt.close()

# 3번--------------------
report = report.pivot_table(index='Year', columns='State', values='Beer')
print(report)
beer_report = report[['New Hampshire','Colorado','Utah']]
plt.title('주별 맥주 소비량의 변화')
plt.plot(beer_report)
plt.xlabel('년도')
plt.ylabel('맥주소비량')
plt.legend(['New Hampshire','Colorado','Utah'])
plt.show()
plt.close()



# 4번-------------------
tips = sns.load_dataset('tips')
print(type(tips))
dinner = tips[tips['time'] == 'Dinner'].total_bill
lunch = tips[tips['time'] == 'Lunch'].total_bill
print(dinner.min())
print(dinner.min())
print(dinner.median())
print(dinner.min())
print(lunch.min())
print(lunch.min())
print(lunch.min())
print(lunch.min())
data = [dinner, lunch]
plt.boxplot(data, labels=['아침','저녁'])
plt.show()
plt.close()
# 5번-------------------
tips = tips.pivot_table(index='size', columns='day', values='total_bill', aggfunc='sum')
print(tips)

# 6번---------------------
plt.title("식사 비용 현황")
plt.plot(tips)
plt.legend(['목','금','토','일'])
plt.xlabel('좌석수')
plt.ylabel('식사비용')
plt.show()
plt.close()

# 7번-----------------------
bank = pd.read_csv('data\\bank.csv', parse_dates=['Closing Date','Updated Date'])
print(bank.info())

# 8번-----------------------
bank['year'] = bank['Closing Date'].dt.year
bank['quarter'] = bank['Closing Date'].dt.quarter # 파산한 분기
closingyear = bank.groupby('year').size()
print(closingyear)
plt.plot(closingyear)
plt.bar(closingyear.index, closingyear.values)
plt.title('년도별 파산한 은행수')
plt.xticks(range(2000,2018))
plt.show()
plt.close()