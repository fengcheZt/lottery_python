# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
质数偏态分析
10期短期质数个数与理论值（20）相差8个时，属于偏态
@author: Administrator
"""
from get_the_num.main.getData import get_short_data
import pymysql
from get_the_num.main.common_util.common_business_util import get_sql_id_list_str
def analyzeByPrimeCount(results):
    merge_results = ()
    for i in results:
        merge_results = merge_results + i
    count = 0
    for num in merge_results:
        if num > 1:
            # 查看因子
            for i in range(2, num):
                if (num % i) == 0:
                    # 不是质数
                    break
            else:
                # 是质数
                count += 1
    sql=""
    # 双色球短期分析中大于8的质数偏态是比较显著的，值得注意
    if abs(count-20) >= 8:
        print("质数分析，明显的质数偏态")
        if count > 20:
            # 寻找质数个数小于2
            # 质数个数大于2
            sql = sql + " AND t.prime_number_count<2"
        else:
            # 寻找质数个数大于2
            # 质数个数小于2
            sql = sql + " AND t.prime_number_count>2"
    else:
        print("质数分析，没有出现质数的明显偏态，当质数出现的次数与20相差8时为偏态，真正差值为" + str(count-20))
    return sql
def getConditionsAfterAnalyzeByPrimeCount(args={},results=(),analysisInfo={}):
    merge_results = ()
    for i in results:
        merge_results = merge_results + i
    count = 0
    for num in merge_results:
        if num > 1:
            # 查看因子
            for i in range(2, num):
                if (num % i) == 0:
                    # 不是质数
                    break
            else:
                # 是质数
                count += 1
    # 双色球短期分析中大于8的质数偏态是比较显著的，值得注意
    if abs(count-20) >= 8:
        msg='质数分析，明显的质数偏态'
        print(msg)
        analysisInfo['zhishuInfo']=msg
        if count > 20:
            # 寻找质数个数小于2
            # 质数个数大于2
            args['analyzeindex__prime_number_count__lt']=2
        else:
            # 寻找质数个数大于2
            # 质数个数小于2
            args['analyzeindex__prime_number_count__gt'] = 2
    else:
        msg="质数分析，没有出现质数的明显偏态，当质数出现的次数与20相差8时为偏态，真正差值为" + str(count-20)
        print(msg)
        analysisInfo['zhishuInfo'] = msg
    return args
def get_is_skewness_prime(results):
    merge_results = ()
    for i in results:
        merge_results = merge_results + i
    count = 0

    for num in merge_results:
        if num > 1:
            # 查看因子
            for i in range(2, num):
                if (num % i) == 0:
                    # 不是质数
                    break
            else:
                # 是质数
                count += 1
    prime_flg = False
    # 双色球短期分析中大于8的质数偏态是比较显著的，值得注意
    if abs(count-20) >= 8:
        print("质数分析，明显的质数偏态")
        prime_flg=True
    else:
        print("质数分析，没有出现质数的明显偏态，当质数出现的次数与20相差8时为偏态，真正差值为" + str(count-20))
        prime_flg=False
    return prime_flg
def select_prime_index_data(prime_flag,alternative_results):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.ALL_SSQ_ID FROM ANALYZE_INDEX t "
    if prime_flag:
        # 质数个数小于2
        sql=sql+" WHERE t.prime_number_count>2"
    else:
        # 质数个数大于2
        sql=sql+" WHERE t.prime_number_count<2"

    sql=get_sql_id_list_str(sql,alternative_results)

    try:
        # 执行sql语句
        cur.execute(sql)
        ABC = cur.fetchall()
        # cur.execute(sql)
        # 提交到数据库执行
        # conn.commit()
    except Exception as e:
        print(e)
        # 如果发生错误则回滚
        conn.rollback()
    cur.close()
    conn.close()
    return ABC
if __name__ =='__main__':
    # insertAllData()
    results=get_short_data()
    analyzeByPrimeCount(results)