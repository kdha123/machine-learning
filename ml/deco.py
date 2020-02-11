# 데코레이터 - 함수데코레이터, 클래스데코레이터
# def test(function):
#     return 'test함수'
# @test
# # hello가 test()의 매개변수로 전달이 된다.
# def hello():
#     pass
# print(hello)

# 함수가 수행되기 전과 후에 다른 처리를 하고 싶을때
# 함수데코레이터를 만들어서 사용할 수 있다.
# 데코레이터가 있는 함수가 매개변수로 간다.
def test(f):
    def inner():
        print('start')
        f()
        print('end')
    return inner

@test
def hello():
    print('hello~~')

hello()
# -----------------
class Test:
    def __init__(self,func):
        print('생성자 호출')
        self.func = func

    def __call__(self, *args, **kwargs):
        print('start')
        self.func()
        print('end')

@Test
def hello():
    print('hello~~~~~')

print('호출전')
hello()
print('호출후')
