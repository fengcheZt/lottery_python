# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
一组3号分析

@author: Administrator
"""
from getData import get_thriple_data
import pymysql
from itertools import combinations
from common_business_util import get_sql_id_list_str
def analyzeByPair(results):

    print("长期分析，一组3号分析")
    print("最有可能同时出现3个号码一组的前5对为：" + str(results[0:5]) )
    print("同时出现3个号码一组可能最小的后5对为：" + str(results[len(results)-5:]))


if __name__ =='__main__':

    results=get_thriple_data()
    # results=( (1,1,1),(2,2,1),(3,0,1),(4,1,1),(5,2,1),(6,3,1),(7,4,1),(8,5,1),(9,6,0),(10,7,1),(11,8,2),(0,9,3),(1,0,4),(2,1,5),(3,2,6),(4,3,7),(5,4,8),(0,0,9),(1,1,0),(2,2,1),(3,3,2))
    analyzeByPair(results)