# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
AC值分析
AC值6,7,8,9最为常见
@author: Administrator
"""
import pymysql
from get_the_num.main.common_util.common_business_util import get_sql_id_list_str
def analyzeByAcValue():
    # AC值6,7,8,9最为常见
    sql=" AND t.ac_value in (6,7,8,9)"
    print("ac值分析，取ac值为6,7,8,9的数据")
    return sql
def getConditionsAfterAnalyzeByAcValue(args={},analysisInfo={}):
    # AC值6,7,8,9最为常见
    args['analyzeindex__ac_value__lt']=9
    args['analyzeindex__ac_value__gt'] = 6
    msg="ac值分析，取ac值为6,7,8,9的数据"
    print(msg)
    analysisInfo['acInfo']=msg
    return args
def select_ac_index_data(alternative_results):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    # ac值6,7,8,9最为常见
    sql = "SELECT t.ALL_SSQ_ID FROM ANALYZE_INDEX t WHERE t.ac_value in (6,7,8,9)"
    sql = get_sql_id_list_str(sql, alternative_results)
    try:
        # 执行sql语句
        cur.execute(sql)
        ABC = cur.fetchall()
        # 提交到数据库执行
        # conn.commit()
    except Exception as e:
        print(e)
        # 如果发生错误则回滚
        conn.rollback()
    cur.close()
    conn.close()
    return ABC
        # cur.execute(sql)
if __name__ =='__main__':
    # insertAllData()
    analyzeByAcValue()