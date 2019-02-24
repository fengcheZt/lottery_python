import pymysql
def get_losing_data(num,count=-1):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python",cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    if num==1:
        sql = "SELECT t.`num_01`"
    elif num==2:
        sql = "SELECT t.`num_02`"
    elif num==3:
        sql = "SELECT t.`num_03`"
    elif num==4:
        sql = "SELECT t.`num_04`"
    elif num==5:
        sql = "SELECT t.`num_05`"
    elif num==6:
        sql = "SELECT t.`num_06`"
    elif num==7:
        sql = "SELECT t.`num_07`"
    elif num==8:
        sql = "SELECT t.`num_08`"
    elif num==9:
        sql = "SELECT t.`num_09`"
    elif num==10:
        sql = "SELECT t.`num_10`"
    elif num==11:
        sql = "SELECT t.`num_11`"
    elif num==12:
        sql = "SELECT t.`num_12`"
    elif num==13:
        sql = "SELECT t.`num_13`"
    elif num==14:
        sql = "SELECT t.`num_14`"
    elif num==15:
        sql = "SELECT t.`num_15`"
    elif num==16:
        sql = "SELECT t.`num_16`"
    elif num==17:
        sql = "SELECT t.`num_17`"
    elif num==18:
        sql = "SELECT t.`num_18`"
    elif num==19:
        sql = "SELECT t.`num_19`"
    elif num==20:
        sql = "SELECT t.`num_20`"
    elif num==21:
        sql = "SELECT t.`num_21`"
    elif num==22:
        sql = "SELECT t.`num_22`"
    elif num==23:
        sql = "SELECT t.`num_23`"
    elif num==24:
        sql = "SELECT t.`num_24`"
    elif num==25:
        sql = "SELECT t.`num_25`"
    elif num==26:
        sql = "SELECT t.`num_26`"
    elif num==27:
        sql = "SELECT t.`num_27`"
    elif num==28:
        sql = "SELECT t.`num_28`"
    elif num==29:
        sql = "SELECT t.`num_29`"
    elif num==30:
        sql = "SELECT t.`num_30`"
    elif num==31:
        sql = "SELECT t.`num_31`"
    elif num==32:
        sql = "SELECT t.`num_32`"
    elif num==33:
        sql = "SELECT t.`num_33`"

    sql = sql+"as num FROM red_losing_lottery t"
    if count>0:
        sql=sql+" limit "+str(count)
    try:
       # 执行sql语句
       cur.execute(sql)
       results = cur.fetchall()
       results_list =[]
       for i in results:
           results_list.append(i['num']/5.5)
       # cur.execute(sql)
       # 提交到数据库执行
       # conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
    return results_list
def get_losing_data_blue(num,count=-1):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python",cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    if num==1:
        sql = "SELECT t.`num_01`"
    elif num==2:
        sql = "SELECT t.`num_02`"
    elif num==3:
        sql = "SELECT t.`num_03`"
    elif num==4:
        sql = "SELECT t.`num_04`"
    elif num==5:
        sql = "SELECT t.`num_05`"
    elif num==6:
        sql = "SELECT t.`num_06`"
    elif num==7:
        sql = "SELECT t.`num_07`"
    elif num==8:
        sql = "SELECT t.`num_08`"
    elif num==9:
        sql = "SELECT t.`num_09`"
    elif num==10:
        sql = "SELECT t.`num_10`"
    elif num==11:
        sql = "SELECT t.`num_11`"
    elif num==12:
        sql = "SELECT t.`num_12`"
    elif num==13:
        sql = "SELECT t.`num_13`"
    elif num==14:
        sql = "SELECT t.`num_14`"
    elif num==15:
        sql = "SELECT t.`num_15`"
    elif num==16:
        sql = "SELECT t.`num_16`"

    sql = sql+"as num FROM blue_losing_lottery t"
    if count>0:
        sql=sql+" limit "+str(count)
    try:
       # 执行sql语句
       cur.execute(sql)
       results = cur.fetchall()
       results_list =[]
       for i in results:
           results_list.append(i['num']/16)
       # cur.execute(sql)
       # 提交到数据库执行
       # conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
    return results_list