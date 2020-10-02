from django.http import HttpResponse
from django.shortcuts import render
from .main.paintChart.loosing_ratio_chart_red import RedChart
from .main.identifyLottery import winLottery,select_selected_ssqdata
from .main.getData import get_all_last_one_data,get_short_data,get_short_data_all
from .main.insertSSQData import updateSSQData
from .main.short_term.odd_even_shewness_analyze import get_is_skewness
from .main.short_term.big_small_analyze import get_is_skewness_bigsmall
from .main.short_term.prime_analyze import get_is_skewness_prime
from .main.short_term.sum_analyze import get_is_shewness_sum
from .main.paintChart.loosing_ratio_chart_blue import BlueChart
from .main.getHitTheJackpotNo import getHitTheJackpotNo
# Create your views here.
def index(request):
    return render(request,'index.html')
def index02(request):
    return render(request,'index02.html')
def short(request):
    results = get_short_data()
    odd_event_flg=get_is_skewness(results)
    big_small_flg=get_is_skewness_bigsmall(results)
    prime_flg=get_is_skewness_prime(results)
    sum_flg = get_is_shewness_sum(results)
    sum_flg = get_is_shewness_sum(results)
    context = {'odd_event_flg': odd_event_flg,'big_small_flg':big_small_flg,'prime_flg':prime_flg,'sum_flg':sum_flg}
    return render(request,'short.html',context)
def short(request):
    results = get_short_data()
    odd_event_flg=get_is_skewness(results)
    big_small_flg=get_is_skewness_bigsmall(results)
    prime_flg=get_is_skewness_prime(results)
    sum_flg = get_is_shewness_sum(results)
    context = {'odd_event_flg': odd_event_flg,'big_small_flg':big_small_flg,'prime_flg':prime_flg,'sum_flg':sum_flg}
    return render(request,'short.html',context)
def mid(request):
    results = get_losing_data(50, "dict")
    resultsBlue = get_losing_data_blue(50)
    context = {'num_list': results, 'num_list_blue': resultsBlue}
    return render(request, 'mid.html', context)
from .models import LongDhr
from get_the_num.main.getData import get_pair_data
from .models import ThripleNum
def long(request):
    # DHR分析
    results=LongDhr.objects.all()
    results_min=LongDhr.objects.order_by('dhr')[:6]
    results_max = LongDhr.objects.order_by('-dhr')[:6]
    sumDHR=0
    for i in results:
        sumDHR=sumDHR+i.dhr
    averageDHR=sumDHR/33
    # 成对号分析
    results = get_pair_data()
    # 最有可能成对的前5对
    max_possible_pair= results[0:5]
    max_possible_pair_list=[]
    for  i in max_possible_pair:
        max_possible_pair_list.append(i[0])
    # 可能最低成对的前5对
    min_possible_pair=results[len(results) - 5:]
    min_possible_pair_list = []
    for i in min_possible_pair:
        min_possible_pair_list.append(i[0])
    # 成团号
    results_thriple=ThripleNum.objects.order_by('-thriple_count')[:6]
    context = {'num_list': results,'min_list':results_min,'max_list':results_max,'averageDHR':round(averageDHR,2),'max_possible_pair':max_possible_pair_list,'min_possible_pair':min_possible_pair_list,'results_thriple':results_thriple}
    # context = {'odd_event_flg': odd_event_flg,'big_small_flg':big_small_flg,'prime_flg':prime_flg,'sum_flg':sum_flg}
    return render(request,'long.html',context)
red_chart=RedChart()
def electrocardiograpy_index_red(request):
    return render(request, 'electrocardiograpy_index_red.html')
def electrocardiograpy1_red(request):
    return red_chart.paint_ecg1()
def electrocardiograpy2_red(request):
    return red_chart.paint_ecg2()
def electrocardiograpy3_red(request):
    return red_chart.paint_ecg3()
def electrocardiograpy4_red(request):
    return red_chart.paint_ecg4()
def electrocardiograpy5_red(request):
    return red_chart.paint_ecg5()
def electrocardiograpy6_red(request):
    return red_chart.paint_ecg6()

blue_chart=BlueChart()
def electrocardiograpy_index_blue(request):
    return render(request, 'electrocardiograpy_index_blue.html')
def electrocardiograpy1_blue(request):
    return blue_chart.paint_ecg1()
def electrocardiograpy2_blue(request):
    return blue_chart.paint_ecg2()
def electrocardiograpy3_blue(request):
    return blue_chart.paint_ecg3()
def win(request):
    # 中大奖页面
    # 更新最新的数据
    # updateSSQData()
    last_ssqdata = get_all_last_one_data()
    selected_results = select_selected_ssqdata(int(last_ssqdata[7]))
    msgList=winLottery()
    context={'msgList':msgList,'last_ssqdata': last_ssqdata[0:7],'selected_results': selected_results}
    return render(request,'win.html',context)

def short_term_num(request):
    results=get_short_data_all()
    context = {'num_list': results}
    return render(request, 'short_term_num.html', context)

def selectNo(request):
    return render(request,'selectNo.html')
def showWinningNumbers(request):
    results=Ssqdata.objects.all();
    context = {'num_list': results}
    return render(request, 'selectNo.html', context)
def showNo(request):
    results=getHitTheJackpotNo()
    # results = get_short_data_all()
    context = {'num_list': results}
    return render(request,'selectNo.html',context)
from django.core import serializers
import json
from .models import Ssqdata
def getAnalysisNum(request):

    results=getHitTheJackpotNo(request)


    # ret = {'status': True, 'data': None}
    # ret['data']=results
    # result =json.dumps(ret);
    ret = {'status': True, 'data': json.loads(serializers.serialize("json", results['hitNoList'])),'analysisInfo':results['analysisInfo']}

    return HttpResponse(json.dumps(ret),content_type='application/json')
    # return HttpResponse(serializers.serialize("json", results['hitNoList']))
    # return JsonResponse(ret)
def testData1(request):
    a=request.GET['a']
    b=request.GET['b']

    if request.is_ajax():
        ajax_string = 'ajax request: '
    else:
        ajax_string = 'not ajax request: '

    c = int(a) + int(b)
    r = HttpResponse(ajax_string + str(c))
    return r
from get_the_num.main.getData import get_losing_data
from get_the_num.main.getData import get_losing_data_blue
def not_hit_term_table(request):
    results=get_losing_data(50,"dict")
    resultsBlue=get_losing_data_blue(50)
    context = {'num_list': results,'num_list_blue':resultsBlue}
    return render(request, 'mid.html', context)
from get_the_num.main.mid_term.analyze_trend_reversal import getTrendReversalNum
def tendencyRevertAnalysis(request):
    results = get_losing_data(20)
    # 趋势反转分析
    num_list = getTrendReversalNum(results)
    return HttpResponse(json.dumps(num_list), content_type='application/json')
from get_the_num.main.mid_term.analyze_up_three_wave import getUpThreeWaveNum
def upThreeWavesAnalysis(request):
    results = get_losing_data(20)
    # 升三浪分析
    num_list = getUpThreeWaveNum(results)
    return HttpResponse(json.dumps(num_list), content_type='application/json')
from get_the_num.main.mid_term.analyze_down_three_wave import getDownThreeWaveNum
def downThreeWavesAnalysis(request):
    results = get_losing_data(20)
    # 降三浪分析
    num_list = getDownThreeWaveNum(results)
    return HttpResponse(json.dumps(num_list), content_type='application/json')
from get_the_num.main.mid_term.analyze_double_bottom import getDoubleBottom
def midAnalysis(request):
    results = get_losing_data(30)
    # 趋势反转分析
    num_list_revert = getTrendReversalNum(results)
    # 升三浪分析
    num_list_up = getUpThreeWaveNum(results)
    # 降三浪分析
    num_list_down = getDownThreeWaveNum(results)
    # 双底分析
    num_list_double_bottom = getDoubleBottom(results)
    # num_list_revert=[1,2,3]
    # num_list_up = [4, 2, 3]
    # num_list_down = [5, 2, 3]
    ret = {'num_list_revert': num_list_revert, 'num_list_up': num_list_up,'num_list_down': num_list_down,'num_list_double_bottom':num_list_double_bottom}
    return HttpResponse(json.dumps(ret), content_type='application/json')

import traceback
from collections import namedtuple
from .models import SelectedSsqdata
import datetime
# 判断今天是否为周末
def is_week_lastday():
    now = (datetime.datetime.utcnow() + datetime.timedelta(hours=8))
    # 假如今天是周日
    sunday = now.weekday()
    # 如果今天是周日，则返回True
    if sunday == 6:
        return True
    else:
        pass
def recordNum(request):
    """record num will be bought"""
    try:
        willBuyNumList =request.POST.getlist('willBuyNumList')
        # willBuyNumObjList=json.dumps(willBuyNumList[0])
        willBuyNumObjList=[]
        # get max termnum
        last_ssqdata = get_all_last_one_data()
        plus2dateYear = (last_ssqdata[8] + datetime.timedelta(days=2)).strftime("%Y")
        plus3dateYear = (last_ssqdata[8] + datetime.timedelta(days=3)).strftime("%Y")
        previousYear = (last_ssqdata[8]).strftime("%Y")
        if plus2dateYear != previousYear:
            termnum = int(plus2dateYear + '001')
        elif plus3dateYear != previousYear:
            if is_week_lastday(last_ssqdata[8] + datetime.timedelta(days=3)):
                termnum = int(plus2dateYear + '001')
        else:
            termnum = int(last_ssqdata[7]) + 1
        for i in willBuyNumList:
            data=json.loads(i, object_hook=lambda d: namedtuple('data', d.keys())(*d.values()))
            selectedNo=SelectedSsqdata(
                data.red01,
                data.red02,
                data.red03,
                data.red04,
                data.red05,
                data.red06,
                data.blue01,
                termnum
            )
            willBuyNumObjList.append(selectedNo)
        SelectedSsqdata.objects.bulk_create(willBuyNumObjList)
    except Exception as e:
        msg = '记录失败'
        traceback.print_exc()
    else:
        msg='记录成功'
    ret = {'status': True, 'msg':msg}
    return HttpResponse(json.dumps(ret),content_type='application/json')
#每次启动更新最新数据
from get_the_num.main.updateData import updateData
# updateData()