from konlpy.tag import Okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from PIL import Image
import numpy as np
import json
import urllib.request

# 네이버 블로그에서 '봄'을 1000건하여 title, description의 내용으로 data\\spring.csv로 저장
client_id = "9eYRtkGNmEzbrUhDYxym"
client_secret = "QFU3tG14u2"
encText = urllib.parse.quote("봄")
url = "https://openapi.naver.com/v1/search/blog?start=1000&display=100&query=" + encText # json 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
tojson = json.loads(result)
with open('data\\spring.csv','a',encoding='utf-8') as f:
    for dic in tojson['items']:
        title = dic['title']
        description = dic['description']
        title = title.replace('<b>봄</b>', '봄')
        title = title.replace(',', ' ')
        description = description.replace('<b>봄</b>', '봄')
        description = description.replace(',', ' ')
        print(title)
        print(description)
        print('-'*30)
        str = '{},{}\n'.format(title, description)
        f.write(str)