# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
重号分析
重号为1个或2个的比率最高
@author: Administrator
"""
from getData import get_last_one_data


def analyzeDoubleSign(results,alternate_num_list):
    list=[]
    for i in alternate_num_list:
        # 求两个集合的交集
        set1=set(results)
        set2=set(i)
        ll=set1.intersection(set2)
        if 1<=len(ll)<=2:
            list.append(i)
    print("重号分析，筛选的结果集个数为："+str(len(list)))
    return list
if __name__ =='__main__':
    # insertAllData()
    results=get_last_one_data()
    alternate_num_list=((2,5,9,11,25,28),(1,5,8,21,25,27))
    list=analyzeDoubleSign(results,alternate_num_list)
    print(list)