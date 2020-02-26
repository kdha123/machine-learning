from sklearn.svm import LinearSVC, SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# data = [[0,0],
#         [0,1],
#         [1,1],
#         [1,0]]
# label = [0,0,0,1]
# # 모델 생성
# model = LinearSVC()
# # 훈련
# model.fit(data,label)
# # 예측
# test_data = [[0,0],
#         [0,1],
#         [1,1],
#         [1,0]]
# test_label = [0,0,0,1]
# pred = model.predict(test_data)
# # 정확도
# acc = accuracy_score(pred, test_label)
# print('정확도',acc)
# --------------------------
# xor_data = [[0,0],
#         [0,1],
#         [1,0],
#         [1,1]]
# label = [0,1,1,0]
# # 모델 생성
# # model = LinearSVC()
# neighbors
# model = KNeighborsClassifier(n_neighbors=1)
# # 훈련
# model.fit(xor_data,label)
# # 예측
# test_data = [[0,0],
#         [0,1],
#         [1,0],
#         [1,1]]
# test_label = [0,1,1,0]
# pred = model.predict(test_data)
# # 정확도
# acc = accuracy_score(pred, test_label)
# print('정확도',acc)
# ---------------------------------------
import pandas as pd
from sklearn.model_selection import train_test_split
# data = pd.read_csv('data\\iris.csv')
# # print(data)
# x = data.loc[:,['Sepal.Length', 'Sepal.Width',  'Petal.Length',  'Petal.Width']]
# y = data.loc[:,'Species']
# # print(x.head(5))
# # print(y.head(5))
# trainx,testx,trainy,testy = train_test_split(x, y, test_size=0.2,shuffle=True)
# model = SVC()
# model.fit(trainx, trainy)
# pred = model.predict(testx)
# print('정답율',accuracy_score(pred,testy))
# ----------------------------------------
import matplotlib.pyplot as plt
tbl = pd.read_csv('data\\bmi.csv')

# 열을 자르고 정규화하기
label = tbl["label"]
w = tbl["weight"]
h = tbl["height"]
wh = pd.concat([w,h], axis=1)

# 학습 전용 데이터왕 테스트 전용 데이터로 나누기
data_train, data_test, label_train, label_test = train_test_split(wh, label)

# 모델 생성후 데이터 학습하기
model = SVC()
model.fit(data_train,label_train)
# 예측하기
pred = model.predict(data_test)
# 결과 테스트
acc = accuracy_score(label_test, pred)
report = classification_report(label_test, pred)

print('정확도',acc)
print('리포트',report)
