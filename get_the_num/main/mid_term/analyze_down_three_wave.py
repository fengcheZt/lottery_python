# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
降三浪分析
第一次出现的间隔为10期以上，第二次出现的间隔为4-8期，第三次出现的间隔0-3期
@author: Administrator
"""
from getData import get_losing_data,get_all_data
from mid_common import getIntersectionResults
import pymysql
from common_business_util import get_sql_id_list_str
def analyzeByDownThreeWave(results,alternative_results=()):
    if len(alternative_results)==0:
        alternative_results=get_all_data()
    trend_num_list=[]
    for index, value in enumerate(results[len(results)-1]):
        if value in range(1,4):
            section_02_value=results[len(results)-value-2][index]
            if section_02_value in range(4,9):
                section_03_value=results[len(results)-value-2-section_02_value-1][index]
                if section_03_value in range(9,12):
                    trend_num_list.append(index+1)
    if len(trend_num_list)==0:
        print("降三浪分析,没有处于该趋势的号码")
    else:
        print("降三浪分析，正处于该趋势的号码为：")
        print(trend_num_list)
    return getIntersectionResults(trend_num_list, alternative_results)

if __name__ =='__main__':
    results=get_losing_data()
    # results=( (1,1,1),(2,2,1),(3,0,1),(4,1,1),(5,2,1),(6,3,1),(7,4,1),(8,5,1),(9,6,0),(10,7,1),(11,8,2),(0,9,3),(1,0,4),(2,1,5),(3,2,6),(4,3,7),(5,4,8),(0,0,9),(1,1,0),(2,2,1),(3,3,2))
    analyzeByDownThreeWave(results)