# -*- coding: utf-8 -*-
import pygal                                                       # First import pygal
from .get_ecg_data import get_losing_data_blue
class BlueChart():
    def __init__(self,limit_count=60):
        self.limit_count=limit_count

    def paint_ecg1(self):
        results=get_losing_data_blue(1,self.limit_count)
        print(len(results))
    
        line_chart = pygal.Line()
        line_chart.title = '单号遗漏比（号码1-5）'
        line_chart.x_labels = map(str, range(1, len(results)))
        line_chart.add('号码：1', get_losing_data_blue(1, self.limit_count))
        line_chart.add('号码：2', get_losing_data_blue(2, self.limit_count))
        line_chart.add('号码：3', get_losing_data_blue(3, self.limit_count))
        line_chart.add('号码：4', get_losing_data_blue(4, self.limit_count))
        line_chart.add('号码：5', get_losing_data_blue(5, self.limit_count))
    
    
        return line_chart.render_django_response()
    def paint_ecg2(self):
    
        results=get_losing_data_blue(1,self.limit_count)
        print(len(results))
    
        line_chart = pygal.Line()
        line_chart.title = '单号遗漏比（号码6-10）'
        line_chart.x_labels = map(str, range(1, len(results)))
    
        line_chart.add('号码：6', get_losing_data_blue(6, self.limit_count))
        line_chart.add('号码：7', get_losing_data_blue(7, self.limit_count))
        line_chart.add('号码：8', get_losing_data_blue(8, self.limit_count))
        line_chart.add('号码：9', get_losing_data_blue(9, self.limit_count))
        line_chart.add('号码：10', get_losing_data_blue(10, self.limit_count))
    
    
        return line_chart.render_django_response()
    def paint_ecg3(self):
    
        results=get_losing_data_blue(1,self.limit_count)
        print(len(results))
    
        line_chart = pygal.Line()
        line_chart.title = '单号遗漏比（号码11-16）'
        line_chart.x_labels = map(str, range(1, len(results)))
    
        line_chart.add('号码：11', get_losing_data_blue(11, self.limit_count))
        line_chart.add('号码：12', get_losing_data_blue(12, self.limit_count))
        line_chart.add('号码：13', get_losing_data_blue(13, self.limit_count))
        line_chart.add('号码：14', get_losing_data_blue(14, self.limit_count))
        line_chart.add('号码：15', get_losing_data_blue(15, self.limit_count))
        line_chart.add('号码：16', get_losing_data_blue(16, self.limit_count))
    
        return line_chart.render_django_response()

if __name__ =='__main__':
    blue_chart=BlueChart(60)