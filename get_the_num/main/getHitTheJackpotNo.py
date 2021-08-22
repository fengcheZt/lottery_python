from xlwt.compat import xrange

from .getData import get_short_data
from .getData import get_losing_data
import random
from ..models import AllSsqdata
from ..models import AnalyzeIndex
from .short_term.odd_even_shewness_analyze import *
from .short_term.big_small_analyze import *
from .short_term.prime_analyze import *
from .short_term.sum_analyze import *
from .short_term.ac_analyze import *
from .short_term.loose_analyze import *
from .short_term.section_analyze import *
from .short_term.consective_num_analyze import *
from get_the_num.main.mid_term.analyze_double_bottom import *
from get_the_num.main.mid_term.analyze_down_three_wave import *
from get_the_num.main.mid_term.analyze_up_three_wave import *
from get_the_num.main.mid_term.analyze_trend_reversal import *
from get_the_num.models import LongDhr
from get_the_num.main.getData import get_pair_data
from get_the_num.models import ThripleNum
from django.db.models import Q
import datetime
from get_the_num.main.getData import get_losing_data_blue
from get_the_num.main.getData import get_occur_num_data_blue
def getHitTheJackpotNo(request):
    # results = AnalyzeIndex.objects.filter(odd_even_ratio=1.00,sum_value=21)
    kwargs = {}
    analysisInfo = {}
    if request.GET['duanqiFlg'] == 'true':
        # 短期分析
        results = get_short_data()
        # kwargs = {'analyzeindex__odd_even_ratio': 1.00,'analyzeindex__sum_value':21}
        #TODO 重构装饰器模式

        if request.GET['jiouFlg']=='true':
            kwargs = getConditionsAferAnalyzeByRatio(kwargs, results,analysisInfo)
        if request.GET['daxiaoFlg']=='true':
            kwargs = getConditionsAfterAnalyzeByBidSmallRatio(kwargs, results,analysisInfo)
        if request.GET['zhishuFlg']=='true':
            kwargs = getConditionsAfterAnalyzeByPrimeCount(kwargs, results,analysisInfo)
        if request.GET['hezhiFlg']=='true':
            kwargs = getConditionsAfterAnalyzeBySumValue(kwargs, results,analysisInfo)
        if request.GET['acFlg']=='true':
            kwargs = getConditionsAfterAnalyzeByAcValue(kwargs,analysisInfo)
        if request.GET['sanduFlg']=='true':
            kwargs = getConditionsAfterAnalyzeByLooseValue(kwargs,analysisInfo)
        if request.GET['qujian3Flg']=='true':
            kwargs = getConditionsAfterAnalyzeBySection(kwargs,analysisInfo)
        if request.GET['lianhaoFlg']=='true':
            kwargs = getConditionAfterAnalyzeConsectiveNum(kwargs,results,analysisInfo)
    midArgs = []
    if request.GET['zhongqiFlg'] == 'true':
        # 中期分析
        # kwargs['midallssqdata__num__in']=[]
        results = get_losing_data(30)
        trend_num_list=[]
        if request.GET['qushiFlg'] == 'true':
            # 趋势反转分析
            trend_num_list = getTrendReversalNum(results,analysisInfo)
        if request.GET['shengsanlangFlg'] == 'true':
            # 升三浪分析
            trend_num_list = trend_num_list+getUpThreeWaveNum(results,analysisInfo)
        if request.GET['jiangsanlangFlg'] == 'true':
            # 降三浪分析
            trend_num_list =trend_num_list+ getDownThreeWaveNum(results,analysisInfo)
        if request.GET['shuangdiFlg'] == 'true':
            # 双底分析
            trend_num_list = trend_num_list+getDoubleBottom(results,analysisInfo)

    # midargs = (Q(red01__in=trend_num_list) | Q(red02__in=trend_num_list)| Q(red03__in=trend_num_list)| Q(red04__in=trend_num_list)| Q(red05__in=trend_num_list)| Q(red06__in=trend_num_list))
    # kwargs['allnum__contains'] = trend_num_list
    midargs = Q()
    for j in trend_num_list:
        midargs &= Q(allnum__contains=','+str(j)+',')
    # kwargs['allnum__contains'] =','+str(j)+','
    longargs = Q()
    # 长期分析
    if request.GET['dhrFlg'] == 'true':
        # DHR 值越低越容易出现
        results = LongDhr.objects.all()
        results_min = LongDhr.objects.order_by('dhr')[:6]
        msg=''
        for i in list(results_min):
            longargs |= Q(allnum__contains=','+str(i.num)+',')
            msg=msg+str(i.num)+','
        analysisInfo["DHRInfo"] = 'DHR值最低的6个数字：'+msg[0:len(msg)-1]
        print('DHR值最低的6个数字：'+msg[0:len(msg)-1])
    if request.GET['chengduiFlg'] == 'true':
        # 成对号，只取最有可能的号
        results_pair = get_pair_data()
        msg = ''
        for i in list(results_pair[0]):
            longargs &= Q(allnum__contains=','+str(i.num)+',')
            msg = msg + str(i.num) + ','
        analysisInfo["PairInfo"] = '成对号，只取最有可能的号：' + msg[0:len(msg) - 1]
        print('成对号，只取最有可能的号：' + msg[0:len(msg) - 1])
    if request.GET['chengtuanFlg'] == 'true':
        # 成团号，只取最有可能成团的号
        # 成团号
        results_thriple = ThripleNum.objects.order_by('-thriple_count')[:6]
        msg = ''
        for i in list(results_thriple[0]):
            longargs &= Q(allnum__contains=','+str(i.num)+',')
            msg = msg + str(i.num) + ','
        analysisInfo["ThripleInfo"] = '成团号，只取最有可能成团的号：' + msg[0:len(msg) - 1]
        print( '成团号，只取最有可能成团的号：' + msg[0:len(msg) - 1])
    if request.GET['lanFlg'] == 'true':
        resultsBlue = get_losing_data_blue(50)
        dictS = resultsBlue[0].copy()
        del dictS['termnum']
        sortResult = sorted(dictS.items(), key=lambda d: d[1], reverse=True)
        currentLosingResultList = []
        blue01ConditionList=[]
        for value in sortResult:
            currentLosingResult = {}
            currentLosingResult['Num'] = value[0][-2:]
            currentLosingResult['Amount'] = value[1]
            blue01ConditionList.append(int(value[0][-2:]))
            currentLosingResultList.append(currentLosingResult)
        # blueargs &= Q(blue01__in=',' + str(j) + ',')
        # kwargs['blue01__in'] = blue01ConditionList[:3]
        print('蓝球遗漏前三位：' + str(blue01ConditionList[0])+","+str(blue01ConditionList[1])+","+str(blue01ConditionList[2]))
        analysisInfo["LanInfo"] = '蓝球遗漏前三位：' + str(blue01ConditionList[0])+","+str(blue01ConditionList[1])+","+str(blue01ConditionList[2])
    if request.GET['lanOccurNumFlg'] == 'true':
        resultsBlue = get_occur_num_data_blue()
        print('蓝球出现次数最少前三位：' + str(resultsBlue[0]['num']) + "," + str(resultsBlue[1]['num']) + "," + str(resultsBlue[2]['num']))
        analysisInfo["LanOccurNumInfo"] = '蓝球出现次数最少前三位：' + str(resultsBlue[0]['num']) + "," + str(resultsBlue[1]['num']) + "," + str(resultsBlue[2]['num'])
        blue01OccurConditionList=[]
        for value in resultsBlue:
            blue01OccurConditionList.append(int(value['num']))
        # kwargs['blue01__in'] = blue01OccurConditionList[:3]

    kwargs['blue01__in'] = list(set(blue01ConditionList[:3]).union(set(blue01OccurConditionList[:3])))
    #     kwargs['midallssqdata__num__in']= list(set( kwargs['midallssqdata__num__in']))
    # kwargs=getConditionAfterAnalyzeConsectiveNum(kwargs,results)
    # if(kwargs.__len__()==0):
    #     kwargs = {'analyzeindex__odd_even_ratio': 1.00, 'analyzeindex__sum_value': 21}
    # sql='SELECT t3.* FROM analyze_index AS t1 JOIN (SELECT ROUND(RAND() * ((SELECT MAX(id) FROM analyze_index)-(SELECT MIN(id) FROM analyze_index))+(SELECT MIN(id) FROM analyze_index)) AS id) AS t2,all_ssqdata t3 WHERE t1.id >= t2.id and t1.id=t3.id ORDER BY t1.id LIMIT 1'

    # sample = random.sample(xrange(AllSsqdata.objects.filter(**kwargs).count()), 5)
    # result = [AllSsqdata.objects.filter(**kwargs)[i] for i in sample]
    # ssqresult = AllSsqdata.objects.filter(**kwargs).order_by('?')[:2]
    # # results=getResultsAferAnalyzeByRatio(results)
    # ssqresult_list=list(ssqresult)

    count = 0
    allresults = []
    # while count != 10:
        # kwargs['id'] = random.randint(1, 17721088)
    starttime = datetime.datetime.now()
    random.randint(0, 9)
    try:
        ssqresult = AllSsqdata.objects.filter(midargs,longargs,**kwargs)
    except:
        ssqresult = AllSsqdata.objects.filter(midargs,longargs, **kwargs)
    # for i in list(ssqresult):
    #     midJudgeList=[]
    #     # 对结果的再次过滤，过滤出同时包含中期分析数字的号码
    #     midJudgeList=[i.red01]+[i.red02]+[i.red03]+[i.red04]+[i.red05]+[i.red06]
    #     # 判断是否包含
    #     if set(midJudgeList) > set(trend_num_list):
    #         allresults = allresults + [i]

        # count = count + 1

    allresults=list(ssqresult)
    endtime = datetime.datetime.now()
    print('Time consume:'+str((endtime - starttime).seconds))
    if len(allresults)>5:
        hitNoList = random.sample(allresults, 5)
    else:
        hitNoList=allresults
    # hitNoList = allresults
    resultList={"hitNoList":hitNoList,"analysisInfo":analysisInfo,"Total":len(allresults)}
    return resultList

if __name__ =='__main__':
    print(getHitTheJackpotNo())