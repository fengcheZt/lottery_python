# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
和偏态分析
双色球短期分析中大于20的和值偏态是比较显著的，值得注意
74到129的和值区间概率最大
@author: Administrator
"""
from get_the_num.main.getData import get_last_one_data
import pymysql
from get_the_num.main.common_util.common_business_util import get_sql_id_list_str
def analyzeBySumValue(results):
    sum_value = 0
    for num in results[0]:
        sum_value = sum_value + num
    sql=""
    # 双色球短期分析中大于20的和值偏态是比较显著的，值得注意
    if abs(sum_value-102) >= 20:
        print("和值分析，明显的和数偏态")
        if sum_value > 102:
            # 寻找和值小于102
            # 和值小于102
            sql = sql + " AND t.sum_value<102 and t.sum_value>74"
        else:
            # 寻找和值大于102
            # 和值大于102
            sql = sql + " AND t.sum_value>102 and t.sum_value<129"
    else:
        print("和值分析，没有出现和值的明显偏态，当和值与102相差20时为偏态，差值为" + str(sum_value-102))
    return sql
def get_is_shewness_sum(results):
    sum_value = 0
    for num in results[0]:
        sum_value = sum_value + num
    sql=""
    sum_flg=False
    # 双色球短期分析中大于20的和值偏态是比较显著的，值得注意
    if abs(sum_value-102) >= 20:
        print("和值分析，明显的和数偏态")
        sum_flg=True
    else:
        print("和值分析，没有出现和值的明显偏态，当和值与102相差20时为偏态，差值为" + str(sum_value-102))
        sum_flg = False
    return sql
def select_sum_index_data(sum_flag,alternative_results):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()

    sql = "SELECT t.ALL_SSQ_ID FROM ANALYZE_INDEX t "
    # 和值在74到129概率最大
    if sum_flag:
        # 和值大于102
        sql=sql+" WHERE t.sum_value>102 and t.sum_value<129"
    else:
        # 和值小于102
        sql=sql+" WHERE t.sum_value<102 and t.sum_value>74"

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
    results=get_last_one_data()
    analyzeBySumValue(results)