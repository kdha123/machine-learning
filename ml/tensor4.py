import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2

def mosaic(img,area,size):
    (x1, y1, x2, y2) = area
    temp = img[y1:y2,x1:x2]
    small = cv2.resize(temp,(size,size)) # 축소
    # 원래크기(모자이크 처리)
    temp = cv2.resize(small,(x2-x1,y2-y1),interpolation=cv2.INTER_AREA)
    tempimg = img.copy()
    tempimg[y1:y2,x1:x2] = temp
    return tempimg


# img = cv2.imread('img\\img2.jpg')
# print(img)
# plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
# plt.axis('off')
# plt.show()
# 모자이크 처리 200,196
# img2 = mosaic(img, (35,35,100,100),10)
# plt.imshow(cv2.cvtColor(img2,cv2.COLOR_BGR2RGB))
# plt.axis('off')
# plt.show()

# ----------------------
# img = cv2.imread('img\\irin2.jpg')
# img = cv2.imread('img\\red2.jpg')
# plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
# plt.axis('off')
# plt.show()
# ---------haarcascade_frontalface_alt.xml
# cascade_file = 'face.xml'
# cascade = cv2.CascadeClassifier(cascade_file)
# img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# # 얼굴인식
# face = cascade.detectMultiScale(img_gray,minSize=(30,30))
# if len(face)==0:
#     print('실패')
#     quit()
# print(face)
# for (x,y,w,h) in face:
#     img = mosaic(img,(x,y,x+w,y+h),5)
#
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.axis('off')
# plt.show()
# -------------------------------------
# xtrain = [1,2,3] # 학습데이터
# ytrain = [60,62,83] # 정답
# # h = wx+b
# w = tf.Variable(0.1)
# b = tf.Variable(0.1)
# # print(w, b)
# h = w*xtrain+b # 모델
# cost = tf.reduce_mean(tf.square(h-ytrain))
# train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(3001):
#         sess.run(train)
#         if i%50==0:
#             print(i,sess.run(cost),sess.run(w),sess.run(b))
# -------------------------------
# x = tf.placeholder(tf.float32, shape=[None])
# y = tf.placeholder(tf.float32, shape=[None])
# w = tf.Variable(tf.random_normal([1]))
# b = tf.Variable(tf.random_normal([1]))
# h = w*x+b
# cost = tf.reduce_mean(tf.square(h-y))
# train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(3001):
#         t,c,ww,bb = sess.run([train,cost,w,b], feed_dict={x:[1,2,3,4,5], y:[2.2,4.6,7,8.5,13]})
#         if i%100 == 0:
#             print(c,ww,bb)
#     # 예측
#     print(sess.run(h, feed_dict={x:[10]}))
# ----------------------------------------
# data = np.loadtxt('data\\cars.csv', skiprows=1, delimiter=',', unpack=True)
# print(data)
# x = data[0] # 데이터
# y = data[1] # 정답
# x, y값을 저장하기위한 변수 지정
# x = tf.placeholder(tf.float32, shape=[None])
# y = tf.placeholder(tf.float32, shape=[None])
# # tf.random_normal([1]) : 값하나를 얻는다.
# w = tf.Variable(tf.random_normal([1]))
# b = tf.Variable(tf.random_normal([1]))
# # print(w, b)
# h = w*x+b # 모델
# 모델에서 정답을 빼면 cost가 나온다.
# cost = tf.reduce_mean(tf.square(h-y))
# 최소화한 cost를 가지고 훈련한다.
# train = tf.train.GradientDescentOptimizer(learning_rate=0.0037).minimize(cost)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(3001):
#         t,c,ww,bb = sess.run([train,cost,w,b], feed_dict={x:data[0], y:data[1]})
#         if i%100==0:
#             print(c)
#
#     # 속도가 30일 때의 제동거리 예측
#     print(sess.run(h, feed_dict={x:[30]}))
#     result = sess.run(h, feed_dict={x:[0,30]})
#     print(result)
#     plt.plot(data[0], data[1],'o')
#     plt.plot([0,30], result)
#     plt.show()
# --------------------------------------------
x = [1,2,3]
y = [1,2,3]
w = tf.placeholder(tf.float32)
h = w*x
cost = tf.reduce_mean(tf.square(h-y))
with tf.Session() as sess:
    wlist = []
    clist = []
    for i in range(-30, 50):
        temp_w = i*0.1 # -30~-50을 0.1 단위로 변경
        cc, ww = sess.run([cost,w], feed_dict={w:temp_w})
        # print(cc)
        # print(ww)
        wlist.append(ww)
        clist.append(cc)
    plt.plot(wlist, clist)
    plt.xlabel('기울기')
    plt.xlabel('cost')
    plt.show()