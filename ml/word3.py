from konlpy.tag import Okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from PIL import Image
import numpy as np
# with open('data\\spring.csv', encoding='utf-8') as f:
#     source = f.read()
#     # print(source)
#     text = source.split('\n')
#     o = Okt()
#     temp = {}
#     for t in text:
#         malist = o.pos(t) #[(단어, 품사)]
#         # print(malist)
#         # print(len(malist))
#         for mal in malist: #(단어, 품사)
#             if (mal[1]=='Noun') | (mal[1]=='Verb'):
#                 if not mal[0] in temp:
#                     temp[mal[0]] = 0
#                 temp[mal[0]]=temp[mal[0]]+1
#         print(temp)
#         break
#         print(sorted(temp.items(),key=lambda x:x[1]))
# a = ['one','two','three','four','five']
# print(a)
# b = '-'.join(a)
# print(b)
# print(b.split('-'))
# print(sorted(a))
# b = {'red':5,'green':2,'blue':10}
# print(sorted(b.items(),key=lambda x:x[1]))
# -----------------------------------------------
# with open('data\\spring.csv', encoding='utf-8') as f:
#     o = Okt()
#     temp = []
#     for line in f:
#         malist = o.pos(line,norm=True, stem=True)
#         # print(malist)
#         for mal in malist:
#             if not mal[1] in ['Punctuation','Alpha','Josa','Eomi']:
#                 temp.append(mal[0])
#     str = ' '.join(temp)
# f2 = open('data\\spring2.csv','w',encoding='utf-8')
# f2.write(str)
# f2.close()
# -------------------------------
# from gensim.models import word2vec
# data = word2vec.LineSentence('data\\spring2.csv')
# model = word2vec.Word2Vec(data,size=200,window=10,min_count=2,sg=1,hs=1)
# model.save('data\\spring.model')

# ----------------------------------
from gensim.models import word2vec
# model = word2vec.Word2Vec.load('data\\spring.model')
# print(model.most_similar(positive=['봄']))
# print(model.most_similar(positive=['꽃']))
# print(model.most_similar(positive=['감자']))
# =============================================
o = Okt()
with open('data\\korona2.csv',encoding='utf-8') as f:
    temp = []
    for line in f:
        malist = o.pos(line, norm=True, stem=True)
        for mal in malist:
            if not mal[1] in ['VerbPrefix','Foreign','Josa','Punctuation','Alpha','Eomi']:
                temp.append(mal[0])
f2 = open('data\\korona3.csv','w',encoding='utf-8')
f2.write(' '.join(temp))
f2.close()
data = word2vec.LineSentence('data\\korona3.csv')
model = word2vec.Word2Vec(data, size=200, window=10, min_count=2, sg=1, hs=1)
# model.save('data\\korona.model')
# model = word2vec.Word2Vec('data\\korona.model')
print(model.most_similar(positive=['코로나']))