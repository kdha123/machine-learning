# Generator
# Eiterator : next()함수를 사용해서 하나하나씩 꺼낼 수 있는 것
a = [1,2,3,4,5,6]
# print(type(a))
# print(a)
ra = reversed(a)
# print(type(ra))
# print(ra)
# print(next(ra))
# print(next(ra))
# print(next(ra))
# print(next(ra))
# print(next(ra))
# print(next(ra))
# print(next(ra)) <- 더이상 꺼낼 수 없으면 오류
for i in ra:
    # print(next(i)) <- 인덱스로 접근하는게 아니기 때문에 오류
    print(i)
# -----------------
# yield 키워드를 사용한 함수는 호출이 안된다.
# yield 키워드를 사용한 함수는 next()를 이용해야한다.
# def test():
#     print('test 함수')
#     yield 'test'
#
# print('a')
# test()
#
# print('b')
# print(test())
# ----------------------------
# return 문은 한번 반환하면 끝이지만
# yield는 함수를 여러번 실행하면서 차례대로 반환이 가능하다.
# 이것이 Generator
def test():
    print('a')
    yield 1
    print('b')
    yield 2
    print('c')
    yield 3

output = test()
k = next(output)
print(k)
k = next(output)
print(k)
k = next(output)
print(k)