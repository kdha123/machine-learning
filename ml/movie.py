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
print(data.columns)