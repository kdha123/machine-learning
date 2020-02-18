import tensorflow as tf
import numpy as np

# 상수 노드
# c1 = tf.constant(3)
# c2 = tf.constant(3, np.float32)
# c3 = tf.constant([3,4,5])
# print(c1)
# print(c2)
# print(c3)

# 텐서플로의 실행
# sess = tf.Session()
# print(sess.run(c1))
# print(sess.run(c2))
# print(sess.run(c3))
# sess.close()

# ---------------------
# c1 = tf.constant(3)
# c2 = tf.constant(4)
# op1 = c1 + c2 # op1 = tf.add(c1,c2)
# op2 = tf.multiply(c1, c2)
# print(op1)
# print(op2)
# sess = tf.Session()
# print(sess.run(op1))
# print(sess.run(op2))
# print(sess.run([c1,c2,op2]))
# ------------
# a = tf.constant(3, dtype=tf.int32, name='a1')
# b = tf.constant(4)
# c = tf.constant(5)
# d = tf.multiply(a,b)
# e = tf.add(c,b)
# f = tf.subtract(d,e)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# with tf.Session() as sess:
#     print(sess.run(e))
#     print(sess.run(f))

# 변수 : 변수는 반드시 초기화 후에 사용해야함 -------------
# a = tf.constant(3, dtype=tf.int32, name='a1')
# b = tf.constant(4)
# c = tf.constant(5)
# op = (a+b)*c
# 변수 선언
# v = tf.Variable(0)
# 변수에 결과 대입하기
# op2 = tf.assign(v, op) # v=(a+b)*c
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer()) # 변수 초기화
#     print(sess.run([v,op2]))
# --------------------------------
# a = tf.constant([[1,2,3],[4,5,6]])
# print(a)
# print(a.get_shape())
# b = tf.constant([[1],[0],[1]])
# print(b.get_shape())
# op1 = tf.matmul(a, b)
# with tf.Session() as sess:
#     print(sess.run(op1))

# 초기화
# a = tf.zeros_like([4,3,2])
# b = tf.zeros([4,3,2])
# print(a)
# with tf.Session() as sess:
#     print(sess.run(a))
#     print(sess.run(b))

# tf.palceholder()
# a = tf.placeholder(tf.int32, [3])
# b = tf.constant(2)
# op=a*b
# with tf.Session() as sess:
#     print(sess.run(op,feed_dict={a:[7,5,3]}))
#     print(sess.run(op,feed_dict={a:[10,20,30]}))
# ----------------
# a = tf.placeholder(tf.int32, [None])
# b = tf.constant(2)
# op=a*b
# with tf.Session() as sess:
#     print(sess.run(op,feed_dict={a:[7,5,3]}))
#     print(sess.run(op,feed_dict={a:[10,20,30]}))
#     print(sess.run(op,feed_dict={a:[10,20,30,100,200]}))
# --------------------------------------------------------
# x = np.random.randn(3,4)
# y = np.random.randn(4,2)
# a = tf.placeholder(tf.float32,shape=(3,4))
# b = tf.placeholder(tf.float32,shape=(4,2))
# op = tf.matmul(a,b)
# with tf.Session() as sess:
#     print(sess.run(op,feed_dict={a:x,b:y}))
# p246~p247 ----------------------------------
# 상수 정의하기
a = tf.constant(120, name='a')
b = tf.constant(130, name='b')
c = tf.constant(140, name='c')

# 변수 정의하기
v = tf.Variable(0, name='v')

# 데이터 플로우 그래프 정의하기
calc_op = a + b + c
assign_op = tf.assign(v,calc_op)

# 세션 실행하기
with tf.Session() as sess:
    print(sess.run(assign_op))
    print(sess.run(v))