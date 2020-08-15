# -*- coding: utf-8 -*-
import pymysql
from get_the_num.main.getData import get_long_data
import itertools
import logging
'''
    插入全部可能的双色球数据
'''
def insertDHRData(results):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql_all = 'INSERT INTO long_dhr(num,appear_1,appear_2,appear_3,appear_4,appear_5,dhr) VALUES (%s,%s,%s,%s,%s,%s,%s) '
    values = []

    for num in range(1,34):
        continious_1 = 0
        continious_2 = 0
        continious_3 = 0
        continious_4 = 0
        continious_5 = 0
        jump_index = 0
        for index, value in enumerate(results):
            if jump_index==len(results):
                break
            if index<jump_index:
                continue
            jump_index = index
            if num in value:
                if index + 1 > len(results)-1:
                    continious_1 += 1
                    break
                if num in results[index + 1]:
                    if index + 2 > len(results) - 1:
                        continious_2 += 1
                        break
                    if num in results[index + 2]:
                        if index + 3 > len(results) - 1:
                            continious_3 += 1
                            break
                        if num in results[index + 3]:
                            if index + 4 > len(results) - 1:
                                continious_4 += 1
                                break
                            if num in results[index + 4]:
                                continious_5 += 1
                                jump_index = index + 6
                            else:
                                continious_4 += 1
                                jump_index = index + 5
                        else:
                            continious_3+=1
                            jump_index = index + 4
                    else:
                        continious_2+=1
                        jump_index = index + 3
                else:
                    continious_1+=1
                    jump_index=index+2
            else:
                continue
        if (continious_2+continious_3+continious_4+continious_5)==0:
            dhr=100
        else:
            dhr = continious_1 / (continious_2 + continious_3 + continious_4 + continious_5)
        tuple_value=(num,continious_1,continious_2,continious_3,continious_4,continious_5,dhr)
        # print((1,continious_11,continious_12,continious_13,continious_14,continious_15,dhr))
        values.append(tuple_value)
    try:
       del_sql="TRUNCATE TABLE long_dhr"
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
def updateDHR():
    results = get_long_data()
    insertDHRData(results)
if __name__ =='__main__':
    results=get_long_data()
    # results=((3,5,9,11,25,28),(1,5,9,11,25,28),(2,5,9,11,25,28),(1,5,9,11,25,28),(1,5,9,11,25,28),(1,5,9,11,25,28),(2,5,9,11,25,28),(1,5,9,11,25,28),(1,5,9,11,25,28),(2,5,9,11,25,28),(1,5,9,11,25,28),(1,5,9,11,25,28),(2,5,9,11,25,28),(2,5,9,11,25,28),(1,5,9,11,25,28),(1,5,9,11,25,28),(1,5,9,11,25,28),(1,5,9,11,25,28),(2,5,9,11,25,28),(2,5,9,11,25,28),)
    insertDHRData(results)
    # print(get_prime_number_count((1,2,3,4,22,30)))