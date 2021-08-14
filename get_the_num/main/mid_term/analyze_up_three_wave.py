# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
升三浪分析
第一次出现的间隔为0-3期，第二次出现的间隔为4-8期，第三次出现的间隔在10期左右
@author: Administrator
"""
from get_the_num.main.getData import get_losing_data,get_all_data
def analyzeByUpThreeWave(results,alternative_results=()):
    if len(alternative_results)==0:
        alternative_results=get_all_data()
    trend_num_list=[]
    for index, value in enumerate(results[len(results)-1]):
        if value in range(9,12):
            section_02_value=results[len(results)-value-2][index]
            if section_02_value in range(4,9):
                section_03_value=results[len(results)-value-2-section_02_value-1][index]
                if section_03_value in range(1,4):
                    trend_num_list.append(index+1)
    if len(trend_num_list)==0:
        print("升三浪分析,没有处于该趋势的号码")
    else:
        print("升三浪分析，正处于该趋势的号码为：")
        print(trend_num_list)
    al_results = []
    for i in alternative_results:
        ll = set(i).intersection(set(trend_num_list))
        if len(ll) == 0:
            al_results.append(i)
    if len(al_results) == 0:
        return alternative_results
    else:
        return al_results
def getUpThreeWaveNum(results,analysisInfo={}):
    trend_num_list=[]
    for index, value in enumerate(results[len(results)-1]):
        if value in range(9,12):
            section_02_value=results[len(results)-value-2][index]
            if section_02_value in range(4,9):
                section_03_value=results[len(results)-value-2-section_02_value-1][index]
                if section_03_value in range(1,4):
                    trend_num_list.append(index+1)
    if len(trend_num_list) == 0:
        msg = "升三浪分析,没有处于该趋势的号码"
        print(msg)
        analysisInfo['shengsanlangInfo'] = msg
    else:
        msg = "升三浪分析，正处于该趋势的号码为：" + str(trend_num_list)
        print(msg)
        analysisInfo['shengsanlangInfo'] = msg
    return trend_num_list

def getConditionByUpThreeWaveNum(args={},results=(),analysisInfo={}):
    trend_num_list=[]
    for index, value in enumerate(results[len(results)-1]):
        if value in range(9,12):
            section_02_value=results[len(results)-value-2][index]
            if section_02_value in range(4,9):
                section_03_value=results[len(results)-value-2-section_02_value-1][index]
                if section_03_value in range(1,4):
                    trend_num_list.append(index+1)
    if len(trend_num_list)==0:
        msg = "升三浪分析,没有处于该趋势的号码"
        print(msg)
        analysisInfo['shengsanlangInfo'] = msg
    else:
        msg = "升三浪分析，正处于该趋势的号码为："+str(trend_num_list)
        print(msg)
        analysisInfo['shengsanlangInfo'] = msg
        args['midallssqdata__num__in'] = args['midallssqdata__num__in']+trend_num_list
    return trend_num_list
if __name__ =='__main__':
    results=get_losing_data()
    # results=((1,2,1,1,1),(2,3,1,1,8),(3,0,1,1,0),(0,0,1,1,1),(1,1,1,1,1),(2,2,1,1,1),(3,0,1,1,1),(4,1,1,1,1),(5,2,1,1,1),(0,3,1,8,7),(1,4,1,0,0),(2,0,1,1,1),(3,1,1,1,1),(4,2,1,1,1),(5,3,1,1,1),(6,4,1,1,1),(7,5,1,1,1),(8,6,1,1,1),(9,7,1,1,1),(10,8,1,1,1),(11,9,10,10,10))
    analyzeByUpThreeWave(results)