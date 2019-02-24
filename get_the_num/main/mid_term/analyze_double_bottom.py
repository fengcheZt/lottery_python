# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
双底分析
某个号码间隔5-8期出现，然后又相隔了相同的期数，可以相差1期
@author: Administrator
"""
from getData import get_losing_data,get_all_data
from mid_common import getIntersectionResults
import pymysql
from common_business_util import get_sql_id_list_str
def analyzeByDoubleBottom(results,alternative_results=()):
    if len(alternative_results)==0:
        alternative_results=get_all_data()
    trend_num_list=[]
    for index, value in enumerate(results[len(results)-1]):
        if value in range(5,9):
            section_02_value=results[len(results)-value-2][index]
            if section_02_value in range(value-1,value+2):
                trend_num_list.append(index+1)
    if len(trend_num_list)==0:
        print("双底分析,没有处于该趋势的号码")
    else:
        print("双底分析，正处于该趋势的号码为：")
        print(trend_num_list)
    return getIntersectionResults(trend_num_list, alternative_results)

if __name__ =='__main__':
    results=get_losing_data()
    # results=((1,1,1),(2,2,2),(3,3,3),(4,4,0),(5,0,1),(0,1,2),(1,2,3),(2,3,4),(3,4,5),(4,5,6),(5,6,7))
    analyzeByDoubleBottom(results)