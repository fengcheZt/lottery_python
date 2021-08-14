
# from get_the_num.models import AllSsqdata
# from django.db.models import Max
# from django.db.models import Min
# from django.db.models import Count

# for i in range(30):
#
#     if i <10:
#         numStr='0'+str(i)
#     ballStr="red"+numStr
#     result1Max = AllSsqdata.objects.filter(ballStr=i).aggregate(Max('id'))
#     result1Min = AllSsqdata.objects.filter(ballStr=i).aggregate(Min('id'))
#     result1Count = AllSsqdata.objects.filter(ballStr=i).aggregate(Count('id'))
#
#     print("---------------------------Num 1---------------------------")
#     print("The count of num 1:" + str(result1Min) + "--" + str(result1Max))
#     print("The range of num 1:" + str(result1Min) + "--" + str(result1Max))

import pymysql
import logging
conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
cur = conn.cursor()
# sqlMinMax = "SELECT  min(id),max(id) FROM all_SSQDATA where red" + numStr + "=" + str(i)
#         sqlCount = "SELECT  count(1) FROM all_SSQDATA where red" + numStr + "=" + str(i)

try:
    for i in range(1,34):
        if i<6:
            print("---------------------------Num " + str(i) + "---------------------------")
            for j in range(1,i+1):
                sqlMinMax = "SELECT  min(id),max(id) FROM all_SSQDATA where red0" + str(j) + "=" + str(i)
                sqlCount = "SELECT  count(1) FROM all_SSQDATA where red0" + str(j) + "=" + str(i)
                # 执行sql语句
                cur.execute(sqlMinMax)
                resultsMaxMin = cur.fetchall()

                cur.execute(sqlCount)
                resultsCount = cur.fetchall()
                print("------------------------Part"+str(j)+" of num "+str(i)+"------------------------")
                print("The count of num " + str(i) + ":" + str(resultsCount[0][0]))
                print("The range of num " + str(i) + ":" + str(resultsMaxMin[0][0]) + "--" + str(resultsMaxMin[0][1]))
        elif i>28:
            print("---------------------------Num " + str(i) + "---------------------------")
            for j in range(1,35-i):
                sqlMinMax = "SELECT  min(id),max(id) FROM all_SSQDATA where red0" + str(j) + "=" + str(i)
                sqlCount = "SELECT  count(1) FROM all_SSQDATA where red0" + str(j) + "=" + str(i)
                # 执行sql语句
                cur.execute(sqlMinMax)
                resultsMaxMin = cur.fetchall()

                cur.execute(sqlCount)
                resultsCount = cur.fetchall()
                print("------------------------Part" + str(j) + " of num " + str(i) + "------------------------")
                print("The count of num " + str(i) + ":" + str(resultsCount[0][0]))
                print("The range of num " + str(i) + ":" + str(resultsMaxMin[0][0]) + "--" + str(resultsMaxMin[0][1]))
        else:
            print("---------------------------Num " + str(i) + "---------------------------")
            for j in range(1,7):
                sqlMinMax = "SELECT  min(id),max(id) FROM all_SSQDATA where red0" + str(j) + "=" + str(i)
                sqlCount = "SELECT  count(1) FROM all_SSQDATA where red0" + str(j) + "=" + str(i)
                # 执行sql语句
                cur.execute(sqlMinMax)
                resultsMaxMin = cur.fetchall()

                cur.execute(sqlCount)
                resultsCount = cur.fetchall()
                print("------------------------Part" + str(j) + " of num " + str(i) + "------------------------")
                print("The count of num " + str(i) + ":" + str(resultsCount[0][0]))
                print("The range of num " + str(i) + ":" + str(resultsMaxMin[0][0]) + "--" + str(resultsMaxMin[0][1]))



        # if i==1:
        #     sqlMinMax = "SELECT  min(id),max(id) FROM all_SSQDATA where red01=1 "
        #     sqlCount = "SELECT  count(1) FROM all_SSQDATA  where red01=1 "
        #     # 执行sql语句
        #     cur.execute(sqlMinMax)
        #     resultsMaxMin = cur.fetchall()
        #
        #     cur.execute(sqlCount)
        #     resultsCount = cur.fetchall()
        #
        #     print("---------------------------Num " + str(i) + "---------------------------")
        #     print("The count of num " + str(i) + ":" + str(resultsCount[0][0]))
        #     print("The range of num " + str(i) + ":" + str(resultsMaxMin[0][0]) + "--" + str(resultsMaxMin[0][1]))
        # elif i==2:
        #     print("---------------------------Num " + str(i) + "---------------------------")
        #     sqlMinMax = "SELECT  min(id),max(id) FROM all_SSQDATA where red01=2 "
        #     sqlCount = "SELECT  count(1) FROM all_SSQDATA  where red01=2 "
        #     # 执行sql语句
        #     cur.execute(sqlMinMax)
        #     resultsMaxMin = cur.fetchall()
        #
        #     cur.execute(sqlCount)
        #     resultsCount = cur.fetchall()
        #
        #     print("------------------------First part of num 2------------------------")
        #     print("The count of num " + str(i) + ":" + str(resultsCount[0][0]))
        #     print("The range of num " + str(i) + ":" + str(resultsMaxMin[0][0]) + "--" + str(resultsMaxMin[0][1]))
        #
        #     sqlMinMax = "SELECT  min(id),max(id) FROM all_SSQDATA where red02=2 "
        #     sqlCount = "SELECT  count(1) FROM all_SSQDATA  where red02=2 "
        #     # 执行sql语句
        #     cur.execute(sqlMinMax)
        #     resultsMaxMin = cur.fetchall()
        #
        #     cur.execute(sqlCount)
        #     resultsCount = cur.fetchall()
        #
        #     print("------------------------Second part of num 2------------------------")
        #     print("The count of num " + str(i) + ":" + str(resultsCount[0][0]))
        #     print("The range of num " + str(i) + ":" + str(resultsMaxMin[0][0]) + "--" + str(resultsMaxMin[0][1]))




   # cur.execute(sql)
   # 提交到数据库执行
   # conn.commit()
except Exception as e:
   logging.exception(e)
   # 如果发生错误则回滚
   conn.rollback()
cur.close()
conn.close()