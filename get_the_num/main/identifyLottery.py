import pymysql
from .getData import get_all_last_one_data
def select_selected_ssqdata():
    conn = pymysql.connect(host='localhost', user='root', passwd="123456", db="python")
    cur = conn.cursor()

    sql = "SELECT t1.RED01,t1.RED02,t1.RED03,t1.RED04,t1.RED05,t1.RED06,t1.BLUE01 FROM selected_ssqdata t1"

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
def winLottery():
    last_ssqdata = get_all_last_one_data()
    selected_results = select_selected_ssqdata()
    # selected_results=((6,10,14,15,19,23,15),(6,10,14,15,19,23,17),(6,10,14,15,19,24,15),(6,10,14,15,19,24,19),(6,10,14,15,17,24,15),(6,10,14,15,18,29,11),(6,10,14,16,18,29,15),(6,10,14,16,18,29,15),(6,10,11,16,18,29,15),(6,9,11,16,18,29,15),(4,9,11,16,18,29,15))
    msg='经过谷底，才能迎来高峰，再接再厉'
    for i in selected_results:
        right_blue = False
        # 判断篮球是否一样
        if last_ssqdata[len(last_ssqdata) - 1] == i[len(i) - 1]:
            right_blue = True
        last_ssqdata_list = list(last_ssqdata)
        # 删除蓝球
        del last_ssqdata_list[len(last_ssqdata) - 1]
        i_list = list(i)
        # 删除蓝球
        del i_list[len(i_list) - 1]
        set1 = set(last_ssqdata_list)
        set2 = set(i_list)
        ll = set1.intersection(set2)
        # 6+1
        if right_blue and len(ll) == 6:
            print("啊-----，你中大奖了！！！！！！！！！！！！！！,中奖号码为：")
            msg="啊-----，你中大奖了！！！！！！！！！！！！！！,中奖号码为："
            print(i)
        # 6+0
        if not right_blue and len(ll) == 6:
            print("已中二等奖,中奖号码为：")
            msg ="已中二等奖,中奖号码为："
            print(i)
        # 5+1
        if right_blue and len(ll) == 5:
            print("已中三等奖,中奖号码为：")
            msg = "已中三等奖,中奖号码为："
            print(i)
        # 5+0 或4+1
        if not right_blue and len(ll) == 5 or right_blue and len(ll) == 4:
            print("已中四等奖,中奖号码为：")
            msg = "已中四等奖,中奖号码为："
            print(i)
        # 4+0 或3+1
        if not right_blue and len(ll) == 4 or right_blue and len(ll) == 3:
            print("已中五等奖,中奖号码为：")
            msg = "已中五等奖,中奖号码为："
            print(i)
        # 2+1,1+1,0+1
        if right_blue and len(ll) == 2 or right_blue and len(ll) == 1 or right_blue and len(ll) == 0:
            print("已中六等奖,中奖号码为：")
            msg = "已中六等奖,中奖号码为："
            print(i)
    return msg
if __name__ =='__main__':
    winLottery()

