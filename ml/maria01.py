import pymysql as my
# 1) db연결
con = my.connect(host='localhost',
                 user='tom',
                 password='jerry',
                 db='bookdb',
                 port=3307,
                 charset='utf8')
# 2) 커서 생성
cur = con.cursor(my.cursors.DictCursor)

# 3) 쿼리문
sql = 'select * from books_publisher'
# 4) 실행
cur.execute(sql)
rows = cur.fetchall()
print(type(rows), rows)
for row in rows:
    # print(row[0], row[1], row[2], row[3])
    print(row['id'], row['name'], row['address'], row['website'])
# 5) 종료
con.close()

# 입력, 수정, 삭제 ----------------------------


# 1) db연결
con = my.connect(host='localhost',
                 user='tom',
                 password='jerry',
                 db='bookdb',
                 port=3307,
                 charset='utf8')
# 2) 커서 생성
cur = con.cursor(my.cursors.DictCursor)

# 3) 쿼리문
# sql = 'insert into books_publisher(name, address, website) values (%s,%s,%s)'
# sql = 'update books_publisher set address=%s, website=%s'
sql = 'delete from books_publisher where id=%s'
# 4) 실행
# cur.execute(sql,('한빛','서울','hanbit.com'))
# cur.execute(sql,('구로','hanbeat.com'))
cur.execute(sql,(4))
con.commit()
# 5) 종료
con.close()
