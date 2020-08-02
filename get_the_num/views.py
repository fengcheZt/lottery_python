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
    sum_flg = get_is_shewness_sum(results)
    context = {'odd_event_flg': odd_event_flg,'big_small_flg':big_small_flg,'prime_flg':prime_flg,'sum_flg':sum_flg}
    return render(request,'short.html',context)
def mid(request):

    # context = {'odd_event_flg': odd_event_flg,'big_small_flg':big_small_flg,'prime_flg':prime_flg,'sum_flg':sum_flg}
    return render(request,'mid.html')
def long(request):

    # context = {'odd_event_flg': odd_event_flg,'big_small_flg':big_small_flg,'prime_flg':prime_flg,'sum_flg':sum_flg}
    return render(request,'long.html')
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
    # 更新最新的数据
    updateSSQData()
    last_ssqdata = get_all_last_one_data()
    selected_results = select_selected_ssqdata()
    msg=winLottery()
    context={'msg':msg,'last_ssqdata': last_ssqdata,'selected_results': selected_results}
    return render(request,'win.html',context)

def short_term_num(request):
    results=get_short_data_all()
    context = {'num_list': results}
    return render(request, 'short_term_num.html', context)

def selectNo(request):
    return render(request,'selectNo.html')

def showNo(request):
    results=getHitTheJackpotNo()
    # results = get_short_data_all()
    context = {'num_list': results}
    return render(request,'selectNo.html',context)
from django.core import serializers
import json
from .models import Ssqdata
def testData(request):
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