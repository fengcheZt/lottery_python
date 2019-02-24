# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
间距偏态分析
最大间距分析
1到4算小
18到26算大
@author: Administrator
"""
from getData import get_last_one_data


def analyzeInterval(results,alternate_num_list):
    min_interval=100
    max_interval=0
    list=[]
    for index,value in enumerate(results):
        if index + 1 == len(results):
            break
        if results[index + 1] - results[index] > max_interval:
            max_interval=results[index + 1] - results[index]
        if results[index + 1] - results[index] < min_interval:
            min_interval=results[index + 1] - results[index]
    if max_interval>=18:
        print("最大间距出现明显偏态，偏大，最大间距为："+str(max_interval))
    if max_interval<=4:
        print("最大间距出现明显偏态，偏小，最大间距为：" + str(max_interval))
    # if min_interval<=4:
    #     print("最小间距出现明显偏态，最小间距为：" + str(min_interval))
    if 4<max_interval<18 :
        print("间距没有出现明显偏态，最大间距为"+str(max_interval)+"  最小间距为："+str(min_interval))
if __name__ =='__main__':
    # insertAllData()
    results=get_last_one_data()
    alternate_num_list=((2,5,9,11,25,28),(1,5,8,21,25,27))
    list=analyzeInterval(results,alternate_num_list)