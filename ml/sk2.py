import glob
import os
# def load_files(path):
#     # print(glob.glob(path))  #[파일명1,파일명2,...]
#     for fname in glob.glob(path):
#         print(fname)
#         print(os.path.basename(fname))
#         print(os.path.basename(fname)[:2])   #정답
#     print(ord('A'))
#     print(ord('a'),ord('z'))
#     print(chr(66))
#     print(chr(98))
#
# train=load_files('data\\lang\\train\\*.*')
# ---------
def makedata(fname):
    with open(fname,encoding='utf-8') as f:
        text=f.read()
        text=text.lower()
        # print(text)
        # print('-'*30)
        code_a=ord('a')
        code_z=ord('z')
        cnt =[0 for n in range(26)]
        # print(cnt)
        for i in text:
            if code_a<=ord(i)<=code_z:
                cnt[ord(i)-code_a] = cnt[ord(i)-code_a]+1
        print(cnt)
        total = sum(cnt)
        rate = list(map(lambda x:x/total, cnt))
        print(rate)

def load_files(path):
    # print(glob.glob(path))
    x=[]   #데이터
    y=[]   #정답
    for fname in glob.glob(path):
        data=makedata(fname)
        print(data)
        break
        # x.append(data)
        # y.append(os.path.basename(fname)[:2])
    # print(y)


train=load_files('data\\lang\\train\\*.*')
# a = [1,2,3,4,5,6]
# total = sum(a)
# print(total)
# b = list(map(lambda x:2*x, a))
# b = list(map(lambda x:x/total,a))
# print(b)

