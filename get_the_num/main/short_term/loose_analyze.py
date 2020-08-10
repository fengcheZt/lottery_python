# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
散度分析
散度值越大，说明号码越集中，散度值越小，说明号码越分散，散度值5,6,7,8,9最为常见
@author: Administrator
"""
import pymysql
from get_the_num.main.common_util.common_business_util import get_sql_id_list_str
def analyzeByLooseValue():
    # 散度值越大，说明号码越集中，散度值越小，说明号码越分散，散度值5,6,7,8,9最为常见
    print("散度分析，取散度为5,6,7,8,9的数据")
    return " AND t.loose_value in (5,6,7,8,9)"
def getConditionsAfterAnalyzeByLooseValue(args={},analysisInfo={}):
    # 散度值越大，说明号码越集中，散度值越小，说明号码越分散，散度值5,6,7,8,9最为常见
    args['analyzeindex__loose_value__in']=[5,6,7,8,9]
    msg="散度分析，取散度为5,6,7,8,9的数据"
    print(msg)
    analysisInfo['sanduInfo']=msg
    return args
def select_loose_index_data(alternative_results):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    # 散度值越大，说明号码越集中，散度值越小，说明号码越分散，散度值5,6,7,8,9最为常见
    sql = "SELECT t.ALL_SSQ_ID FROM ANALYZE_INDEX t WHERE t.loose_value in (5,6,7,8,9)"

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
    analyzeByLooseValue()