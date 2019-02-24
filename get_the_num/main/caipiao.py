# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 12:20:43 2018

@author: Administrator
"""
from urllib.request import urlopen
import re,xlwt
def get_3d_html():
    page_num=range(1,3)
    b=''
    for page in page_num:
        url='http://kaijiang.zhcw.com/zhcw/html/3d/list_' \
            +str(page_num[page-1]) \
            +'.html'
        a=urlopen(url)
        html=a.read()
        html=html.decode('utf-8')
        b=b+html
    return b
def get_3d_num():
    html=get_3d_html()
    reg=re.compile(r'<tr>.*?<td align="center">'
                   r'(.*?)</td>.*?<td align="center">'
                   r'(.*?)</td>.*?<td align="center" '
                   r'css="padding-left:20px;">'
                   r'<em>(.*?)</em>.*?<em>(.*?)</em>.*?'
                   r'<em>(.*?)</em></td>',re.S)
    it = re.findall(reg,html)
    return it
def excel_create(ceshi):
    newTable='fucai_3d.xls'
    wb=xlwt.Workbook(encoding = 'utf-8')
    ws= wb.add_sheet('test1')
    headData = ['开奖日期','期号','百位','十位','个位']
    for col in range(0,5):
        ws.write(0,col,headData[col])
    index=1
    for j in ceshi:
        for i in range(0,5):
            print(j[i])
            ws.write(index,i,j[i])
        index +=1
        wb.save(newTable)
if __name__ =='__main__':
    w=get_3d_num()
    excel_create(w)
