# -*- coding: utf-8 -*-
import pymysql
from getData import get_all_ssq_data
import itertools
import logging
'''
    插入全部可能的双色球数据
'''
def insertBlueLosingLotteryData(results):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql_all = 'INSERT INTO blue_losing_lottery(TERMNUM,NUM_01,NUM_02,NUM_03,NUM_04,NUM_05,NUM_06,NUM_07,NUM_08,NUM_09,NUM_10,NUM_11,NUM_12,NUM_13,NUM_14,NUM_15,NUM_16) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '
    values = []
    dict={'losing_count_1':0,'losing_count_2':0,'losing_count_3':0,'losing_count_4':0,'losing_count_5':0,'losing_count_6':0,'losing_count_7':0,'losing_count_8':0,'losing_count_9':0,'losing_count_10':0,'losing_count_11':0,'losing_count_12':0,'losing_count_13':0,'losing_count_14':0,'losing_count_15':0,'losing_count_16':0}
    for i in reversed(results):
        for j in range(1,17):
            key_str = 'losing_count_' + str(j)
            if j not in i:
                dict[key_str]+=1
            else:
                dict[key_str]=0
        insert_tuple=(i[0],)+tuple(dict.values())
        values.append(insert_tuple)

    try:
       del_sql = "TRUNCATE TABLE blue_losing_lottery"
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
def updateBlueLosingLottery():
    results = get_blue_ssq_data()
    insertBlueLosingLotteryData(results)
"""
    获得中期数据，前60条
"""
def get_blue_ssq_data():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.`termnum`,t.`blue01` FROM SSQDATA t ORDER BY OPENDATE DESC"
    try:
       # 执行sql语句
       cur.execute(sql)
       results = cur.fetchall()
       # cur.execute(sql)
       # 提交到数据库执行
       # conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
    return results
if __name__ =='__main__':
    updateBlueLosingLottery()