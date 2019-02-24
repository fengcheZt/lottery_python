# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
偏度分析
偏度值在2,3,4,5,6,7最为常见，占比81%
@author: Administrator
"""
from getData import get_last_one_data
'''
    偏度分析
    last_one_results  上期的中奖号码
    alternative_results 备选号码
'''
def analyzeLeaningValue(last_one_results,alternative_results):
    sum_value = 0
    # 偏度值在2,3,4,5,6,7最为常见，占比81%
    leaning_list=[2,3,4,5,6,7]
    right_results=()
    for i in alternative_results:
        list2=[]
        for j in i:
            list1=[]
            for x in last_one_results:
                list1.append(abs(j-x))
            list2.append(min(list1))
        if max(list2) in leaning_list:
            right_results=right_results+i
    print("偏度分析后的结果集数量："+str(len(right_results)))
    return right_results
if __name__ =='__main__':
    # insertAllData()
    results=get_last_one_data()
    analyzeLeaningValue(results)