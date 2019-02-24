# -*- coding: utf-8 -*-
import pymysql
import itertools
import logging
from inserAllData import get_prime_number_count
def updateIndex():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()

    values = []
    redBall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
               29,
               30, 31, 32, 33]
    blueBall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    redList = list(itertools.combinations(redBall, 6))
    try:
        all_count = 1
        for i in redList:
            for j in blueBall:
                ij = i + (j,)
                # 获得质数个数
                prime_number_count = get_prime_number_count(i)
                index_tuple = (prime_number_count,)+(all_count,)
                sql_index = 'UPDATE ANALYZE_INDEX SET PRIME_NUMBER_COUNT=%s WHERE ALL_SSQ_ID= %s '%index_tuple
                cur.execute(sql_index)
                conn.commit()
                all_count += 1
    except Exception as e:
        logging.exception(e)
        # print(e)
        # 如果发生错误则回滚
        conn.rollback()
    cur.close()
    conn.close()
def updateSectionIndex():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()

    values = []
    redBall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
               29,
               30, 31, 32, 33]
    blueBall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    redList = list(itertools.combinations(redBall, 6))
    sql_index = "INSERT INTO ANALYZE_INDEX(ID,ONE_SECTION,TWO_SECTION,THREE_SECTION) VALUES (%s,%s, %s, %s) " \
                "ON DUPLICATE KEY UPDATE ONE_SECTION = VALUES(ONE_SECTION) , TWO_SECTION = VALUES(TWO_SECTION), THREE_SECTION = VALUES(THREE_SECTION)"
    values=[]

    all_count = 1
    for i in redList:
        for j in blueBall:
            one_section_count = 0
            two_section_count = 0
            three_section_count = 0
            for num in i:
                if 1 <= num <= 11:
                    one_section_count += 1
                elif 12 <= num <= 22:
                    two_section_count += 1
                else:
                    three_section_count += 1


            index_tuple = (all_count,one_section_count,two_section_count,three_section_count)
            # sql_index = 'UPDATE ANALYZE_INDEX SET ONE_SECTION=%s ,TWO_SECTION=%s,THREE_SECTION=%s WHERE ALL_SSQ_ID= %s '%index_tuple
            values.append(index_tuple)
            all_count += 1


    try:
        cur.executemany(sql_index,values)
        conn.commit()
    except Exception as e:
        logging.exception(e)
        # print(e)
        # 如果发生错误则回滚
        conn.rollback()
    cur.close()
    conn.close()


def updateRemainderIndex():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()

    values = []
    redBall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
               29,
               30, 31, 32, 33]
    blueBall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    redList = list(itertools.combinations(redBall, 6))
    sql_index = "INSERT INTO ANALYZE_INDEX(ID,REMAINDER_SIX) VALUES (%s,%s) " \
                "ON DUPLICATE KEY UPDATE REMAINDER_SIX = VALUES(REMAINDER_SIX)"
    values = []

    all_count = 1
    for i in redList:
        for j in blueBall:
            one_section_count = 0
            two_section_count = 0
            three_section_count = 0
            for num in i:
                if 1 <= num <= 11:
                    one_section_count += 1
                elif 12 <= num <= 22:
                    two_section_count += 1
                else:
                    three_section_count += 1

            index_tuple = (all_count, one_section_count, two_section_count, three_section_count)
            # sql_index = 'UPDATE ANALYZE_INDEX SET ONE_SECTION=%s ,TWO_SECTION=%s,THREE_SECTION=%s WHERE ALL_SSQ_ID= %s '%index_tuple
            values.append(index_tuple)
            all_count += 1

    try:
        cur.executemany(sql_index, values)
        conn.commit()
    except Exception as e:
        logging.exception(e)
        # print(e)
        # 如果发生错误则回滚
        conn.rollback()
    cur.close()
    conn.close()
"""
更新连号指标  11个
无连号为0
1组2连号12
1组3连号13
1组4连号14
1组5连号15
1组6连号16
2组2连号22
2组3连号23
3组2连号32
1组2连号+1组3连号1213
1组2连号+1组4连号1214
"""
def updateConsectiveNumIndex():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()

    values = []
    redBall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
               29,
               30, 31, 32, 33]
    blueBall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    redList = list(itertools.combinations(redBall, 6))
    sql_index = "INSERT INTO ANALYZE_INDEX(ID,CONSECTIVE_NUM_INDEX) VALUES (%s,%s) " \
                "ON DUPLICATE KEY UPDATE CONSECTIVE_NUM_INDEX = VALUES(CONSECTIVE_NUM_INDEX)"
    values = []

    all_count = 1
    for i in redList:
        for j in blueBall:


            consective_num_index=0
            consective_num_count = 0

            for index, value in enumerate(i):
                if index + 1 == len(i):
                    break
                if i[index + 1] - i[index] == 1:
                    consective_num_count += 1
            if consective_num_count == 0:
                consective_num_index = 0
            if consective_num_count == 1:
                consective_num_index = 12
            if consective_num_count == 2:
                for index, value in enumerate(i):
                    if i[index + 1] - i[index] == 1:
                        if i[index + 2] - i[index + 1] == 1:
                            consective_num_index = 13
                            break
                        else:
                            consective_num_index = 22
                            break
            if consective_num_count == 3:
                for index, value in enumerate(i):
                    if i[index + 1] - i[index] == 1:
                        if i[index + 2] - i[index + 1] == 1:
                            if i[index + 3] - i[index + 2] == 1:
                                consective_num_index = 14
                                break
                            else:
                                consective_num_index = 1213
                                break
                        else:
                            # 只有从头开始才可以进入以下判断
                            if index == 0:
                                if i[index + 5] - i[index + 4] == 1 and i[index + 4] - i[index + 3] == 1 or i[
                                    index + 4] - i[index + 3] == 1 and i[index + 3] - i[index + 2] == 1:
                                    consective_num_index = 1213
                                    break
                                else:
                                    consective_num_index = 32
                                    break
                            else:
                                # 如果第一个和第二个不相差1，只能是1213
                                consective_num_index = 1213
                                break

            if consective_num_count == 4:
                for index, value in enumerate(i):
                    if i[index + 1] - i[index] == 1:
                        if i[index + 2] - i[index + 1] == 1:
                            if i[index + 3] - i[index + 2] == 1:
                                if i[index + 4] - i[index + 3] == 1:
                                    consective_num_index = 15
                                    break
                                else:
                                    if i[index + 5] - i[index + 4] == 1:
                                        consective_num_index = 1214
                                        break
                            else:
                                consective_num_index = 23
                                break
                        else:
                            consective_num_index = 1214
                            break

            if consective_num_count == 5:
                consective_num_index = 16


            index_tuple = (all_count, consective_num_index)
            # sql_index = 'UPDATE ANALYZE_INDEX SET ONE_SECTION=%s ,TWO_SECTION=%s,THREE_SECTION=%s WHERE ALL_SSQ_ID= %s '%index_tuple
            values.append(index_tuple)
            all_count += 1

    try:
        cur.executemany(sql_index, values)
        conn.commit()
    except Exception as e:
        logging.exception(e)
        # print(e)
        # 如果发生错误则回滚
        conn.rollback()
    cur.close()
    conn.close()
if __name__ =='__main__':
    # updateSectionIndex()
    updateConsectiveNumIndex()
