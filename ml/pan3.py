import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# fontname = font_manager.FontProperties(fname='malgun.ttf').get_name()
# rc('font', family=fontname)
#
d1 = pd.read_csv('data\\concat_1.csv')
# print(d1)
d2 = pd.read_csv('data\\concat_2.csv')
# print(d2)
d3 = pd.read_csv('data\\concat_3.csv')
# print(d3)
#
#
# print(data)
# data = pd.concat([d1,d2,d3])
# print(data.loc[1])
# print(data.iloc[1])
# data = pd.concat([d1,d2,d3], ignore_index=True)
# print(data)

# data = pd.concat([d1,d2,d3], axis=1)
# print(data)
# ------------------------
person = pd.read_csv('data\\survey_person.csv')
site = pd.read_csv('data\\survey_site.csv')
survey = pd.read_csv('data\\survey_survey.csv')
visited = pd.read_csv('data\\survey_visited.csv')
print(person)
ps = person.merge(survey, left_on='ident', right_on='person')
print(survey)
print(ps)
print(site)
print(visited)
sv = site.merge(visited, left_on='name', right_on='site')
print(sv)
