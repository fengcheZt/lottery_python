# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
趋势反转分析
10期以上未出现，出现1次后，在紧接着的两期又出现1次
@author: Administrator
"""
from getData import get_losing_data,get_all_data
from mid_common import getIntersectionResults
import pymysql
from common_business_util import get_sql_id_list_str
def analyzeByTrendReversal(results,alternative_results=()):
    if len(alternative_results)==0:
        alternative_results=get_all_data()
    trend_num_list=[]
    for index, value in enumerate(results[len(results)-4]):
        # 10期以上未出现，出现1次后，在紧接着的两期又出现1次
        if value>10 and results[len(results)-3][index]==0 and (results[len(results)-2][index]==0 or results[len(results)-1][index]==0):
            trend_num_list.append(index+1)
    if len(trend_num_list)==0:
        print("趋势反转分析,没有处于该趋势的号码")
    else:
        print("趋势反转分析，正处于该趋势的号码为：")
        print(trend_num_list)
    return getIntersectionResults(trend_num_list, alternative_results)

if __name__ =='__main__':
    # insertAllData()
    results=get_losing_data()
    analyzeByTrendReversal(results)