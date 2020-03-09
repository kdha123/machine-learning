from konlpy.tag import Hannanum, Kkma, Twitter
# h = Hannanum()
# malist = h.pos('침체된 경기를 활성화한다는 취지에선 긍정적이지만, 자칫 세금 낭비가 우려된다는 지적도 나온다.')
# print(malist)
# k = Kkma()
# malist = k.pos('침체된 경기를 활성화한다는 취지에선 긍정적이지만, 자칫 세금 낭비가 우려된다는 지적도 나온다.')
# print(malist)
# t = Twitter()

from konlpy.tag import Okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# o = Okt()
# malist = o.pos('침체된 경기를 활성화한다는 취지에선 긍정적이지만, 자칫 세금 낭비가 우려된다는 지적도 나온다.')
# print(malist)
# --------------------------
from konlpy.corpus import kolaw
# source = kolaw.open('constitution.txt').read()
# # print(source)
# o = Okt()
# nouns = o.nouns(source) # 명사추출
# # 단어 제외시키기
# nouns = [n for n in nouns if len(n)!=1 & (n !='로써') & (n !='다만') & (n !='모든') & (n !='그때')]
# print(nouns)
# print(nouns)
import nltk
from PIL import Image
import numpy as np
# text = nltk.Text(nouns)
# # print(text)
# data = text.vocab() # 단어의 빈도수
# # print(data)
# # 상위단어 추출 : most_common()
# data700 = data.most_common(700)
# print(data700)
# dic = dict(data700)
# print(dic)
# # 워드 클라우드
# img = Image.open('img\\three.jpg')
# mask = np.array(img)
# wc = WordCloud(font_path='malgun.ttf', mask=mask)
# w = wc.generate_from_frequencies(dic)
# plt.imshow(w)
# plt.axis('off')
# plt.show()
# 네이버 뉴스에서 '코로나'와 관련된 기사 300건을 검색하여
# title, description의 내용으로 워드클라우드를 예쁘게
import json
import urllib.request
client_id = "9eYRtkGNmEzbrUhDYxym"
client_secret = "QFU3tG14u2"
encText = urllib.parse.quote("코로나")
url = "https://openapi.naver.com/v1/search/news.json?query="+ encText + "&display=100&start=201" # json 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)

tojson=json.loads(result)

# print(len(tojson))
# print(type(tojson))
# print(tojson['items'])  #[{},{},...{}]
# with open('data\\korona.txt','a',encoding='utf-8') as f:
#     for dic in tojson['items']:
#         # print(dic['title'])
#         # print(dic['description'])
#         title=dic['title']
#         description=dic['description']
#         title=title.replace('<b>코로나</b>','코로나')
#         title=title.replace(',',' ')
#         description=description.replace('<b>코로나</b>','코로나')
#         description=description.replace(',',' ')
#         # print(title)
#         # print(description)
#         # print('-'*30)
#         str = '{},{}\n'.format(title, description)
#         f.write(str)
source = open('data\\korona.txt', encoding='utf-8').read()
print(source)
o = Okt()
nouns = o.nouns(source) # 명사추출
# # 단어 제외시키기
nouns = [n for n in nouns if len(n) != 1 & (n != '위해') & (n !='코로나')]
text = nltk.Text(nouns)
# print(text)
data = text.vocab() # 단어의 빈도수
# print(data)
# 상위단어 추출 : most_common()
data700 = data.most_common(700)
# print(data700)
dic = dict(data700)
print(dic)
# 워드 클라우드
img = Image.open('img\\three.jpg')
mask = np.array(img)
wc = WordCloud(font_path='malgun.ttf', mask=mask)
w = wc.generate_from_frequencies(dic)
plt.imshow(w)
plt.axis('off')
plt.show()
# ------------------------
# 네이버 블로그에서 '봄'을 1000건하여 title, description의 내용으로 data\\spring.csv로 저장