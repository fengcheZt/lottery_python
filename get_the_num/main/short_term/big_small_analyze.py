# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
大小号偏态分析
大小号相差8个位偏态
@author: Administrator
"""
from get_the_num.main.getData import get_short_data
import pymysql
from get_the_num.main.common_util.common_business_util import get_sql_id_list_str
def analyzeByBidSmallRatio(results,alternative_results=()):
    merge_results = ()
    for i in results:
        merge_results = merge_results + i
    small_count = 0
    big_count = 0
    for a1 in merge_results:
        if a1 <= 16:
            # 小号
            small_count += 1
        else:
            # 大号
            big_count += 1
    if small_count == 0:
        # 全为大号
        ratio = 100
    else:
        ratio = big_count / small_count
    difference = big_count - small_count
    sql=""
    # 双色球短期分析中大于8的大小号偏态是比较显著的，值得注意
    if abs(difference) >= 8:
        print("大小分析，明显的大小号偏态")
        if big_count > small_count:
            # 寻找大小比小于1的
            # 大号少，小号多
            sql = sql + " WHERE t.big_small_ratio<1"
        else:
            # 大号多，小号少
            sql = sql + " WHERE t.big_small_ratio>1"
    else:
        print("大小分析，没有出现大小号的明显偏态，差值为8为偏态，真正差值为" + str(difference))
    return sql
def getConditionsAfterAnalyzeByBidSmallRatio(args={},results=(),analysisInfo={}):
    merge_results = ()
    for i in results:
        merge_results = merge_results + i
    small_count = 0
    big_count = 0
    for a1 in merge_results:
        if a1 <= 16:
            # 小号
            small_count += 1
        else:
            # 大号
            big_count += 1
    if small_count == 0:
        # 全为大号
        ratio = 100
    else:
        ratio = big_count / small_count
    difference = big_count - small_count
    # 双色球短期分析中大于8的大小号偏态是比较显著的，值得注意
    if abs(difference) >= 8:
        msg='大小分析，明显的大小号偏态'
        print(msg)
        analysisInfo['daxiaoInfo'] = msg
        if big_count > small_count:
            # 寻找大小比小于1的
            # 大号少，小号多
            args['analyzeindex__big_small_ratio__lt']=1
        else:
            # 大号多，小号少
            args['analyzeindex__big_small_ratio__gt'] = 1
    else:
        msg="大小分析，没有出现大小号的明显偏态，差值为8为偏态，真正差值为" + str(difference)
        print(msg)
        analysisInfo['daxiaoInfo'] = msg
    return args
def get_is_skewness_bigsmall(results):
    merge_results = ()
    for i in results:
        merge_results = merge_results + i
    small_count = 0
    big_count = 0
    for a1 in merge_results:
        if a1 <= 16:
            # 小号
            small_count += 1
        else:
            # 大号
            big_count += 1
    if small_count == 0:
        # 全为大号
        ratio = 100
    else:
        ratio = big_count / small_count
    difference = big_count - small_count
    big_small_flg=False
    # 双色球短期分析中大于8的大小号偏态是比较显著的，值得注意
    if abs(difference) >= 8:
        print("大小分析，明显的大小号偏态")
        big_small_flg=True
    else:
        print("大小分析，没有出现大小号的明显偏态，差值为8为偏态，真正差值为" + str(difference))
        big_small_flg=False
    return big_small_flg
def select_big_small_index_data(big_small_flag,alternative_results):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.ALL_SSQ_ID FROM ANALYZE_INDEX t "
    if big_small_flag:
        # 大号多，小号少
        sql=sql+" AND t.big_small_ratio>1"
    else:
        # 大号少，小号多
        sql=sql+" AND t.big_small_ratio<1"

    sql = get_sql_id_list_str(sql, alternative_results)
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
    analyzeByBidSmallRatio(results)