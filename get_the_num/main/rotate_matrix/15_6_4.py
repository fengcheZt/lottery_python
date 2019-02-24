"""
    15个号码中6保4型旋转矩阵
"""
from get_the_num.main.getData import get_last_one_data
def get_matrix_10_5_4(selected_num_list=[]):
    matrix_list=[]
    selected_num_list.insert(0,-1)
    list =selected_num_list
    if len(list)==16:
        tupple01 = (list[1], list[2], list[4], list[6], list[11], list[12])
        tupple02 = (list[1], list[3], list[4], list[7], list[13], list[14])
        tupple03 = (list[1], list[3], list[5], list[8], list[10], list[12])
        tupple04 = (list[1], list[4], list[5], list[8], list[9], list[15])
        tupple05 = (list[1], list[6], list[7], list[8], list[13], list[15])
        tupple06 = (list[1], list[9], list[10], list[11], list[14], list[15])
        tupple07 = (list[2], list[3], list[5], list[6], list[9], list[14])

        tupple08 = (list[2], list[3], list[5], list[7], list[9], list[11])
        tupple09 = (list[2], list[3], list[9], list[10], list[12], list[13])
        tupple10 = (list[2], list[4], list[5], list[10], list[13], list[15])
        tupple11 = (list[2], list[7], list[8], list[12], list[14], list[15])
        tupple12 = (list[2], list[8], list[10], list[11], list[13], list[14])
        tupple13 = (list[3], list[4], list[8], list[12], list[14], list[15])
        tupple14 = (list[3], list[6], list[7], list[10], list[12], list[15])

        tupple15 = (list[3], list[6], list[8], list[11], list[13], list[15])
        tupple16 = (list[4], list[6], list[7], list[8], list[9], list[10])
        tupple17 = (list[5], list[6], list[7], list[10], list[11], list[14])
        tupple18 = (list[5], list[6], list[9], list[12], list[13], list[14])
        tupple19 = (list[5], list[7], list[9], list[11], list[12], list[13])

        matrix_list=[tupple01,tupple02,tupple03,tupple04,tupple05,tupple06,tupple07,tupple08,tupple09,tupple10,tupple11,tupple12,tupple13,tupple14,tupple15,tupple16,tupple17,tupple18,tupple19]
    else:
        print("备选号码必须为15个数")
    return matrix_list
if __name__ =='__main__':
    last_one=get_last_one_data()
    list=[1,2,3,4,5,10,11,16,18,21,24,25,28,30,33]
    results=get_matrix_10_5_4(list)
    for i in results:
        x=set(last_one)
        y=set(i)
        a=x.intersection(y)
        if len(a)>=4:
            print(i)