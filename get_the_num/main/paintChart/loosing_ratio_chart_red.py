# -*- coding: utf-8 -*-
import pygal                                                       # First import pygal
from .get_ecg_data import get_losing_data
class RedChart():
    def __init__(self,limit_count=60):
        self.limit_count=limit_count
    def paint_ecg1(self):
    
        results=get_losing_data(1,self.limit_count)
        print(len(results))
    
        line_chart = pygal.Line()
        line_chart.title = '单号遗漏比（号码1-5）'
        line_chart.x_labels = map(str, range(1, len(results)))
        line_chart.add('号码：1', get_losing_data(1, self.limit_count))
        line_chart.add('号码：2', get_losing_data(2, self.limit_count))
        line_chart.add('号码：3', get_losing_data(3, self.limit_count))
        line_chart.add('号码：4', get_losing_data(4, self.limit_count))
        line_chart.add('号码：5', get_losing_data(5, self.limit_count))
    
    
        return line_chart.render_django_response()
    def paint_ecg2(self):
    
        results=get_losing_data(1,self.limit_count)
        print(len(results))
    
        line_chart = pygal.Line()
        line_chart.title = '单号遗漏比（号码6-10）'
        line_chart.x_labels = map(str, range(1, len(results)))
    
        line_chart.add('号码：6', get_losing_data(6, self.limit_count))
        line_chart.add('号码：7', get_losing_data(7, self.limit_count))
        line_chart.add('号码：8', get_losing_data(8, self.limit_count))
        line_chart.add('号码：9', get_losing_data(9, self.limit_count))
        line_chart.add('号码：10', get_losing_data(10, self.limit_count))
    
    
        return line_chart.render_django_response()
    def paint_ecg3(self):
    
        results=get_losing_data(1,self.limit_count)
        print(len(results))
    
        line_chart = pygal.Line()
        line_chart.title = '单号遗漏比（号码11-15）'
        line_chart.x_labels = map(str, range(1, len(results)))
    
        line_chart.add('号码：11', get_losing_data(11, self.limit_count))
        line_chart.add('号码：12', get_losing_data(12, self.limit_count))
        line_chart.add('号码：13', get_losing_data(13, self.limit_count))
        line_chart.add('号码：14', get_losing_data(14, self.limit_count))
        line_chart.add('号码：15', get_losing_data(15, self.limit_count))
    
    
        return line_chart.render_django_response()
    def paint_ecg4(self):
        results=get_losing_data(1,self.limit_count)
        print(len(results))
    
        line_chart = pygal.Line()
        line_chart.title = '单号遗漏比（号码16-20）'
        line_chart.x_labels = map(str, range(1, len(results)))
    
        line_chart.add('号码：16', get_losing_data(16, self.limit_count))
        line_chart.add('号码：17', get_losing_data(17, self.limit_count))
        line_chart.add('号码：18', get_losing_data(18, self.limit_count))
        line_chart.add('号码：19', get_losing_data(19, self.limit_count))
        line_chart.add('号码：20', get_losing_data(20, self.limit_count))
    
    
        return line_chart.render_django_response()
    def paint_ecg5(self):
        results=get_losing_data(1,self.limit_count)
        print(len(results))
    
        line_chart = pygal.Line()
        line_chart.title = '单号遗漏比（号码21-25）'
        line_chart.x_labels = map(str, range(1, len(results)))
    
        line_chart.add('号码：21', get_losing_data(21, self.limit_count))
        line_chart.add('号码：22', get_losing_data(22, self.limit_count))
        line_chart.add('号码：23', get_losing_data(23, self.limit_count))
        line_chart.add('号码：24', get_losing_data(24, self.limit_count))
        line_chart.add('号码：25', get_losing_data(25, self.limit_count))
    
    
        return line_chart.render_django_response()
    def paint_ecg6(self):
        results=get_losing_data(1,self.limit_count)
        print(len(results))
    
        line_chart = pygal.Line()
        line_chart.title = '单号遗漏比（号码26-33）'
        line_chart.x_labels = map(str, range(1, len(results)))
    
        line_chart.add('号码：26', get_losing_data(26, self.limit_count))
        line_chart.add('号码：27', get_losing_data(27, self.limit_count))
        line_chart.add('号码：28', get_losing_data(28, self.limit_count))
        line_chart.add('号码：29', get_losing_data(29, self.limit_count))
        line_chart.add('号码：30', get_losing_data(30, self.limit_count))
        line_chart.add('号码：31', get_losing_data(31, self.limit_count))
        line_chart.add('号码：32', get_losing_data(32, self.limit_count))
        line_chart.add('号码：33', get_losing_data(33, self.limit_count))
    
        return line_chart.render_django_response()

if __name__ =='__main__':
    red_chart=RedChart()
    red_chart.paint_ecg1()