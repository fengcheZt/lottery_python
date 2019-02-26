# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:42:38 2018

@author: Administrator
"""
from urllib.error import HTTPError
from urllib.request import urlopen
import re,xlwt
import pymysql
import hashlib

from bs4 import BeautifulSoup


def get_ssq_html(get_page_num=0):
    url='http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'
    try:
        a = urlopen(url)
    except HTTPError as e:
        url = 'http://kaijiang.zhcw.com/zhcw/inc/ssq/ssq_wqhg.jsp?pageNum=1'
        a = urlopen(url)
    html=a.read()
    html=html.decode('utf-8')
    totalcount=re.search(r'<p class="pg">.*?<strong>(.*?)</strong>.*?</p>',html).group(1)
    page_num=range(1,int(totalcount)+1)
    b=''
    if get_page_num==0:
        # 取所有数据
        for page in page_num:

            url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_' \
                  + str(page_num[page - 1]) \
                  + '.html'

            try:
                a = urlopen(url)
            except HTTPError as e:
                url = 'http://kaijiang.zhcw.com/zhcw/inc/ssq/ssq_wqhg.jsp?pageNum=' \
                      + str(page_num[page - 1])
                a = urlopen(url)

            html = a.read()
            html = html.decode('utf-8')
            b = b + html
    else:
        # 取指定页数据
        url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_' \
              + str(get_page_num) \
              + '.html'
        try:
            a = urlopen(url)
        except HTTPError as e:
            url = 'http://kaijiang.zhcw.com/zhcw/inc/ssq/ssq_wqhg.jsp?pageNum=' \
                  + str(get_page_num)
            a = urlopen(url)
        html = a.read()
        html = html.decode('utf-8')
        b = b + html
    return b

def get_ssq_num():
    html=get_ssq_html(1)
    reg=re.compile(r'<tr>.*?<td align="center">'
                   r'(.*?)</td>.*?<td align="center">'
                   r'(.*?)</td>.*?<td align="center" '
                   r'css="padding-left:10px;">.*?'
                   r'<em class="rr">(.*?)</em>.*?<em class="rr">(.*?)</em>.*?'
                   r'<em class="rr">(.*?)</em>.*?<em class="rr">(.*?)</em>.*?'
                   r'<em class="rr">(.*?)</em>.*?<em class="rr">(.*?)</em>.*?'
                   r'<em>(.*?)</em></td>'
                  ,re.S)
    it = re.findall(reg,html)
    return it
def parse_one_page():
    html = get_ssq_html(1)
    soup = BeautifulSoup(html, "lxml")
    i=0
    for item in soup.select('tr')[2:-1]:
        yield {
            'openDate':item.select('td')[i].text,
            'termNum':item.select('td')[i+1].text,
            'red01':item.select('td em')[0].text,
            'red02': item.select('td em')[1].text,
            'red03': item.select('td em')[2].text,
            'red04': item.select('td em')[3].text,
            'red05': item.select('td em')[4].text,
            'red06': item.select('td em')[5].text,
            'blue01': item.select('td em')[6].text
        }
def excel_create(ceshi):
    newTable='ssq.xls'
    wb=xlwt.Workbook(encoding = 'utf-8')
    ws= wb.add_sheet('test1')
    headData = ['开奖日期','期号','1','2','3','4','5','6','7']
    for col in range(0,9):
        ws.write(0,col,headData[col])
    index=1
    for j in ceshi:
        for i in range(0,9):
            print(j[i])
            ws.write(index,i,j[i])
        index +=1
        wb.save(newTable)
def insertData():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = 'INSERT INTO SSQDATA(OPENDATE,TERMNUM,RED01, RED02, RED03, RED04,RED05,RED06,BLUE01,HASHCODE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '
    values=[]
    for j in parse_one_page():
        opendate=j['openDate']
        termnum=j['termNum']
        red01=j['red01']
        red02=j['red02']
        red03=j['red03']
        red04=j['red04']
        red05=j['red05']
        red06=j['red06']
        blue01=j['blue01']
        hashStr=opendate+red01+red02+red03+red04+red05+red06+blue01
        # hashcode=hash(str(hashStr))
        # bytes(hashStr, encoding="utf8")
        m = hashlib.md5(bytes(hashStr, encoding="utf8"))
        hashcode = m.hexdigest()

        querySql='SELECT COUNT(1) FROM SSQDATA T WHERE T.HASHCODE ="%s"'% (hashcode)
        cur.execute(querySql)
        data = cur.fetchone()

        if(data[0]==0):
            value=(opendate, termnum,red01,red02,red03,red04,red05,red06,blue01,hashcode)
            values.append(value)


    try:
       # 执行sql语句
       cur.executemany(sql, values)
       # cur.execute(sql)
       # 提交到数据库执行
       conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()


def updateSSQData():
    # ceshi = get_ssq_num()
    insertData()
if __name__ =='__main__':
    updateSSQData()
    # parse_one_page()