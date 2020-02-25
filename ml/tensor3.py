import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

# a = tf.constant(10, name='a1')
# b = tf.constant(5)
# print(a)
# print(b)
# op = a+b
# v = tf.Variable(0)
# 변수는 반드시 초기화 해야한다.

# op2 = tf.assign(v, op)
# op = tf.add(a,b)
# print(op)
# sess = tf.Session()
# sess.run(tf.global_variables_initializer())
# print(sess.run(op))
# print(sess.run([a,b,op]))
# print(sess.run([op2,v]))
# sess.close()

# -----------------------------
# 변수 정의
# a = tf.placeholder(np.int32)
# b = tf.placeholder(tf.int32)
# c = tf.placeholder(tf.int32)
# op1 = a+b
# op2 = tf.multiply(op1, c)
# with tf.Session() as sess:
#     # print(sess.run(a, feed_dict={a:3}))
#     # print(sess.run(op1, feed_dict={a:3, b:100}))
#     print(sess.run([op2,op1], feed_dict={a:3, b:100,c:11}))
#     print(sess.run([op2,op1], feed_dict={a:[3,13], b:[100,1],c:7}))
# ---------------------------------
# state = tf.Variable(0)
# one = tf.constant(1)
# new_value = tf.add(state,one)
# update = tf.assign(state, new_value)
# sess = tf.Session()
# sess.run(tf.global_variables_initializer())
# for x in range(5):
#     sess.run(update)
#     result = sess.run(state)
#     print(result)
# sess.close()
# --------------------------
# a = tf.constant([1,2,3,4,5,6,7,8,9])
# b = tf.constant([[[1,1],[2,2]],[[3,3],[4,4]]])
# op1 = tf.reshape(a,[3,3])
# with tf.Session() as sess:
#     result = sess.run(op1)
#     print(result)
#     print(sess.run(b))
#     print(sess.run(tf.reshape(b,[4,-1])))
#     print(sess.run(tf.reshape(b,[-1])))
# --------------------------------
# pip install opencv-python
# import cv2
import matplotlib.pyplot as plt

# img = cv2.imread('img\\296. DRAMA.jpg')
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.axis('off')
# plt.show()
# cv2.imwrite('img\\img2.jpg',img)
# img2 = cv2.resize(img,(400,300))
# plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
# plt.axis('off')
# plt.show()
# print(type(img))
# img3 = img2[150:300,70:170]
# plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
# plt.axis('off')
# plt.show()
# ----------------------------------------------
# mnist = input_data.read_data_sets('../mnist/data/',one_hot=True)
# 0 : 1000000000
# 1 : 0100000000
# 7 : 0000000100
# print(mnist.train) # 학습용데이터, 정답
# print(mnist.test) # 검증용 데이터, 정답
# 데이터 갯수
# print('학습데이터 개수 : ',mnist.train.num_examples)
# print('검증데이터 개수 : ',mnist.test. num_examples)
# 실제 데이터 이미지
# print(mnist.train.images[100])
# plt.imshow(mnist.train.images[100].reshape(28,28),cmap='Greys',interpolation='nearest')
# plt.show()
# # 실제 데이터 정답
# print('정답 :', mnist.train.labels[100])
# dan = tf.placeholder(tf.int32)
# one = tf.constant(1)
# v = tf.Variable(0)
# op1 = tf.assign(v, v+one)
# op2 = dan * v
#
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(9):
#         sess.run(op1)
#         r, d, vv = sess.run([op2,dan,v], feed_dict={dan:5})
#         print('{} X {} = {}'.format(d,vv,r))
# 1~10까지 합
# one = tf.constant(1)
# v = tf.Variable(0)
# hap = tf.Variable(0)
# op1 = tf.assign(v, tf.add(v,one)) #v = v+1
# op2 = tf.assign(hap,tf.add(hap,v)) # hap = hap+v
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     for i in range(10):
#         sess.run(op1)
#         # print(sess.run(op2))
#         result = sess.run(op2)
#     print(result)

# tf.less(x,y) : x가 y보다 작다면 True
# tf.greater(x,y) : x가 y보다 크다면 True
# tf.equal(x,y) : x가 y와 크거나 같다면 True
a = tf.constant(5)
b = tf.constant(3)
op1 = tf.less(a,b)
with tf.Session() as sess:
    sess.run([a,b])
    # print(sess.run(tf.equal(a,b)))
    # print(sess.run(tf.less(a,b)))
    # print(sess.run(tf.greater(a,b)))
    result = sess.run(op1)
    print(result)
