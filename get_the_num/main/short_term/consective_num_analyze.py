# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
连号分析

@author: Administrator
"""
from get_the_num.main.getData import get_short_data

def analyzeConsectiveNum(results):
    no_consective_num_count = 0
    one_two_consective_num_count=0
    other_consective_num_count=0
    for i in results:
        consective_num_count = 0
        for index,value in enumerate(i):
            if index+1==len(i):
                break
            if i[index+1]-i[index]==1:
                consective_num_count+=1
        # 无连号和一组两连号占占比79%
        if consective_num_count==0:
            # 如果为0 代表无连号
            no_consective_num_count+=1
        elif consective_num_count==1:
            # 如果为1 代表一组两连号
            one_two_consective_num_count+=1
        else:
            #其他情况
            other_consective_num_count+=1
    sql=""
    if no_consective_num_count/10 - 0.3612 >0.2:
        # 如果无连号占比概率大于理论概率的百分之二十，说明偏态
        print("连号分析，出现了无连号的明显偏态")
        sql = sql + " AND  t.consective_num_index=12"
    elif one_two_consective_num_count/10 - 0.4312 >0.2:
        print("连号分析，出现了一组两连号的明显偏态")
        sql = sql + " AND  t.consective_num_index=0"
    return sql

def getConditionAfterAnalyzeConsectiveNum(args={},results=(),analysisInfo={}):
    no_consective_num_count = 0
    one_two_consective_num_count=0
    other_consective_num_count=0
    for i in results:
        consective_num_count = 0
        for index,value in enumerate(i):
            if index+1==len(i):
                break
            if i[index+1]-i[index]==1:
                consective_num_count+=1
        # 无连号和一组两连号占占比79%
        if consective_num_count==0:
            # 如果为0 代表无连号
            no_consective_num_count+=1
        elif consective_num_count==1:
            # 如果为1 代表一组两连号
            one_two_consective_num_count+=1
        else:
            #其他情况
            other_consective_num_count+=1
    if no_consective_num_count/10 - 0.3612 >0.2:
        # 如果无连号占比概率大于理论概率的百分之二十，说明偏态
        msg="连号分析，出现了无连号的明显偏态"
        print(msg)
        analysisInfo["lianhao"]=msg
        args['analyzeindex__consective_num_index']=12
    elif one_two_consective_num_count/10 - 0.4312 >0.2:
        msg = "连号分析，出现了一组两连号的明显偏态"
        print(msg)
        analysisInfo["lianhao"] = msg
        args['analyzeindex__consective_num_index'] = 0
    return args
if __name__ =='__main__':
    # insertAllData()
    results=get_short_data()
    alternate_num_list=((2,5,9,11,25,28),(1,5,8,21,25,27))
    list=analyzeConsectiveNum(results)
    print(list)