# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:34:44 2018
区间偏态分析

@author: Administrator
"""
from getData import get_last_one_data


def analyzeBySection():

    sql = " AND t.one_section>0 and t.one_section<4"
    sql =sql+ " AND t.two_section>0 and t.two_section<4"
    sql =sql+ " AND t.three_section>0 and t.three_section<4"
    print("3区间偏态分析，取三区间值在0到4的数据")
    return sql
if __name__ =='__main__':
    # insertAllData()
    results=get_last_one_data()
    analyzeBySection(results)