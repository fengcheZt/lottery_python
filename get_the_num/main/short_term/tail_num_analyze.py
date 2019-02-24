# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
尾号偏态分析
寻找尾号近期出现最少的那个，最为下期号码的预判标准
@author: Administrator
"""
from getData import get_short_data


def analyzeByTailNum(results,alternate_num_list=()):
    merge_results = ()
    for i in results:
        merge_results = merge_results + i
    zero_count = 0
    one_count = 0
    two_count=0
    three_count = 0
    four_count = 0
    five_count = 0
    six_count = 0
    seven_count = 0
    eight_count = 0
    nine_count = 0

    for j in merge_results:
        # 取尾数
        (j, r) = divmod(j, 10)
        if r == 0:
            # 尾数为0
            zero_count += 1
        elif r==1:
            # 尾数为1
            one_count += 1
        elif r==2:
            two_count += 1
        elif r==3:
            three_count += 1
        elif r==4:
            four_count += 1
        elif r==5:
            five_count += 1
        elif r==6:
            six_count += 1
        elif r==7:
            seven_count += 1
        elif r==8:
            eight_count += 1
        elif r==9:
            nine_count += 1

    dict={0:zero_count,1:one_count,2:two_count,3:three_count,4:four_count,5:five_count,6:six_count,7:seven_count,8:eight_count,9:nine_count}
    tail_num=min(dict, key=dict.get)
    # 取最少的尾号的号码列表
    tail_num_list=get_key(dict,dict[tail_num])
    num_list=[]
    for i in range(1,33):
        num=i
        # 取尾数
        (i, r) = divmod(i, 10)
        if r in tail_num_list:
            num_list.append(num)
    print("尾号分析，得出号码列表为："+str(num_list))
    alternate_list=[]
    for i in alternate_num_list:
        set1 = set(i)
        set2 = set(num_list)
        ll = set1.intersection(set2)
        if len(ll)>0:
            alternate_list.append(i)
    print("尾号分析，得出结果集个数为："+str(len(alternate_list)))
    return alternate_list
def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]

if __name__ =='__main__':
    # insertAllData()
    results=get_short_data()
    analyzeByTailNum(results)

