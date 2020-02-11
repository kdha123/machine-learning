import time
from datetime import date
import requests
from bs4 import BeautifulSoup

now = date.today()
nowstring = now.strftime('%y-%m-%d')
print(nowstring)

for page in range(1, 3):
    time.sleep(1)
    pageurl='https://comic.naver.com/webtoon/list.nhn?titleId=570503&weekday=thu&page={}'
    url = pageurl.format(page)
    recvd = requests.get(url)
    # print(recvd)
    # print(recvd.text)
    dom = BeautifulSoup(recvd.text, 'lxml')

    # 이미지경로, 제목, 점수, 등록일
    table = dom.find('table',{'class':'viewList'})
    trs = table.find_all('tr')
    # print(len(trs),type(trs))
    cnt = 0
    # with open(os.path.join('data','webtoon.csv'), 'a', encoding='utf-8') as f:
    fn = 'd:\\study\\ml\\data\\' + nowstring + '.csv'
    with open(fn, 'a', encoding='utf-8') as f:
        for tr in trs:
            if cnt == 0:
                cnt = cnt + 1
                continue
            img = tr.find('img')['src']
            # print(img)
            td = tr.find('td',{'class':'title'})
            title = td.find('a').text
            # saveimg(img, title)
            # print(title)
            div = tr.find('div',{'class':'rating_type'})
            rating = div.find('strong').text
            # print(rating)
            regdate = tr.find('td',  {'class':'num'}).text
            # print(regdate)
            str = '{}, {}, {}\n'.format(title, rating, regdate)
            f.write(str)
# ---------------
# pip install pyinstaller
# pyinstaller --noconsole --onefile soup1.py
