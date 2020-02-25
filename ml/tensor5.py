import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2

# a = tf.constant([5,100,1,2])
# b = tf.constant([[1,2,3],[4,5,6],[1,1,1]])
# with tf.Session() as sess:
    # print(sess.run(a))
    # 가장 큰 값의 인덱스
    # print(sess.run(tf.argmax(a,0)))
    # 가장 작은 값의 인덱스
    # print(sess.run(tf.argmin(a,0)))
    # print(sess.run(b))
    # 0 = 세로방향 , 1 = 가로방향
    # 가장 큰 값의 인덱스 위치
    # print(sess.run(tf.argmax(b,0)))
    # print(sess.run(tf.argmax(b,1)))

# ---------------------------------------
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("../mnist/data/", one_hot=True)
# print(mnist.train) # 학습용 데이터
# print(mnist.test) # 검증용 데이터
# print('학습데이터의 개수', mnist.train.num_examples) # 55000
# print('검증데이터의 개수', mnist.test.num_examples) # 10000
# print('학습데이터의 10001번째 데이터',mnist.train.images[10000])
# plt.imshow(mnist.train.images[10000].reshape(28,28),cmap='Greys',
#            interpolation='nearest')
# plt.show()
# print('학습데이터의 10001번째 정답',mnist.train.labels[10000])
# print('학습데이터의 10001째 데이터 차원',mnist.train.images[10000].shape)
# print('검증데이터의 10001번째 데이터',mnist.test.images[1000])
# print('검증데이터의 10001번째 데이터 이미지')
# plt.imshow(mnist.test.images[1000].reshape(28,28),cmap='Greys',
#            interpolation='nearest')
# plt.show()
# print('검증데이터의 1001번째 정답',mnist.test.labels[1000])
# print('학습데이터의 10001째 데이터 차원',mnist.test.images[1000].shape)

# h = wx+b
# h = xw+b => [None,784]x[784,10] =[None,10]
# x = tf.placeholder(tf.float32,[None,784])
# # 정답
# y = tf.placeholder(tf.float32,[None,10])
# w = tf.Variable(tf.random_normal([784,10]))
# b = tf.Variable(tf.random_normal([10]))
# # 다중 분류
# h = tf.nn.softmax(tf.matmul(x,w)+b)
# cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(h),axis=1))
# train = tf.train.GradientDescentOptimizer(0.5).minimize(cost)
#
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     # r = sess.run(h,feed_dict={x:mnist.train.images[10000:10001]})
#     # print(r)
#     # print(sess.run(tf.argmax(r,1)))
#     for i in range(1001):
#         batch_x, batch_y = mnist.train.next_batch(1000)
#         t,c = sess.run([train,cost], feed_dict={x:batch_x,y:batch_y})
#         if i % 100 == 0:
#             # print(i,c)
#             corr = tf.equal(tf.argmax(h,1),tf.argmax(y,1))
#             # 두개가 똑같으면 1, 틀리면 0
#             acc = sess.run(tf.reduce_mean(tf.cast(corr,tf.float32)), feed_dict={x:batch_x,y:batch_y})
#             # print(i,'정확도',acc)
#     #   검증
#     import random
#     r = random.randint(0,mnist.test.num_examples-1)
#     print('실제 정답',sess.run(tf.argmax(mnist.test.labels[r:r+1],1)))
#     # 우리 눈에 보이게 하려면 가로세로 28
#     plt.imshow(mnist.test.images[r:r+1].reshape(28,28),cmap='Greys', interpolation='nearest')
#     plt.show()
# --------------------------------------------------
data = np.loadtxt('data\\zoo\\zoo.csv', delimiter=',')
print(data.shape)
xdata=data[:,:16]
ydata = data[:,[-1]]
print(xdata) #(101, 16)
print(ydata) #(101, 1)
x = tf.placeholder(tf.float32,[None,16])
y = tf.placeholder(tf.int32,[None,1]) #0~6
# h = xw+b
# h = [None,16]x[?,?] = [None,7] 따라서 w는 [16,7] b에는 값의 갯수가 나와야함.
w = tf.Variable(tf.random_normal([16,7]))
b = tf.Variable(tf.random_normal([7]))
sess = tf.Session()
sess.run(tf.global_variables_initializer())
onehot = tf.one_hot(y,7)
# print(sess.run(onehot,feed_dict={y:ydata}))
# 3차원을 2차원으로 바꾸는 작업(차원이 맞지 않아서)
onehot = tf.reshape(onehot,[-1,7])
print(sess.run(onehot,feed_dict={y:ydata}))
logits = tf.matmul(x,w)+b
h = tf.nn.softmax(logits)
tempcost = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=onehot)
cost = tf.reduce_mean(tempcost)
train = tf.train.GradientDescentOptimizer(0.7).minimize(cost)
for i in range(2001):
    sess.run(train,feed_dict={x:xdata,y:ydata})
    if i % 100 == 0:
        print(i,sess.run(cost,feed_dict={x:xdata,y:ydata}))
corr = tf.equal(tf.argmax(h,1), tf.argmax(onehot,1)) # 0,1,1,0,1...
acc = tf.reduce_mean(tf.cast(corr,tf.float32))
print(sess.run(acc,feed_dict={x:xdata,y:ydata}))
# 검증하기
sample= [[1,0,0,1,0,0,1,1,1,1,0,0,4,1,1,0]]
print('예측',sess.run(tf.argmax(h,1),{x:sample}))