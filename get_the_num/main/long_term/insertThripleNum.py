# -*- coding: utf-8 -*-
import pymysql
from get_the_num.main.getData import get_long_data
import itertools
import logging
from itertools import combinations
'''
    插入三号一组统计
'''
def insertThripleData(results):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql_all = 'INSERT INTO thriple_num(thriple_num,thriple_count) VALUES (%s,%s) '
    values = []
    pair_list = list(combinations(range(1, 34), 3))
    for i in pair_list:
        count=0
        for j in results:
            if set(i).issubset(set(j)):
                count+=1
        data_tuple=(str(i),count)
        values.append(data_tuple)
    try:
       del_sql="TRUNCATE TABLE thriple_num"
       cur.execute(del_sql)
       # 执行sql语句
       cur.executemany(sql_all, values)
       # cur.execute(sql)
       # 提交到数据库执行
       conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
def updateThripleData():
    results = get_long_data()
    insertThripleData(results)
if __name__ =='__main__':
    results=get_long_data()
    # # results=((3,5,9,11,25,28),(1,5,9,11,25,28),(2,5,9,11,25,28),(1,5,9,11,25,28),(1,5,9,11,25,28),(1,5,9,11,25,28),(2,5,9,11,25,28),(1,5,9,11,25,28),(1,5,9,11,25,28),(2,5,9,11,25,28),(1,5,9,11,25,28),(1,5,9,11,25,28),(2,5,9,11,25,28),(2,5,9,11,25,28),(1,5,9,11,25,28),(1,5,9,11,25,28),(1,5,9,11,25,28),(1,5,9,11,25,28),(2,5,9,11,25,28),(2,5,9,11,25,28),)
    # results=((1,2,3,4,5,6),)
    insertThripleData(results)
    # print(get_prime_number_count((1,2,3,4,22,30)))