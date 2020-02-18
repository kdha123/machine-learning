import numpy as np
# 생성 np.array(리스트, 속성)
# 속성 : dtype
a =  [1,2,3,4,5]
# print(type(a), a)
# arr1 = np.array(a)
# print(arr1, type(arr1))
# arr1 = np.array(a, dtype=float)
# print(arr1)
# b=[[1,2,3],[4,5,6]]
# arr2= np.array(b)
# print(arr2)
# c=[[[1,2],[3,4]],[[5,6],[7,8]]]
# arr3 = np.array(c)
# print(arr3)
# print(arr3.shape)
# print(arr3.dtype)
# print(arr3.ndim)
# arr1 = np.array(a)
# print(arr1.shape)

# 초기화 함수
# np.zeros(shape,속성)
# np.ones(shape,속성)
# np.full(shape, 값)
# np.empty(shape)
# np.eye(숫자)

# x = np.zeros((2,4))
# print(x)
# print(x.dtype)
# x = np.zeros((2,3,4), dtype=int)
# print(x)
# print(x.dtype)
# x = np.full((5,2),9)
# print(x)
# x = np.empty((5,2))
# print(x)
# x = np.eye(7)
# print(x)
# a = [[1,2,3,],[4,5,6]]

# 값이 정해져 있을 때
# print(np.array(a))
# np.zeros_like(리스트)
# np.ones_like(리스트)
# np.full_like(리스트)
# np.empty_like(리스트)
# arr1 = np.zeros_like(a)
# print(arr1)
# arr1 = np.ones_like(a)
# print(arr1)
# arr1 = np.full_like(a,5)
# print(arr1)
# arr1 = np.empty_like(a)
# print(arr1)

# 데이터 생성
# np.linspace(시작, 종료, 개수, 속성)
# a1 = np.linspace(0, 1, 5)
# print(a1)
# a1 = np.linspace(0, 1, 6)
# print(a1)
# 개수를 지정하지 않으면 50개
# a1 = np.linspace(0, 1)
# print(a1)
# 마지막 값 포함 여부
# a1 = np.linspace(0, 1, 5, endpoint=False)
# print(a1)
# a1 = np.linspace(0, 1, 5, dtype=int)
# print(a1)
# np.arange(시작,종료,스텝,[dtype])
# a1 = np.arange(0,10,2)
# print(a1)
# a1 = np.arange(10)
# print(a1)

# 난수데이터 생성
# np.random.normal(속성)
# loc : 평균
# scale : 표준편차
# size : 행,열
# a = np.random.normal(loc=0,scale=1, size=(2,3))
# print(a)
# np.random.randint(시작, 종료, 속성)
# a = np.random.randint(10,20,size=(5,))
# print(a)
# ------------------
# a1 = np.arange(10)
# print(a1[3])
# print(a1[5:8])
# a2 = a1[5:8]
# print(a2)
# a2[0] = 10
# print(a2) # numpy 배열의 조각은 원본배열의 뷰
# print(a1)
# a3 = a1[5:8].copy()
# a3[0] = 99
# print(a3)
# print(a1)
# --------------------
# a1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a1)
# print(a1[:2])
# print(a1[:2,1:])
# print(a1[:,:1])
# a1[:2,1:2]=0
# print(a1)
# boolean 추출
# np.random.seed(9)
# colors = np.array(['red','orange','blue','red','blue','orange','orange'])
# print(colors)
# data = np.random.randn(7,4)
# print(data)
# print(colors=='orange')
# print(data[colors=='orange'])
# print(data[colors=='blue'])
# --------------------
# x = np.arange(12)
# print(x)
# print(x.reshape(3,4))
# print(x.reshape(2,3,2))
# print(x.reshape((3,5))) err
# y = np.arange(20)
# print(y)
# y = y.reshape(4, -1) # 4*-1:나머지값(5) =20
# print(y)
# y = y.reshape(2, -1, 2)
# print(y)
# y = y.reshape(3, -1) err
# print(y)
# y = y.reshape(-1)
# print(y)

# 행렬곱
# (2,3)x (2,3) => err
# (2,3)x (3,2) => (2,2)
# (2,3)x (3,4) => (2,4)

# x = np.array([[1,2,3],[4,5,6]])
# print(x)
# y = np.array([[1,0,-1],[1,1,0]])
# print(y)
# print(np.dot(x,y)) err
# print(y.T) # 3행 2열
# print(np.dot(x,y.T))
# print(x.T)
# print(np.dot(x.T,y))
# 3,2 x 2,3 = 3,3

# 입출력
# data = np.loadtxt('data\\heights.csv', skiprows=1, delimiter=',')
# print(data)
# data = np.loadtxt('data\\heights.csv', skiprows=1, delimiter=',', unpack=True)
# print(data)
# -------------------
# a = np.random.randint(0,10,size=(2,4))
# print(a)
# np.savetxt('data\\num.csv', a, delimiter=',')
# ------------------------
# a = np.random.randint(0,10,size=(2,4))
# print(a)
# np.save('data\\arr1', a)
# b = np.random.randint(0,10,size=(30))
# c = np.random.randint(0,10,size=(2,3,4))
# print(c)
# print(b)
# np.savez('data\\arr2',a,b,c)
# np.load()
print(np.load('data\\arr1.npy'))
print(np.load('data\\arr2.npz'))
print(np.load('data\\arr2.npz').files)
print(np.load('data\\arr2.npz')['arr_0'])
print(np.load('data\\arr2.npz')['arr_1'])
print(np.load('data\\arr2.npz')['arr_2'])
