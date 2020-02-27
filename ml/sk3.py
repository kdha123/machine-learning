import glob
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
def makedata(f):
    with open(f, encoding='utf-8') as f:
        text=f.read()
        text=text.lower()
        code_a=ord('a')
        code_z=ord('z')
        cnt=[0 for n in range(26)]
        # print(cnt)
        for c in text:
            if code_a<= ord(c) <=code_z:
                cnt[ord(c)-code_a]=cnt[ord(c)-code_a]+1
        # print(cnt)
        total=sum(cnt)
        rate=list(map(lambda x:x/total,cnt))
        # print(rate)
        return rate
def load_files(path):
    files=glob.glob(path)  #리스트
    print(files)
    x=[]   #데이터
    y=[]   #정답
    for f in files:
        rate=makedata(f)
        x.append(rate)
        # print(f,'**',os.path.basename(f))
        y.append(os.path.basename(f)[:2])
    return {'data':x,'label':y}
    # print(y)

# train=load_files('data\\lang\\train\\*.*')  #{'data':[],'label':[]}
# # print(train)
# test=load_files('data\\lang\\test\\*.*')    #{'data':[],'label':[]}
# # print(test)
# model=SVC()   #모델생성
# model.fit(train['data'],train['label'])   #훈련
# pred=model.predict(test['data'])   #예측
# acc=accuracy_score(pred,test['label'])
# print('정확도',acc)




# -------------------------------
# print(ord('A'))
# print(ord('a'))
# print(chr(65))
# print(chr(97))
# a=[1,2,3,4,5,6]
# total=sum(a)
# print(total)
# # map(함수,반복가능객체)
# # lambda 입력:출력
# print(list(map(lambda x:2*x,a)))
# print(list(map(lambda x:x/total,a)))
# print(glob.glob('data\\*.xlsx'))
# print(os.path.basename('d:\\study\\ml'))
# print(os.path.basename('d:\\study\\ml\\movie.py'))
# basename은 경로의 마지막(디렉토리,파일 등 상관X)

# -----------------------------------

import urllib.request as req
# local = "mushroom.csv"
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
# req.urlretrieve(url,local)
# print("ok")
import pandas as pd
df = pd.read_csv('data\\mushroom.csv', header=None)
# print(df.head())
label = []
data = []
for index,value in df.iterrows():
    # print(value)
    label.append(value[0]) # 정답
    temp = []
    for d in value[1:]:
        temp.append(ord(d))
    data.append(temp)
trainx, testx, trainy, testy = train_test_split(data, label, test_size=0.25)

model = RandomForestClassifier()
model.fit(trainx, trainy)
pred = model.predict(testx)
acc = accuracy_score(pred, testy)
print('정확도',acc)




# dates=[['2019-01-01','2019-01-02','2019-01-03','2019-01-04'],
#        ['2019-02-01', '2019-02-02', '2019-02-03', '2019-02-04']]
# df = pd.DataFrame(dates,columns=['a','b','c','d'])
# # for k,v in df.iteritems():
# #     print(k)
# #     print(v)
# for k,v in df.iterrows():
#     print(k) # 행인데스
#     print(v) # 데이터
# print(df)
# for d in df: # 열이름
#     print(d)
# person = {"name":"kim","age":20,1004:"yes"}
# for k, v in person.items():
#     print(k,v)