import pymysql


def get_short_data():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.`red01`,t.`red02`,t.`red03`,t.`red04`,t.`red05`,t.`red06` FROM SSQDATA t ORDER BY ID LIMIT 10"
    try:
       # 执行sql语句
       cur.execute(sql)
       results = cur.fetchall()
       # cur.execute(sql)
       # 提交到数据库执行
       # conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
    return results
def get_short_data_all():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python",cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    sql = "SELECT t.`termNum`, t.`red01`,t.`red02`,t.`red03`,t.`red04`,t.`red05`,t.`red06`,t.`blue01` FROM SSQDATA t ORDER BY TERMNUM DESC LIMIT 10"
    try:
       # 执行sql语句
       cur.execute(sql)
       results = cur.fetchall()
       # cur.execute(sql)
       # 提交到数据库执行
       # conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
    return results
"""
    获得中期数据，前60条
"""
def get_mid_data():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.`termnum`,t.`red01`,t.`red02`,t.`red03`,t.`red04`,t.`red05`,t.`red06` FROM SSQDATA t ORDER BY OPENDATE DESC LIMIT 60"
    try:
       # 执行sql语句
       cur.execute(sql)
       results = cur.fetchall()
       # cur.execute(sql)
       # 提交到数据库执行
       # conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
    return results
"""
    获得中期数据，前60条
"""
def get_all_ssq_data():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.`termnum`,t.`red01`,t.`red02`,t.`red03`,t.`red04`,t.`red05`,t.`red06` FROM SSQDATA t ORDER BY OPENDATE DESC"
    try:
       # 执行sql语句
       cur.execute(sql)
       results = cur.fetchall()
       # cur.execute(sql)
       # 提交到数据库执行
       # conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
    return results
"""
    获得长期数据，前60条
"""
def get_long_data():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.`termnum`,t.`red01`,t.`red02`,t.`red03`,t.`red04`,t.`red05`,t.`red06` FROM SSQDATA t"
    try:
       # 执行sql语句
       cur.execute(sql)
       results = cur.fetchall()
       # cur.execute(sql)
       # 提交到数据库执行
       # conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
    return results
"""
    获得遗漏期数数据
"""
def get_losing_data(count=-1):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.`num_01`,t.`num_02`,t.`num_03`,t.`num_04`,t.`num_05`,t.`num_06`,t.`num_07`,t.`num_08`,t.`num_09`,t.`num_10`,t.`num_11`,t.`num_12`,t.`num_13`,t.`num_14`,t.`num_15`,t.`num_16`,t.`num_17`,t.`num_18`,t.`num_19`,t.`num_20`,t.`num_21`,t.`num_22`,t.`num_23`,t.`num_24`,t.`num_25`,t.`num_26`,t.`num_27`,t.`num_28`,t.`num_29`,t.`num_30`,t.`num_31`,t.`num_32`,t.`num_33`  FROM red_losing_lottery t"
    if count>0:
        sql=sql+" limit "+str(count)
    try:
       # 执行sql语句
       cur.execute(sql)
       results = cur.fetchall()
       # cur.execute(sql)
       # 提交到数据库执行
       # conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
    return results
"""
    获得dhr数据
"""
def get_dhr_data():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.`num`,t.`dhr`  FROM long_dhr t"
    try:
       # 执行sql语句
       cur.execute(sql)
       results = cur.fetchall()
       # cur.execute(sql)
       # 提交到数据库执行
       # conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
    return results
"""
    获得成对数据
"""
def get_pair_data():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.`pair_num`,t.`pair_count`  FROM pair_num t ORDER BY t.pair_count desc"
    try:
       # 执行sql语句
       cur.execute(sql)
       results = cur.fetchall()
       # cur.execute(sql)
       # 提交到数据库执行
       # conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
    return results
"""
    获得成对数据
"""
def get_thriple_data():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.`thriple_num`,t.`thriple_count`  FROM thriple_num t ORDER BY t.thriple_count desc"
    try:
       # 执行sql语句
       cur.execute(sql)
       results = cur.fetchall()
       # cur.execute(sql)
       # 提交到数据库执行
       # conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
    return results
def get_all_data():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.`red01`,t.`red02`,t.`red03`,t.`red04`,t.`red05`,t.`red06` FROM ALL_SSQDATA t"
    try:
       # 执行sql语句
       cur.execute(sql)
       results = cur.fetchall()
       # cur.execute(sql)
       # 提交到数据库执行
       # conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
    return results
"""
    获得6个红球
"""
def get_last_one_data():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.`red01`,t.`red02`,t.`red03`,t.`red04`,t.`red05`,t.`red06` FROM SSQDATA t ORDER BY OPENDATE DESC LIMIT 1"
    try:
       # 执行sql语句
       cur.execute(sql)
       results = cur.fetchall()
       # cur.execute(sql)
       # 提交到数据库执行
       # conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
    return results[0]
"""
    获得6个红球和1个篮球
"""
def get_all_last_one_data():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.`red01`,t.`red02`,t.`red03`,t.`red04`,t.`red05`,t.`red06`,t.`blue01` FROM SSQDATA t ORDER BY OPENDATE DESC LIMIT 1"
    try:
       # 执行sql语句
       cur.execute(sql)
       results = cur.fetchall()
       # cur.execute(sql)
       # 提交到数据库执行
       # conn.commit()
    except Exception as e:
       print(e)
       # 如果发生错误则回滚
       conn.rollback()
    cur.close()
    conn.close()
    return results[0]
def select_index_data(odd_event_flag):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.ALL_SSQ_ID FROM ANALYZE_INDEX t "
    if odd_event_flag:
        # 奇数多，偶数少
        sql=sql+" WHERE t.odd_even_ratio>1"
    else:
        # 奇数少，偶数多
        sql=sql+" WHERE t.odd_even_ratio<1"
    try:
        # 执行sql语句
        cur.execute(sql)
        ABC = cur.fetchall()
        # cur.execute(sql)
        # 提交到数据库执行
        # conn.commit()
    except Exception as e:
        print(e)
        # 如果发生错误则回滚
        conn.rollback()
    cur.close()
    conn.close()
    return ABC
def select_big_small_index_data(big_small_flag):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.ALL_SSQ_ID FROM ANALYZE_INDEX t "
    if big_small_flag:
        # 大号多，小号少
        sql=sql+" WHERE t.big_small_ratio>1"
    else:
        # 大号少，小号多
        sql=sql+" WHERE t.big_small_ratio<1"
    try:
        # 执行sql语句
        cur.execute(sql)
        ABC = cur.fetchall()
        # cur.execute(sql)
        # 提交到数据库执行
        # conn.commit()
    except Exception as e:
        print(e)
        # 如果发生错误则回滚
        conn.rollback()
    cur.close()
    conn.close()
    return ABC
def select_prime_index_data(prime_flag):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t.ALL_SSQ_ID FROM ANALYZE_INDEX t "
    if prime_flag:
        # 质数个数小于2
        sql=sql+" WHERE t.prime_number_count>2"
    else:
        # 质数个数大于2
        sql=sql+" WHERE t.prime_number_count<2"
    try:
        # 执行sql语句
        cur.execute(sql)
        ABC = cur.fetchall()
        # cur.execute(sql)
        # 提交到数据库执行
        # conn.commit()
    except Exception as e:
        print(e)
        # 如果发生错误则回滚
        conn.rollback()
    cur.close()
    conn.close()
    return ABC
def select_sum_index_data(sum_flag):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()

    sql = "SELECT t.ALL_SSQ_ID FROM ANALYZE_INDEX t "
    # 和值在74到129概率最大
    if sum_flag:
        # 和值大于102
        sql=sql+" WHERE t.sum_value>102 and t.sum_value<129"
    else:
        # 和值小于102
        sql=sql+" WHERE t.sum_value<102 and t.sum_value>74"
    try:
        # 执行sql语句
        cur.execute(sql)
        ABC = cur.fetchall()
        # cur.execute(sql)
        # 提交到数据库执行
        # conn.commit()
    except Exception as e:
        print(e)
        # 如果发生错误则回滚
        conn.rollback()
    cur.close()
    conn.close()
    return ABC
def select_loose_index_data():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    # 散度值越大，说明号码越集中，散度值越小，说明号码越分散，散度值5,6,7,8,9最为常见
    sql = "SELECT t.ALL_SSQ_ID FROM ANALYZE_INDEX t WHERE t.loose_value in (5,6,7,8,9)"

    try:
        # 执行sql语句
        cur.execute(sql)
        ABC = cur.fetchall()
        # cur.execute(sql)
        # 提交到数据库执行
        # conn.commit()
    except Exception as e:
        print(e)
        # 如果发生错误则回滚
        conn.rollback()
    cur.close()
    conn.close()
    return ABC
def select_ac_index_data():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    # ac值6,7,8,9最为常见
    sql = "SELECT t.ALL_SSQ_ID FROM ANALYZE_INDEX t WHERE t.ac_value in (6,7,8,9)"

    try:
        # 执行sql语句
        cur.execute(sql)
        ABC = cur.fetchall()
        # cur.execute(sql)
        # 提交到数据库执行
        # conn.commit()
    except Exception as e:
        print(e)
        # 如果发生错误则回滚
        conn.rollback()
    cur.close()
    conn.close()
    return ABC
def select_index_data_sql(condition_sql):
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()
    sql = "SELECT t1.RED01,t1.RED02,t1.RED03,t1.RED04,t1.RED05,t1.RED06,t1.BLUE01 FROM ANALYZE_INDEX t , all_ssqdata t1 WHERE 1=1 and t.all_ssq_id=t1.id"
    if condition_sql != "":
        sql=sql+condition_sql
    try:
        # 执行sql语句
        cur.execute(sql)
        ABC = cur.fetchall()
        # cur.execute(sql)
        # 提交到数据库执行
        # conn.commit()
    except Exception as e:
        print(e)
        # 如果发生错误则回滚
        conn.rollback()
    cur.close()
    conn.close()
    return ABC
if __name__ =='__main__':
    # get_data()
    select_index_data(True)