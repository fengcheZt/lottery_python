
from .getData import get_short_data
import random
from ..models import AllSsqdata
from ..models import AnalyzeIndex
from .short_term.odd_even_shewness_analyze import getConditionsAferAnalyzeByRatio
from .short_term.big_small_analyze import getConditionsAfterAnalyzeByBidSmallRatio
from .short_term.prime_analyze import getConditionsAfterAnalyzeByPrimeCount
from .short_term.sum_analyze import getConditionsAfterAnalyzeBySumValue
from .short_term.ac_analyze import getConditionsAfterAnalyzeByAcValue
from .short_term.loose_analyze import getConditionsAfterAnalyzeByLooseValue
from .short_term.section_analyze import getConditionsAfterAnalyzeBySection
from .short_term.consective_num_analyze import getConditionAfterAnalyzeConsectiveNum

def getHitTheJackpotNo(request):
    # results = AnalyzeIndex.objects.filter(odd_even_ratio=1.00,sum_value=21)

    results = get_short_data()
    # kwargs = {'analyzeindex__odd_even_ratio': 1.00,'analyzeindex__sum_value':21}
    #TODO 重构装饰器模式
    kwargs={}
    analysisInfo={}
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


    # kwargs=getConditionAfterAnalyzeConsectiveNum(kwargs,results)
    # if(kwargs.__len__()==0):
    #     kwargs = {'analyzeindex__odd_even_ratio': 1.00, 'analyzeindex__sum_value': 21}
    # sql='SELECT t3.* FROM analyze_index AS t1 JOIN (SELECT ROUND(RAND() * ((SELECT MAX(id) FROM analyze_index)-(SELECT MIN(id) FROM analyze_index))+(SELECT MIN(id) FROM analyze_index)) AS id) AS t2,all_ssqdata t3 WHERE t1.id >= t2.id and t1.id=t3.id ORDER BY t1.id LIMIT 1'
    count=0
    allresults=[]
    while count!=10:
        kwargs['id'] = random.randint(1, 17721088)
        ssqresult = AllSsqdata.objects.filter(**kwargs)
        if ssqresult.exists():
            allresults=allresults+list(ssqresult)
            count=count+1

    # results=getResultsAferAnalyzeByRatio(results)
    hitNoList=random.sample(allresults,5)
    resultList={"hitNoList":hitNoList,"analysisInfo":analysisInfo}
    return resultList

if __name__ =='__main__':
    print(getHitTheJackpotNo())