"""
11组分析全部综合利用，随机选出结果集10个数据
奇偶，大小，质数，和值，ac值,散度值，区间,连号需要查询sql
偏度，尾号，重号
"""
import random
from odd_even_shewness_analyze import analyzeByRatio
from getData import get_short_data
from big_small_analyze import analyzeByBidSmallRatio
from prime_analyze import analyzeByPrimeCount
from sum_analyze import analyzeBySumValue
from ac_analyze import analyzeByAcValue
from loose_analyze import analyzeByLooseValue
from getData import select_index_data_sql
from section_analyze import analyzeBySection
from consective_num_analyze import analyzeConsectiveNum
from leaning_analyze import analyzeLeaningValue
from getData import get_last_one_data
from tail_num_analyze import analyzeByTailNum
from double_sign_analyze import analyzeDoubleSign
from insertSSQData import updateSSQData
from analyze_trend_reversal import analyzeByTrendReversal
from getData import get_losing_data
from analyze_up_three_wave import analyzeByUpThreeWave
from analyze_double_bottom import analyzeByDoubleBottom
from analyze_down_three_wave import analyzeByDownThreeWave
from inserLosingLotteryData import updateLosingLottery
from insertThripleNum import updateThripleData
from inserDHRData import updateDHR
from insertPairNum import updatePairData
from insertSelectedData import insertSelectedData
from updateData import updateData
def analyzeShort():
    # ------------------------------------------ 短期分析
    results = get_short_data()
    # 奇偶比分析
    sql1 = analyzeByRatio(results)
    # 大小号比分析
    sql2 = analyzeByBidSmallRatio(results)
    # 质数分析
    sql3 = analyzeByPrimeCount(results)
    # 和值分析
    sql4 = analyzeBySumValue(results)
    # AC值分析
    sql5 = analyzeByAcValue()
    # 散度分析
    sql6 = analyzeByLooseValue()
    # 区间分析
    sql7 = analyzeBySection()
    # 连号分析
    sql8 = analyzeConsectiveNum(results)
    sql = sql1 + sql2 + sql3 + sql4 + sql5 + sql6 + sql7 + sql8
    alternative_results = select_index_data_sql(sql)

    # 取上一期数据
    result = get_last_one_data()
    # 偏度分析
    # alternative_results = analyzeLeaningValue(result, alternative_results)
    # 尾号分析
    alternative_results = analyzeByTailNum(results, alternative_results)
    # 重号分析
    alternative_results = analyzeDoubleSign(result, alternative_results)
    return alternative_results

def analyzeMid(alternative_results=()):
    results = get_losing_data()
    # 趋势反转分析
    alternative_results=analyzeByTrendReversal(results,alternative_results)
    # 升三浪分析
    alternative_results=analyzeByUpThreeWave(results,alternative_results)
    # 降三浪分析
    alternative_results=analyzeByDownThreeWave(results,alternative_results)
    # 双底分析
    alternative_results = analyzeByDoubleBottom(results, alternative_results)
    return alternative_results
# def analyzeLong(alternative_results=()):

if __name__ =='__main__':
    # 更新最新的数据
    updateData()
    alternative_results=()
    #------------------------------------------ 短期分析
    alternative_results=analyzeShort()
    # ------------------------------------------ 中期分析
    alternative_results=analyzeMid(alternative_results)
    result_list=list(alternative_results)
    if len(result_list)==0:
        print("没有备选号码")
    else:
        the_num_list=[]
        for i in range(0,5):
            the_num = random.randint(0, len(result_list) - 1)
            the_num_list.append(result_list[the_num])
        print(the_num_list)
        # 将选好数据录入数据库
        insertSelectedData(the_num_list)
