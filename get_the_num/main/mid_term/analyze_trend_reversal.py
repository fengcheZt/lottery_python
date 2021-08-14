# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
趋势反转分析
10期以上未出现，出现1次后，在紧接着的两期又出现1次
@author: Administrator
"""
from get_the_num.main.getData import get_losing_data,get_all_data
from get_the_num.main.mid_term.mid_common import getIntersectionResults
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

# 获得处于趋势反转的号码
def getTrendReversalNum(results,analysisInfo={}):
    trend_num_list=[]
    for index, value in enumerate(results[len(results)-4]):
        if index ==0:
            continue
        # 10期以上未出现，出现1次后，在紧接着的两期又出现1次
        if value>10 and results[len(results)-3][index]==0 and (results[len(results)-2][index]==0 or results[len(results)-1][index]==0):
            trend_num_list.append(index+1)
    if len(trend_num_list) == 0:
        msg = "趋势反转分析,没有处于该趋势的号码"
        print(msg)
        analysisInfo['qushiInfo'] = msg
    else:
        msg = "趋势反转分析，正处于该趋势的号码为：" + str(trend_num_list)
        print(msg)
        analysisInfo['qushiInfo'] = msg

    return trend_num_list

# 获得sql 条件
def getConditionByTrendReversalNum(args={},results=(),analysisInfo={}):
    trend_num_list = []
    for index, value in enumerate(results[len(results) - 4]):
        if index == 0:
            continue
        # 10期以上未出现，出现1次后，在紧接着的两期又出现1次
        if value > 10 and results[len(results) - 3][index] == 0 and (
                results[len(results) - 2][index] == 0 or results[len(results) - 1][index] == 0):
            trend_num_list.append(index + 1)
    if len(trend_num_list) == 0:
        msg="趋势反转分析,没有处于该趋势的号码"
        print(msg)
        analysisInfo['qushiInfo']=msg
    else:
        msg ="趋势反转分析，正处于该趋势的号码为："+str(trend_num_list)
        print(msg)
        analysisInfo['qushiInfo']=msg
        args['midallssqdata__num__in'] =args['midallssqdata__num__in']+ trend_num_list

    return args
if __name__ =='__main__':
    # insertAllData()
    results=get_losing_data()
    analyzeByTrendReversal(results)