import pandas as pd
movies = pd.read_csv('data\\ml-1m\\movies.dat', sep="::", names=['MovieID','Title','Genres'])
# print(movies)
ratings = pd.read_csv('data\\ml-1m\\ratings.dat', sep="::", names=['UserID','MovieID','Rating','Timestamp'])
# print(ratings)

users = pd.read_csv('data\\ml-1m\\users.dat', sep="::", names=['UserID','Gender','Age','Occupation','Zip-code'])
# print(users)

ur = users.merge(ratings, on='UserID')
# print(ur)
data = ur.merge(movies, on='MovieID')
# print(data)
# print(data.columns)

# 성별에 따른 영화 평점
gender_rating = data.pivot_table(index='Title', columns="Gender", values='Rating')
# print(gender_rating)

# 제목별 영화 평점 건수
ratingcnt = data.groupby('Title').size()
# print(ratingcnt)
# print(type(ratingcnt))

# print(ratingcnt.sort_values(ascending=False))
# 200건 이상의 평점정보를 가진것만 추출
ratingcnt200 = ratingcnt[ratingcnt>=200]
# print(ratingcnt200)
# 200건 이상의 평점정보를 가진 영화제목
# print(ratingcnt200.index)
gender_rating = gender_rating.loc[ratingcnt200.index]
print(gender_rating)
print(gender_rating)
# 여자들이 좋아하는 영화순으로 출력
woman10 = gender_rating.sort_values(by='F', ascending=False).head(10)
# print(woman10)

# 남녀간에 호불호가 큰 영화
gender_rating['diff'] = gender_rating['F']-gender_rating['M']
gender_rating['diff'] = gender_rating['diff'].abs()
# print(gender_rating)
print(gender_rating.sort_values(by='diff', ascending=False))

# 성별에 관계없이 호불호가 큰 영화
movie_rating_std = data.groupby("Title")['Rating'].std()
# print(movie_rating_std)
movie_rating_std = movie_rating_std.loc[ratingcnt200.index]
print(movie_rating_std.sort_values(ascending=False).head(10))


