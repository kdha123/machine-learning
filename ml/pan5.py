import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
rc('font', family=fontname)

tips = sns.load_dataset('tips')
# print(tips)
tips2 = tips.head(10)
# print(tips2)

# 1, 3, 5, 7, 9행의 total_bill만 출력
# print(tips2.loc[[1,3,5,7,9],'total_bill'])
tips2.loc[[1,3,5,7,9],'total_bill']='notvalue'
# print(tips2)
# print(tips2.info())
# tips2['total_bill']=tips2['total_bill'].astype(float)
# 잘못입력된 문자열처리(to_numeric)
# tips2['total_bill'] = pd.to_numeric(tips2['total_bill'])
# tips2['total_bill'] = pd.to_numeric(tips2['total_bill'], errors='ignore')
# tips2['total_bill'] = pd.to_numeric(tips2['total_bill'], errors='coerce')
tips2['total_bill'] = pd.to_numeric(tips2['total_bill'], errors='coerce', downcast='float')
# print(tips2.info())
# print(tips2)
# print(tips.info())
tips['sex'] = tips['sex'].astype(str)
print(tips.info())
