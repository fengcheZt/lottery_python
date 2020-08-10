# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
区间偏态分析

@author: Administrator
"""
from get_the_num.main.getData import get_last_one_data


def analyzeBySection():

    sql = " AND t.one_section>0 and t.one_section<4"
    sql =sql+ " AND t.two_section>0 and t.two_section<4"
    sql =sql+ " AND t.three_section>0 and t.three_section<4"
    print("3区间偏态分析，取三区间值在0到4的数据")
    return sql
def getConditionsAfterAnalyzeBySection(args={},analysisInfo={}):

    args['analyzeindex__one_section__gt']=0
    args['analyzeindex__one_section__lt'] = 4
    args['analyzeindex__two_section__gt'] = 0
    args['analyzeindex__two_section__lt'] = 4
    args['analyzeindex__three_section__gt'] = 0
    args['analyzeindex__three_section__lt'] = 4
    msg="3区间偏态分析，取三区间值在0到4的数据"
    print(msg)
    analysisInfo['qujian3Info']=msg
    return args
if __name__ =='__main__':
    # insertAllData()
    results=get_last_one_data()
    analyzeBySection(results)