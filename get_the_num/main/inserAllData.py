# -*- coding: utf-8 -*-
import pymysql
import itertools
import logging
'''
    插入全部可能的双色球数据
'''
def insertAllData():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql_all = 'INSERT INTO ALL_SSQDATA(RED01, RED02, RED03, RED04,RED05,RED06,BLUE01) VALUES (%s,%s,%s,%s,%s,%s,%s) '
    values = []
    redBall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
               29,
               30, 31, 32, 33]
    blueBall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    redList = list(itertools.combinations(redBall, 6))
    for i in redList:
        for j in blueBall:
            ij = i + (j,)
            values.append(ij)
    try:
       # 执行sql语句
       cur.executemany(sql, values)
       # cur.execute(sql)
       # 提交到数据库执行
       conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
def updateAllDataAllNum():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql_all = 'UPDATE ALL_SSQDATA SET ALLNUM= VALUES (%s,%s,%s,%s,%s,%s,%s) '
    values = []
    redBall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
               29,
               30, 31, 32, 33]
    blueBall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    redList = list(itertools.combinations(redBall, 6))
    for i in redList:
        for j in blueBall:
            ij = i + (j,)
            values.append(ij)
    try:
       # 执行sql语句
       cur.executemany(sql, values)
       # cur.execute(sql)
       # 提交到数据库执行
       conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
def insertAnalyzeIndex():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql_index = 'INSERT INTO ANALYZE_INDEX(ALL_SSQ_ID, ODD_EVEN_RATIO,BIG_SMALL_RATIO,PRIME_NUMBER_COUNT,SUM_VALUE,LOOSE_VALUE,AC_VALUE) VALUES (%s,%s,%s,%s,%s,%s,%s) '
    values = []
    redBall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
               29,
               30, 31, 32, 33]
    blueBall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    redList = list(itertools.combinations(redBall, 6))
    all_count=1
    for i in redList:
        for j in blueBall:
            ij = i + (j,)
            # 获得奇偶比
            odd_event_ratio=get_odd_event_ratio(i)
            # 获得大小比
            big_small_ratio=get_big_small_ratio(i)
            # 获得质数个数
            prime_number_count=get_prime_number_count(i)
            # 获得和值
            sum_value=get_sum_value(i)
            # 获得散度值
            loose_value=get_loose_value(i)
            # 获得AC值
            ac_value=get_ac_value(i)
            index_tuple=(all_count,)+(odd_event_ratio,)+(big_small_ratio,)+(prime_number_count,)+(sum_value,)+(loose_value,)+(ac_value,)
            values.append(index_tuple)
            all_count += 1

    try:
        # 执行sql语句
        cur.executemany(sql_index, values)
        # cur.execute(sql)
        # 提交到数据库执行
        conn.commit()
    except Exception as e:
        logging.exception(e)
        # print(e)
        # 如果发生错误则回滚
        conn.rollback()
    cur.close()
    conn.close()
'''
    获得奇偶比
    ratio =0 代表全为偶数
    ratio =100 代表全为奇数
'''
def get_odd_event_ratio(one_data):
    even_count = 0
    odd_count = 0
    for a1 in one_data:
        if (a1 % 2) == 0:
            even_count += 1
        else:
            # 奇数
            odd_count += 1
    if even_count==0:
        # 全为奇数
        ratio=100
    else:
        ratio = odd_count / even_count
    return round(ratio,2)
'''
    获得大小比
    小等于16认为是小号 16个
    大于16 认为是大号  17个
'''
def get_big_small_ratio(one_data):
    small_count = 0
    big_count = 0
    for a1 in one_data:
        if a1<= 16:
            # 小号
            small_count += 1
        else:
            # 大号
            big_count += 1
    if small_count==0:
        # 全为大号
        ratio=100
    else:
        ratio = big_count / small_count
    return round(ratio,2)
'''
    获得质数个数
    大于1 且仅能被1和自身整除
    2 3 5 7 11 13 17 19 23 29 31
'''
def get_prime_number_count(one_data):
    count = 0
    for num in one_data:
        if num > 1:
            # 查看因子
            for i in range(2, num):
                if (num % i) == 0:
                    # 不是质数
                    break
                else:
                    # 是质数
                    count+=1
    return count
'''
    获得和值
    平均和值为102 （33+1）*6/2
'''
def get_sum_value(one_data):
    sum_value = 0
    for num in one_data:
        sum_value=sum_value+num
    return sum_value
'''
    获得散度值
    散度为5到9 最为常见
'''
def get_loose_value(one_data):
    big_value_list=[]
    for i in range(1, 33):
        list = []
        for num in one_data:
            list.append(abs(i - num))
        big_value_list.append(min(list))
    return max(big_value_list)
'''
    获得算术复杂性（AC值）
    AC值越大，随机性越高，AC值越小，随机性越低
    AC值6,7,8,9概率最高
'''
def get_ac_value(one_data):
    list=[]
    for num in one_data:
        for i in one_data:
            list.append(abs(num-i))
    # 任何一种号码中任意两值的正数差值的个数减去（R-1）R为开奖号码的个数，双色球为6个，此处减一，是为了去除自身相减的情况
    return len(set(list))-(6-1)-1
if __name__ =='__main__':
    # insertAllData()
    insertAnalyzeIndex()
    # print(get_prime_number_count((1,2,3,4,22,30)))