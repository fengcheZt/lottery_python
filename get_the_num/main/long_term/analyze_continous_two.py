# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
连续两期出现比率分析
DHR越小，下一期有可能此号码再次出现，越大，连续出现的几率越低
@author: Administrator
"""
from getData import get_dhr_data
import pymysql
from common_business_util import get_sql_id_list_str
def analyzeByDHR(results):
    max_dhr=0
    min_dhr=100
    max_dhr_num=0
    min_dhr_num=0
    for i in results:
        if i[1]>max_dhr:
            max_dhr=i[1]
            max_dhr_num=i[0]
        if i[1]<min_dhr:
            min_dhr=i[1]
            min_dhr_num = i[0]
    print("长期分析，连续两期DHR分析，DHR越小，越容易连续出现")
    print("最大DHR的号码："+str(max_dhr_num)+"DHR值为："+str(max_dhr))
    print("最小DHR的号码：" + str(min_dhr_num)+"DHR值为："+str(min_dhr))


if __name__ =='__main__':
    results=get_dhr_data()
    # results=( (1,1,1),(2,2,1),(3,0,1),(4,1,1),(5,2,1),(6,3,1),(7,4,1),(8,5,1),(9,6,0),(10,7,1),(11,8,2),(0,9,3),(1,0,4),(2,1,5),(3,2,6),(4,3,7),(5,4,8),(0,0,9),(1,1,0),(2,2,1),(3,3,2))
    analyzeByDHR(results)