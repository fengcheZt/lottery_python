# -*- coding: utf-8 -*-
import pymysql
from getData import get_all_ssq_data
import itertools
import logging
'''
    插入蓝球出现次数表
'''
def insertBlueOccurNumData():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    # sql_all = 'INSERT INTO blue_occur_num(id,num,amount) VALUES (%s,%s,(SELECT COUNT(*) FROM blue_losing_lottery WHERE num_%s=0)) '
    # values = []
    # for i in range(1,17):
    #     if i<10:
    #         stri="0"+str(i)
    #     insert_tuple=(i,i,stri)
    #     values.append(insert_tuple)

    try:
       del_sql = "TRUNCATE TABLE blue_occur_num"
       cur.execute(del_sql)
       sql_01 = "INSERT INTO blue_occur_num VALUE (1,'01',(SELECT COUNT(*) FROM blue_losing_lottery WHERE num_01 =0))"
       sql_02 = "INSERT INTO blue_occur_num VALUE (2,'02',(SELECT COUNT(*) FROM blue_losing_lottery WHERE num_02 =0))"
       sql_03 = "INSERT INTO blue_occur_num VALUE (3,'03',(SELECT COUNT(*) FROM blue_losing_lottery WHERE num_03 =0))"
       sql_04 = "INSERT INTO blue_occur_num VALUE (4,'04',(SELECT COUNT(*) FROM blue_losing_lottery WHERE num_04 =0))"
       sql_05 = "INSERT INTO blue_occur_num VALUE (5,'05',(SELECT COUNT(*) FROM blue_losing_lottery WHERE num_05 =0))"
       sql_06 = "INSERT INTO blue_occur_num VALUE (6,'06',(SELECT COUNT(*) FROM blue_losing_lottery WHERE num_06 =0))"
       sql_07 = "INSERT INTO blue_occur_num VALUE (7,'07',(SELECT COUNT(*) FROM blue_losing_lottery WHERE num_07 =0))"
       sql_08 = "INSERT INTO blue_occur_num VALUE (8,'08',(SELECT COUNT(*) FROM blue_losing_lottery WHERE num_08 =0))"
       sql_09 = "INSERT INTO blue_occur_num VALUE (9,'09',(SELECT COUNT(*) FROM blue_losing_lottery WHERE num_09 =0))"
       sql_10 = "INSERT INTO blue_occur_num VALUE (10,'10',(SELECT COUNT(*) FROM blue_losing_lottery WHERE num_10 =0))"
       sql_11 = "INSERT INTO blue_occur_num VALUE (11,'11',(SELECT COUNT(*) FROM blue_losing_lottery WHERE num_11 =0))"
       sql_12 = "INSERT INTO blue_occur_num VALUE (12,'12',(SELECT COUNT(*) FROM blue_losing_lottery WHERE num_12 =0))"
       sql_13 = "INSERT INTO blue_occur_num VALUE (13,'13',(SELECT COUNT(*) FROM blue_losing_lottery WHERE num_13 =0))"
       sql_14 = "INSERT INTO blue_occur_num VALUE (14,'14',(SELECT COUNT(*) FROM blue_losing_lottery WHERE num_14 =0))"
       sql_15 = "INSERT INTO blue_occur_num VALUE (15,'15',(SELECT COUNT(*) FROM blue_losing_lottery WHERE num_15 =0))"
       sql_16 = "INSERT INTO blue_occur_num VALUE (16,'16',(SELECT COUNT(*) FROM blue_losing_lottery WHERE num_16 =0))"
       cur.execute(sql_01)
       cur.execute(sql_02)
       cur.execute(sql_03)
       cur.execute(sql_04)
       cur.execute(sql_05)
       cur.execute(sql_06)
       cur.execute(sql_07)
       cur.execute(sql_08)
       cur.execute(sql_09)
       cur.execute(sql_10)
       cur.execute(sql_11)
       cur.execute(sql_12)
       cur.execute(sql_13)
       cur.execute(sql_14)
       cur.execute(sql_15)
       cur.execute(sql_16)
       # 执行sql语句
       # cur.executemany(sql_all, values)
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
    insertBlueOccurNumData()