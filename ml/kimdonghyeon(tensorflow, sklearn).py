import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 1번

data = np.loadtxt('data\\product.csv', delimiter=',', skiprows=1, encoding="utf-8")
# print(data)
xdata = data[:,0:2]
# print(xdata)
ydata = data[:,[-1]]
# print(ydata)
x = tf.placeholder(tf.float32,[None,2])
y = tf.placeholder(tf.float32,[None,1])
w = tf.Variable(tf.random_normal([2,1]))
b = tf.Variable(tf.random_normal([1]))

h = tf.matmul(x,w) + b
cost = tf.reduce_mean(tf.square(h-y))
train = tf.train.GradientDescentOptimizer(0.03).minimize(cost)
# 훈련
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(3001):
        sess.run(train, feed_dict={x:xdata, y:ydata})
        if i % 500 == 0:
            print(sess.run(cost, feed_dict={x:xdata, y:ydata}))
        # 예측해보기
    print(sess.run(h, feed_dict={x:[[3,5]]}))
    # 기울기
    print(sess.run(w))
    # 절편
    print(sess.run(b))


# 2번.---------------------------------------------------------

data = pd.read_csv('data\\iris.csv')
# print(data)
x = data.loc[:,['Sepal.Length', 'Sepal.Width',  'Petal.Length',  'Petal.Width']]
y = data.loc[:,'Species']
print(x.head(5))
print(y.head(5))
# test_size = 0.3은 테스트셋이 30%를 의미함
trainx,testx,trainy,testy = train_test_split(x, y, test_size=0.3, shuffle=True)
model = SVC()
model.fit(trainx, trainy)
pred = model.predict(testx)
print('정답율',accuracy_score(pred,testy))

