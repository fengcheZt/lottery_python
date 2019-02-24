from django.contrib import admin
from django.urls import path
from . import views
app_name='get_the_num'
urlpatterns = [
    path('index/',views.index),
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
    path('win/',views.win),
    path('short_term_num/',views.short_term_num,name='short_term'),
    path('mid/',views.mid,name='mid'),
    path('long/',views.long,name='long'),

]