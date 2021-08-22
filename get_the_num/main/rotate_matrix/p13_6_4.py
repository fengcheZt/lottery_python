"""
    13个号码中6保4型旋转矩阵
"""
from get_the_num.main.getData import get_last_one_data
import random
def get_matrix_13_6_4(selected_num_list=[],selected_blue_num_list=[]):

    matrix_list=[]
    selected_num_list.insert(0,-1)
    list =selected_num_list
    if len(list)==14:
        tupple01 = (list[1], list[2], list[3], list[6], list[7], list[12],random.choice(selected_blue_num_list))
        tupple02 = (list[1], list[4], list[5], list[8], list[9], list[10],random.choice(selected_blue_num_list))
        tupple03 = (list[1], list[4], list[6], list[8], list[10], list[13],random.choice(selected_blue_num_list))
        tupple04 = (list[1], list[5], list[6], list[9], list[10], list[11],random.choice(selected_blue_num_list))
        tupple05 = (list[1], list[5], list[7], list[10], list[11], list[13],random.choice(selected_blue_num_list))
        tupple06 = (list[2], list[3], list[4], list[8], list[11], list[12],random.choice(selected_blue_num_list))
        tupple07 = (list[2], list[3], list[5], list[9], list[12], list[13], random.choice(selected_blue_num_list))
        tupple08 = (list[2], list[3], list[6], list[7], list[10], list[12], random.choice(selected_blue_num_list))
        tupple09 = (list[4], list[5], list[6], list[7], list[8], list[11], random.choice(selected_blue_num_list))
        tupple10 = (list[4], list[7], list[8], list[9], list[11], list[13], random.choice(selected_blue_num_list))


        matrix_list=[tupple01,tupple02,tupple03,tupple04,tupple05,tupple06,tupple07,tupple08,tupple09,tupple10]
    else:
        print("备选号码必须为13个数")
    return matrix_list
if __name__ =='__main__':
    last_one=get_last_one_data()
    list=[1,2,3,16,19,21,24,25,28,33]
    results=get_matrix_13_6_4(list)
    for i in results:
        x=set(last_one)
        y=set(i)
        a=x.intersection(y)
        if len(a)>=4:
            print(i)