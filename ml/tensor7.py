import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2


# water.csv 파일은 총 정수기 대여 대수(전월), 10년이상 노후 정수기 대여 대수(전월),
# AS시간(당월)에 대한 데이터이다. 주변의 신규 아파트가 동시 입주함에 따라 가입자수가
# 늘어 다음달의 AS시간을 예측하고 이에 따라 신규인력을 채용하고자 한다.

# 1) 10년미만 정수기 대여수와 10년이상 노후 정수기 대여수에 따라 AS시간을 예측하는
# 모델을 # tensorflow를 활용하여 작성하고 최종 cost와 기울기, 절편을 출력하시오.

# 2) 월말 최종 대여수를 보니 총 대여수가 300,000대, 그중 10년 이상 노후 정수기
# 대수가 70,000대로 집계되었다. 다음달의 AS시간을 예측하고 그에 따라 필요한
# AS기사의 인원수를 예측하시오.
# 단)AS기사 1명이 한달간 처리하는 AS시간=8시간*20일

# data = np.loadtxt('data\\water.csv', delimiter=',', skiprows=1)
# print(data)
# xdata = data[:,1:3]
# ydata = data[:,[-1]]
# x = tf.placeholder(tf.float32,[None,2])
# y = tf.placeholder(tf.float32,[None,1])
# w = tf.Variable(tf.random_normal([2,1]))
# b = tf.Variable(tf.random_normal([1]))
# h = tf.matmul(x,w) + b
# cost = tf.reduce_mean(tf.square(h-y))
# train = tf.train.GradientDescentOptimizer(0.00000000003).minimize(cost)
# # 훈련
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(3001):
#         sess.run(train, feed_dict={x:xdata, y:ydata})
#         if i % 500 == 0:
#             print(sess.run(cost, feed_dict={x:xdata, y:ydata}))
#         #예측
#     result = sess.run(h,feed_dict={x:[[70000,230000]]})
#     print(result)
#     print('필요인원수',round(result[0][0]/160))
    # print(result[0][0]/160)

# ----------------------------------------------------------------
# diabetes.csv
# 분류를 두 개로 할 때는 sigmoid가 적용이 된다.
# data = np.loadtxt('data\\diabetes.csv', delimiter=',')
# print(data.shape)
# # 훈련용 데이터
# trainx, trainy = data[:570,:8], data[:570,[-1]]
# # 검증용 데이터 # 0 정상 , 1 발병
# testx, testy = data[570:,8:], data[570:,[-1]]
# x = tf.placeholder(tf.float32,[None,8])
# y = tf.placeholder(tf.float32,[None,1])
# w = tf.Variable(tf.random_normal([8,1]))
# b = tf.Variable(tf.random_normal([1]))
# h = tf.sigmoid(tf.matmul(x,w)+b)
# cost = -tf.reduce_mean(y*tf.log(h)+(1-y)*tf.log(1-h))
# train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(20001):
#         sess.run(train, feed_dict={x:trainx, y:trainy})
#         if i%1000==0:
#             print(sess.run(cost,feed_dict={x:trainx, y:trainy}))
#     # 검증
#     # print(sess.run(h,feed_dict={x:testx,y:testy}))
#     pred = tf.cast(h>0.5, dtype=tf.float32)
#     acc = tf.reduce_mean(tf.cast(tf.equal(pred,y), tf.float32))
#     print('정확도',sess.run(acc, feed_dict={x:trainx, y:trainy}))

