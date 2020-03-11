import json
import urllib.request
from konlpy.tag import Okt
import nltk
# 1번 -----------------------------------------------------
client_id = "****************"
client_secret = "*************"
encText = urllib.parse.quote("추석")
url = "https://openapi.naver.com/v1/search/news.json?query="+ encText + "&display=100&start=901" # json 결과
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
with open('data\\kimdonghyeon.txt','a',encoding='utf-8') as f:
    for dic in tojson['items']:
        description=dic['description']
        description=description.replace('<b>추석</b>','추석')
        description=description.replace(',',' ')
        str = '{}\n'.format(description)
        f.write(str)

# 2번 ----------------------------------------
source = open('data\\kimdonghyeon.txt', encoding='utf-8').read()
# print(source)
o = Okt()
nouns = o.nouns(source) # 명사추출
# 단어 제외시키기
nouns = [n for n in nouns if len(n) != 1 & (n != '위해') & (n != '지난') & (n != '우리')]
text = nltk.Text(nouns)
data = text.vocab() # 단어의 빈도수
# 상위단어 추출 : most_common()
data30 = data.most_common(30)
dic = dict(data30)
print(dic)

# 3번-----------------------------------
from gensim.models import word2vec
with open('data\\kimdonghyeon.txt',encoding='utf-8') as f:
    temp = []
    for line in f:
        malist = o.pos(line, norm=True, stem=True)
        for mal in malist:
            if not mal[1] in ['VerbPrefix','Foreign','Josa','Punctuation','Alpha','Eomi']:
                temp.append(mal[0])
        # print(temp)
f2 = open('data\\kimdonghyeon2.txt','w',encoding='utf-8')
f2.write(' '.join(temp))
f2.close()
data = word2vec.LineSentence('data\\kimdonghyeon2.txt')
model = word2vec.Word2Vec(data, size=200, window=10, min_count=2, sg=1, hs=1)
model.save('data\\kimdonghyeon.model')


# 4번 ----------------------------------------
# model = word2vec.Word2Vec('data\\kimdonghyeon.model')
print(model.most_similar(positive=['선물']))
