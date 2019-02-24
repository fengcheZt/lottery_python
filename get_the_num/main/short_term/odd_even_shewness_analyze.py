# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
奇偶偏态分析
5期分析，奇偶数差8个属于明显偏态
10期分析，奇偶数差12个属于明显偏态
@author: Administrator
"""
import pymysql

from get_the_num.main.common_util.common_business_util import get_sql_id_list_str
from get_the_num.main.getData import get_short_data
def analyzeByRatio(results):
    merge_results = ()
    for i in results:
        merge_results = merge_results + i
    even_count = 0
    odd_count = 0
    for j in merge_results:
        if (j % 2) == 0:
            # 偶数
            even_count += 1
        else:
            # 奇数
            odd_count += 1
    difference = odd_count - even_count
    # 双色球短期分析中大于8的奇偶号偏态是比较显著的，值得注意
    sql=""
    odd_event_index=0
    if len(results)==5:
        odd_event_index=8
    if len(results)==10:
        odd_event_index = 12
    if abs(difference) >= odd_event_index:
        print("奇偶分析，明显的奇偶偏态")
        if odd_count > even_count:
            # 寻找奇偶比小于1的
            # 奇数少，偶数多
            sql = sql + " AND t.odd_even_ratio<1"
        else:
            # 奇数多，偶数少
            sql = sql + " AND t.odd_even_ratio>1"
    else:
        print("奇偶分析，没有出现奇偶的明显偏态，10期分析，差值为12为偏态，5期分析，差值为8为偏态，真正差值为" + str(difference)+"")
    return sql
def get_is_skewness(results):
    merge_results = ()
    for i in results:
        merge_results = merge_results + i
    even_count = 0
    odd_count = 0
    for j in merge_results:
        if (j % 2) == 0:
            # 偶数
            even_count += 1
        else:
            # 奇数
            odd_count += 1
    difference = odd_count - even_count
    # 双色球短期分析中大于8的奇偶号偏态是比较显著的，值得注意
    odd_event_flg=False
    odd_event_index=0
    if len(results)==5:
        odd_event_index=8
    if len(results)==10:
        odd_event_index = 12
    if abs(difference) >= odd_event_index:
        print("奇偶分析，明显的奇偶偏态")
        odd_event_flg=True
    else:
        print("奇偶分析，没有出现奇偶的明显偏态，10期分析，差值为12为偏态，5期分析，差值为8为偏态，真正差值为" + str(difference)+"")
        odd_event_flg = False
    return odd_event_flg
def select_index_data(odd_event_flag, alternative_results):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.ALL_SSQ_ID FROM ANALYZE_INDEX t "
    if odd_event_flag:
        # 奇数多，偶数少
        sql=sql+" WHERE  t.odd_even_ratio>1"
    else:
        # 奇数少，偶数多
        sql=sql+" WHERE t.odd_even_ratio<1"
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

def get_index_data(flg,alternative_results):
    if len(get_index_data)==0:
        return select_index_data(flg)
    else:
        results=select_all_index_data(alternative_results)

def select_all_index_data(alternative_results):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.ALL_SSQ_ID,t.ODD_EVENT_RATIO FROM ANALYZE_INDEX t IN (%s)"% \
          alternative_results
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
    analyzeByRatio(results)
    # results=select_all_index_data([1,2,3])
    # print(results)
    # list=[1.2,3]
    # a=''
    # print(i for i in list)
