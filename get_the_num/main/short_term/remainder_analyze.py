# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
余数偏态分析
模6 取余
余0   概率15.15%
余1   概率18.18%
余2   概率18.18%
余3   概率18.18%
余4   概率15.15%
余5   概率15.15%
在此定义，当近期中奖号码余数的出现情况与标准相差5%时，可以猜测下期中奖号码可能会有近期出现概率低号码
也可能不会出现出现概率高的号码
当有5%的差距时，认为出现了余数的偏态
@author: Administrator
"""
from getData import get_short_data


def analyzeByRemainderSix(results):
    merge_results = ()
    for i in results:
        merge_results = merge_results + i
    zero_count = 0
    one_count = 0
    two_count=0
    three_count = 0
    four_count = 0
    five_count = 0


    for j in merge_results:
        # 取余数
        remainder_value=j%6
        if remainder_value==0:
            # 余数为0
            zero_count += 1
        elif remainder_value==1:
            # 余数为1
            one_count += 1
        elif remainder_value==2:
            two_count += 1
        elif remainder_value==3:
            three_count += 1
        elif remainder_value==4:
            four_count += 1
        elif remainder_value==5:
            five_count += 1

    zero_ratio=zero_count/60
    one_ratio=one_count/60
    two_ratio=two_count/60
    three_ratio = three_count / 60
    four_ratio = four_count / 60
    five_ratio = five_count / 60
    num_list=[]
    if (zero_ratio-0.1515)>0.05:
        num_list.append([6,12,18,24,30])
    elif (one_ratio-0.1818)>0.05:
        num_list.append([1, 7, 13, 19, 25,31])
    elif (two_ratio - 0.1818) > 0.05:
        num_list.append([2, 8, 14, 20,26, 32])
    elif (three_ratio - 0.1818) > 0.05:
        num_list.append([3, 9, 15, 21, 27, 33])
    elif (four_ratio - 0.1515) > 0.05:
        num_list.append([4, 10, 16, 22, 28])
    elif (five_ratio - 0.1515) > 0.05:
        num_list.append([5, 11, 17, 23, 29])
    else:
        print("没有出现明显的余数偏态")
    print(num_list)


if __name__ =='__main__':
    # insertAllData()
    results=get_short_data()
    analyzeByRemainderSix(results)

