from django.contrib import admin
from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt
app_name='get_the_num'
urlpatterns = [
    path('index/',views.index),
    path('index02/',views.index02),
    path('red_ecg1/',views.electrocardiograpy1_red,name='ecg1'),
    path('red_ecg2/',views.electrocardiograpy2_red,name='ecg2'),
    path('red_ecg3/',views.electrocardiograpy3_red,name='ecg3'),
    path('red_ecg4/',views.electrocardiograpy4_red,name='ecg4'),
    path('red_ecg5/',views.electrocardiograpy5_red,name='ecg5'),
    path('red_ecg6/',views.electrocardiograpy6_red,name='ecg6'),
    path('red_ecg/index/',views.electrocardiograpy_index_red,name='ecgIndex'),
    path('blue_ecg1/',views.electrocardiograpy1_blue,name='blue_ecg1'),
    path('blue_ecg2/',views.electrocardiograpy2_blue,name='blue_ecg2'),
    path('blue_ecg3/',views.electrocardiograpy3_blue,name='blue_ecg3'),
    path('blue_ecg/index/',views.electrocardiograpy_index_blue,name='blue_ecgIndex'),
    path('short/',views.short,name='short'),
    path('win/',views.win,name='win'),
    path('short_term_num/',views.short_term_num,name='short_term'),
    path('mid/',views.mid,name='mid'),
    path('long/',views.long,name='long'),
    path('selectNo/',views.selectNo,name='selectNo'),
    path('showNo/',views.showNo,name='showNo'),
    path('getAnalysisNum/',views.getAnalysisNum,name='getAnalysisNum'),
    # path('notHitTermTable/',views.not_hit_term_table,name='not_hit_term_table'),
    path('tendencyRevertAnalysis/',views.tendencyRevertAnalysis,name='tendencyRevertAnalysis'),
    path('upThreeWavesAnalysis/',views.tendencyRevertAnalysis,name='upThreeWavesAnalysis'),
    path('downThreeWavesAnalysis/',views.tendencyRevertAnalysis,name='downThreeWavesAnalysis'),
    path('midAnalysis/',views.midAnalysis,name='midAnalysis'),
    path('recordNum/',csrf_exempt(views.recordNum),name='recordNum'),
    path('matrix/',csrf_exempt(views.rotaryMaritx),name='matrix'),
    path('selectNumByMatrix/',csrf_exempt(views.selectNumByMatrix),name='selectNumByMatrix'),
]