from wordcloud import WordCloud
import matplotlib.pyplot as plt
# source = open('data\\alice.txt').read()
# print(source)
# wc = WordCloud(background_color='skyblue')
# w = wc.generate(source)
# plt.imshow(w)
# plt.axis('off')
# plt.show()
# 배경 이미지 ----------------------------
from PIL import Image
import numpy as np
# img = Image.open('img\\three.jpg')
# mask = np.array(img) # byte 배열 생성
# # print(mask)
# source = open('data\\alice.txt').read()
# wc = WordCloud(mask=mask)
# w = wc.generate(source)
# plt.imshow(w)
# plt.axis('off')
# plt.show()

# 불필요한 단어 제거----------------
from wordcloud import STOPWORDS
# sw = set(STOPWORDS)
# print(sw)
# sw.add('Alice')
# sw.add('said')
# img = Image.open('img\\three.jpg')
# mask = np.array(img) # byte 배열 생성
# print(mask)
# source = open('data\\alice.txt').read()
# wc = WordCloud(mask=mask, stopwords=sw)
# w = wc.generate(source)
# plt.imshow(w)
# plt.axis('off')
# plt.show()

# yesterday 노래가사를 검색하여 'yesterday' 단어를 제외하고
# 예쁘게 워드클라우드 만드세요---------------------------------
sw = set(STOPWORDS)
print(sw)
sw.add('yesterday')
img = Image.open('img\\three.jpg')
mask = np.array(img) # byte 배열 생성
print(mask)
source = open('data\\yesterday.txt', encoding='utf-8').read()
wc = WordCloud(mask=mask, stopwords=sw, font_path='malgun.ttf', max_font_size=300)
w = wc.generate(source)
plt.imshow(w)
plt.axis('off')
plt.show()