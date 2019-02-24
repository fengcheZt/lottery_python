"""
    10个号码中6保5型旋转矩阵
"""
from get_the_num.main.getData import get_last_one_data
def get_matrix_10_5_4(selected_num_list=[]):
    matrix_list=[]
    selected_num_list.insert(0,-1)
    list =selected_num_list
    if len(list)==11:
        tupple01 = (list[1], list[2], list[3], list[4], list[5], list[6])
        tupple02 = (list[1], list[2], list[3], list[6], list[9], list[10])
        tupple03 = (list[1], list[2], list[3], list[7], list[8], list[10])
        tupple04 = (list[1], list[2], list[4], list[6], list[7], list[8])
        tupple05 = (list[1], list[2], list[5], list[8], list[9], list[10])
        tupple06 = (list[1], list[3], list[4], list[7], list[9], list[10])
        tupple07 = (list[1], list[4], list[5], list[7], list[8], list[9])

        tupple08 = (list[1], list[5], list[6], list[7], list[9], list[10])
        tupple09 = (list[2], list[3], list[4], list[5], list[7], list[9])
        tupple10 = (list[2], list[3], list[4], list[6], list[8], list[9])
        tupple11 = (list[2], list[4], list[5], list[6], list[7], list[10])
        tupple12 = (list[3], list[4], list[5], list[6], list[8], list[10])
        tupple13 = (list[3], list[5], list[6], list[7], list[8], list[9])
        tupple14 = (list[4], list[6], list[7], list[8], list[9], list[10])

        matrix_list=[tupple01,tupple02,tupple03,tupple04,tupple05,tupple06,tupple07,tupple08,tupple09,tupple10,tupple11,tupple12,tupple13,tupple14]
    else:
        print("备选号码必须为10个数")
    return matrix_list
if __name__ =='__main__':
    last_one=get_last_one_data()
    list=[1,2,3,16,19,21,24,25,28,33]
    results=get_matrix_10_5_4(list)
    for i in results:
        x=set(last_one)
        y=set(i)
        a=x.intersection(y)
        if len(a)>=4:
            print(i)