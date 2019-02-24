import pymysql
def insertSelectedData(data):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = 'INSERT INTO selected_ssqdata(RED01, RED02, RED03, RED04,RED05,RED06,BLUE01) VALUES (%s,%s,%s,%s,%s,%s,%s) '
    try:
       cur.execute("TRUNCATE TABLE selected_ssqdata")
       # 执行sql语句
       cur.executemany(sql, data)
       # cur.execute(sql)
       # 提交到数据库执行
       conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
if __name__ =='__main__':
    data=[(3, 6, 9, 20, 28, 32, 3), (3, 5, 9, 18, 30, 32, 15), (6, 9, 15, 18, 22, 30, 13), (1, 14, 18, 20, 29, 33, 12), (1, 14, 16, 22, 27, 30, 3), (7, 14, 20, 24, 26, 32, 13), (8, 14, 21, 25, 30, 32, 16), (2, 7, 9, 16, 20, 25, 6), (7, 9, 18, 20, 27, 32, 8), (1, 4, 9, 14, 18, 24, 4)]
    insertSelectedData(data)