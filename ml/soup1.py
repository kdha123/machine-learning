# format
# print('{} + {} = {}'.format(3, 4, 3+4))
# print('{0} + {1} = {1}'.format(3, 4, 3+4))
# print('%d + %d = %d' %(3,4,3+4))
# print('%s + %s = %s' %('3',4,3+4))
# print('%d + %s = %s' %('a',4,3+4))
# print('%0.4f'%(3.141592))
# =========================
import os
import requests
from bs4 import BeautifulSoup
import time
#
#
def saveimg(img, title):
    title = title.replace(':','')
    title = title.replace('<','')
    title = title.replace('>','')
    title = title.replace('?','')
    title = title.replace('/','')
    filename = 'img\\' + title + img[-27:-23]
    # print(filename)
    print(img[-27: -23])
    revcdimg = requests.get(img)
    print(revcdimg)
    f = open(filename, 'wb')
    f.write(revcdimg.content)
#
#
#
# url='https://comic.naver.com/webtoon/list.nhn?titleId=570503&weekday=thu'
# recvd = requests.get(url)
# # print(recvd)
# # print(recvd.text)
# dom = BeautifulSoup(recvd.text, 'lxml')
#
# # 이미지경로, 제목, 점수, 등록일
# table = dom.find('table',{'class':'viewList'})
# trs = table.find_all('tr')
# # print(len(trs),type(trs))
# cnt = 0
# with open(os.path.join('data','webtoon.csv'), 'w', encoding='utf-8') as f:
# # with open('data\\webtoon.csv', 'w', encoding='utf-8') as f:
#     for tr in trs:
#         if cnt == 0:
#             cnt = cnt + 1
#             continue
#         img = tr.find('img')['src']
#         # print(img)
#         td = tr.find('td',{'class':'title'})
#         title = td.find('a').text
#         saveimg(img, title)
#         # print(title)
#         div = tr.find('div',{'class':'rating_type'})
#         rating = div.find('strong').text
#         # print(rating)
#         regdate = tr.find('td',  {'class':'num'}).text
#         # print(regdate)
#         str = '{}, {}, {}\n'.format(title, rating, regdate)
#         f.write(str)

# --------------------------페이징
# for page in range(1,6):
#     time.sleep(1)
#     pageurl='https://comic.naver.com/webtoon/list.nhn?titleId=570503&weekday=thu&page={}'
#     url = pageurl.format(page)
#     recvd = requests.get(url)
#     # print(recvd)
#     # print(recvd.text)
#     dom = BeautifulSoup(recvd.text, 'lxml')
#
#     # 이미지경로, 제목, 점수, 등록일
#     table = dom.find('table',{'class':'viewList'})
#     trs = table.find_all('tr')
#     # print(len(trs),type(trs))
#     cnt = 0
#     with open(os.path.join('data','webtoon.csv'), 'a', encoding='utf-8') as f:
#     # with open('data\\webtoon.csv', 'w', encoding='utf-8') as f:
#         for tr in trs:
#             if cnt == 0:
#                 cnt = cnt + 1
#                 continue
#             img = tr.find('img')['src']
#             # print(img)
#             td = tr.find('td',{'class':'title'})
#             title = td.find('a').text
#             saveimg(img, title)
#             # print(title)
#             div = tr.find('div',{'class':'rating_type'})
#             rating = div.find('strong').text
#             # print(rating)
#             regdate = tr.find('td',  {'class':'num'}).text
#             # print(regdate)
#             str = '{}, {}, {}\n'.format(title, rating, regdate)
#             f.write(str)
# ============================================이미지까지, 책제목, 확장자
import os
import sys
import json
import urllib.request
client_id = "9eYRtkGNmEzbrUhDYxym"
client_secret = "QFU3tG14u2"
encText = urllib.parse.quote("증상")
url = "https://openapi.naver.com/v1/search/book.json?display=100&query=" + encText # json 결과
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
# 책 제목, 저자, 출판사, 가격 ==> data\\book.csv, 이미지( 책제목, 확장자)
with open("data\\book.csv", 'w', encoding='utf-8')as f:
    tojson = json.loads(result)
    print(tojson)
    for dic in tojson['items']:
        title = dic['title']
        title = title.replace('<b>증상</b>', '증상')
        image = dic['image']
        # print(image)
        saveimg(image, title)
        author = dic['author']
        publisher = dic['publisher']
        price = dic['price']
        str = '{},{},{},{},{}\n'.format(title, image, author, publisher, price)
        f.write(str)